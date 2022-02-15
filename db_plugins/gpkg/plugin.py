# -*- coding: utf-8 -*-

"""
/***************************************************************************
Name                 : DB Manager
Description          : Database manager plugin for QGIS
Date                 : May 23, 2011
copyright            : (C) 2011 by Giuseppe Sucameli
email                : brush.tyler@gmail.com

 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from builtins import str

# this will disable the dbplugin if the connector raise an ImportError
from .connector import GPKGDBConnector

from qgis.PyQt.QtCore import Qt, QSettings, QFileInfo
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QApplication, QAction, QFileDialog
from qgis.core import QgsDataSourceURI
from qgis.gui import QgsMessageBar

from ..plugin import DBPlugin, Database, Table, VectorTable, RasterTable, TableField, TableIndex, TableTrigger, \
    InvalidDataException

from . import resources_rc
hasattr(resources_rc, 'foo')


def classFactory():
    return GPKGDBPlugin


class GPKGDBPlugin(DBPlugin):

    @classmethod
    def icon(self):
        return QIcon(":/db_manager/gpkg/icon")

    @classmethod
    def typeName(self):
        return 'gpkg'

    @classmethod
    def typeNameString(self):
        return 'GeoPackage'

    @classmethod
    def providerName(self):
        return 'ogr'

    @classmethod
    def connectionSettingsKey(self):
        return '/GPKG/connections'

    def databasesFactory(self, connection, uri):
        return GPKGDatabase(connection, uri)

    def connect(self, parent=None):
        conn_name = self.connectionName()
        settings = QSettings()
        settings.beginGroup(u"/%s/%s" % (self.connectionSettingsKey(), conn_name))

        if not settings.contains("gpkgpath"):  # non-existent entry?
            raise InvalidDataException(u'there is no defined database connection "%s".' % conn_name)

        database = settings.value("gpkgpath")

        uri = QgsDataSourceURI()
        uri.setDatabase(database)
        return self.connectToUri(uri)

    @classmethod
    def addConnection(self, conn_name, uri):
        settings = QSettings()
        settings.beginGroup(u"/%s/%s" % (self.connectionSettingsKey(), conn_name))
        settings.setValue("gpkgpath", uri.database())
        return True

    @classmethod
    def addConnectionActionSlot(self, item, action, parent, index):
        QApplication.restoreOverrideCursor()
        try:
            filename = QFileDialog.getOpenFileName(parent,
                                                   parent.tr("Choose GeoPackage file"), None, "GeoPackage (*.gpkg)")
            if not filename:
                return
        finally:
            QApplication.setOverrideCursor(Qt.WaitCursor)

        conn_name = QFileInfo(filename).fileName()
        uri = QgsDataSourceURI()
        uri.setDatabase(filename)
        self.addConnection(conn_name, uri)
        index.internalPointer().itemChanged()


class GPKGDatabase(Database):

    def __init__(self, connection, uri):
        Database.__init__(self, connection, uri)

    def connectorsFactory(self, uri):
        return GPKGDBConnector(uri)

    def dataTablesFactory(self, row, db, schema=None):
        return GPKGTable(row, db, schema)

    def vectorTablesFactory(self, row, db, schema=None):
        return GPKGVectorTable(row, db, schema)

    def rasterTablesFactory(self, row, db, schema=None):
        return GPKGRasterTable(row, db, schema)

    def info(self):
        from .info_model import GPKGDatabaseInfo

        return GPKGDatabaseInfo(self)

    def sqlResultModel(self, sql, parent):
        from .data_model import GPKGSqlResultModel

        return GPKGSqlResultModel(self, sql, parent)

    def registerDatabaseActions(self, mainWindow):
        action = QAction(self.tr("Run &Vacuum"), self)
        mainWindow.registerAction(action, self.tr("&Database"), self.runVacuumActionSlot)

        Database.registerDatabaseActions(self, mainWindow)

    def runVacuumActionSlot(self, item, action, parent):
        QApplication.restoreOverrideCursor()
        try:
            if not isinstance(item, (DBPlugin, Table)) or item.database() is None:
                parent.infoBar.pushMessage(self.tr("No database selected or you are not connected to it."),
                                           QgsMessageBar.INFO, parent.iface.messageTimeout())
                return
        finally:
            QApplication.setOverrideCursor(Qt.WaitCursor)

        self.runVacuum()

    def runVacuum(self):
        self.database().aboutToChange.emit()
        self.database().connector.runVacuum()
        self.database().refresh()

    def runAction(self, action):
        action = str(action)

        if action.startswith("vacuum/"):
            if action == "vacuum/run":
                self.runVacuum()
                return True

        return Database.runAction(self, action)

    def uniqueIdFunction(self):
        return None

    def toSqlLayer(self, sql, geomCol, uniqueCol, layerName="QueryLayer", layerType=None, avoidSelectById=False, filter=""):
        from qgis.core import QgsVectorLayer

        vl = QgsVectorLayer(self.uri().database(), layerName, 'ogr')
        vl.setSubsetString(sql)
        return vl


class GPKGTable(Table):

    def __init__(self, row, db, schema=None):
        Table.__init__(self, db, None)
        self.name, self.isView, self.isSysTable = row

    def ogrUri(self):
        ogrUri = u"%s|layername=%s" % (self.uri().database(), self.name)
        return ogrUri

    def mimeUri(self):

        # QGIS has no provider to load Geopackage vectors, let's use OGR
        return u"vector:ogr:%s:%s" % (self.name, self.ogrUri())

    def toMapLayer(self):
        from qgis.core import QgsVectorLayer

        provider = "ogr"
        uri = self.ogrUri()

        return QgsVectorLayer(uri, self.name, provider)

    def tableFieldsFactory(self, row, table):
        return GPKGTableField(row, table)

    def tableIndexesFactory(self, row, table):
        return GPKGTableIndex(row, table)

    def tableTriggersFactory(self, row, table):
        return GPKGTableTrigger(row, table)

    def tableDataModel(self, parent):
        from .data_model import GPKGTableDataModel

        return GPKGTableDataModel(self, parent)


class GPKGVectorTable(GPKGTable, VectorTable):

    def __init__(self, row, db, schema=None):
        GPKGTable.__init__(self, row[:-5], db, schema)
        VectorTable.__init__(self, db, schema)
        # GPKG does case-insensitive checks for table names, but the
        # GPKG provider didn't do the same in Qgis < 1.9, so self.geomTableName
        # stores the table name like stored in the geometry_columns table
        self.geomTableName, self.geomColumn, self.geomType, self.geomDim, self.srid = row[-5:]
        self.extent = self.database().connector.getTableExtent((self.schemaName(), self.name), self.geomColumn, force=False)

    def uri(self):
        uri = self.database().uri()
        uri.setDataSource('', self.geomTableName, self.geomColumn)
        return uri

    def hasSpatialIndex(self, geom_column=None):
        geom_column = geom_column if geom_column is not None else self.geomColumn
        return self.database().connector.hasSpatialIndex((self.schemaName(), self.name), geom_column)

    def createSpatialIndex(self, geom_column=None):
        self.aboutToChange.emit()
        ret = VectorTable.createSpatialIndex(self, geom_column)
        if ret is not False:
            self.database().refresh()
        return ret

    def deleteSpatialIndex(self, geom_column=None):
        self.aboutToChange.emit()
        ret = VectorTable.deleteSpatialIndex(self, geom_column)
        if ret is not False:
            self.database().refresh()
        return ret

    def refreshTableEstimatedExtent(self):
        return

    def refreshTableExtent(self):
        prevExtent = self.extent
        self.extent = self.database().connector.getTableExtent((self.schemaName(), self.name), self.geomColumn, force=True)
        if self.extent != prevExtent:
            self.refresh()

    def runAction(self, action):
        if GPKGTable.runAction(self, action):
            return True
        return VectorTable.runAction(self, action)


class GPKGRasterTable(GPKGTable, RasterTable):

    def __init__(self, row, db, schema=None):
        GPKGTable.__init__(self, row[:-3], db, schema)
        RasterTable.__init__(self, db, schema)
        self.prefixName, self.geomColumn, self.srid = row[-3:]
        self.geomType = 'RASTER'
        self.extent = self.database().connector.getTableExtent((self.schemaName(), self.name), self.geomColumn)

    def gpkgGdalUri(self):
        gdalUri = u'GPKG:%s:%s' % (self.uri().database(), self.prefixName)
        return gdalUri

    def mimeUri(self):
        # QGIS has no provider to load rasters, let's use GDAL
        uri = u"raster:gdal:%s:%s" % (self.name, self.uri().database())
        return uri

    def toMapLayer(self):
        from qgis.core import QgsRasterLayer, QgsContrastEnhancement

        # QGIS has no provider to load rasters, let's use GDAL
        uri = self.gpkgGdalUri()
        rl = QgsRasterLayer(uri, self.name)
        if rl.isValid():
            rl.setContrastEnhancement(QgsContrastEnhancement.StretchToMinimumMaximum)
        return rl


class GPKGTableField(TableField):

    def __init__(self, row, table):
        TableField.__init__(self, table)
        self.num, self.name, self.dataType, self.notNull, self.default, self.primaryKey = row
        self.hasDefault = self.default


class GPKGTableIndex(TableIndex):

    def __init__(self, row, table):
        TableIndex.__init__(self, table)
        self.num, self.name, self.isUnique, self.columns = row


class GPKGTableTrigger(TableTrigger):

    def __init__(self, row, table):
        TableTrigger.__init__(self, table)
        self.name, self.function = row
