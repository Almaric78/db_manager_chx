# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/db_manager/ui/DlgSqlLayerWindow.ui'
#
# Created: Sat Sep 16 18:51:46 2017
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DbManagerDlgSqlLayerWindow(object):
    def setupUi(self, DbManagerDlgSqlLayerWindow):
        DbManagerDlgSqlLayerWindow.setObjectName(_fromUtf8("DbManagerDlgSqlLayerWindow"))
        DbManagerDlgSqlLayerWindow.resize(662, 525)
        self.gridLayout_2 = QtGui.QGridLayout(DbManagerDlgSqlLayerWindow)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.avoidSelectById = QtGui.QCheckBox(DbManagerDlgSqlLayerWindow)
        self.avoidSelectById.setObjectName(_fromUtf8("avoidSelectById"))
        self.horizontalLayout_2.addWidget(self.avoidSelectById)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.updateLayerBtn = QtGui.QPushButton(DbManagerDlgSqlLayerWindow)
        self.updateLayerBtn.setObjectName(_fromUtf8("updateLayerBtn"))
        self.horizontalLayout_2.addWidget(self.updateLayerBtn)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.splitter = QtGui.QSplitter(DbManagerDlgSqlLayerWindow)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.queryBuilderBtn = QtGui.QToolButton(self.layoutWidget)
        self.queryBuilderBtn.setText(_fromUtf8(""))
        self.queryBuilderBtn.setObjectName(_fromUtf8("queryBuilderBtn"))
        self.horizontalLayout.addWidget(self.queryBuilderBtn)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.presetCombo = QtGui.QComboBox(self.layoutWidget)
        self.presetCombo.setObjectName(_fromUtf8("presetCombo"))
        self.horizontalLayout.addWidget(self.presetCombo)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.presetName = QtGui.QLineEdit(self.layoutWidget)
        self.presetName.setText(_fromUtf8(""))
        self.presetName.setObjectName(_fromUtf8("presetName"))
        self.horizontalLayout.addWidget(self.presetName)
        self.presetStore = QtGui.QPushButton(self.layoutWidget)
        self.presetStore.setObjectName(_fromUtf8("presetStore"))
        self.horizontalLayout.addWidget(self.presetStore)
        self.presetDelete = QtGui.QPushButton(self.layoutWidget)
        self.presetDelete.setObjectName(_fromUtf8("presetDelete"))
        self.horizontalLayout.addWidget(self.presetDelete)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.editSql = QgsCodeEditorSQL(self.layoutWidget)
        self.editSql.setObjectName(_fromUtf8("editSql"))
        self.verticalLayout_2.addWidget(self.editSql)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.btnExecute = QtGui.QPushButton(self.layoutWidget)
        self.btnExecute.setObjectName(_fromUtf8("btnExecute"))
        self.hboxlayout.addWidget(self.btnExecute)
        self.lblResult = QtGui.QLabel(self.layoutWidget)
        self.lblResult.setText(_fromUtf8(""))
        self.lblResult.setObjectName(_fromUtf8("lblResult"))
        self.hboxlayout.addWidget(self.lblResult)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem2)
        self.btnClear = QtGui.QPushButton(self.layoutWidget)
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.hboxlayout.addWidget(self.btnClear)
        self.verticalLayout_2.addLayout(self.hboxlayout)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.viewResult = QtGui.QTableView(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.viewResult.sizePolicy().hasHeightForWidth())
        self.viewResult.setSizePolicy(sizePolicy)
        self.viewResult.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.viewResult.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.viewResult.setObjectName(_fromUtf8("viewResult"))
        self.verticalLayout.addWidget(self.viewResult)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.uniqueColumnCheck = QtGui.QCheckBox(DbManagerDlgSqlLayerWindow)
        self.uniqueColumnCheck.setObjectName(_fromUtf8("uniqueColumnCheck"))
        self.horizontalLayout_6.addWidget(self.uniqueColumnCheck)
        self.uniqueCombo = QtGui.QComboBox(DbManagerDlgSqlLayerWindow)
        self.uniqueCombo.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uniqueCombo.sizePolicy().hasHeightForWidth())
        self.uniqueCombo.setSizePolicy(sizePolicy)
        self.uniqueCombo.setEditable(True)
        self.uniqueCombo.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.uniqueCombo.setObjectName(_fromUtf8("uniqueCombo"))
        self.horizontalLayout_6.addWidget(self.uniqueCombo)
        self.hasGeometryCol = QtGui.QCheckBox(DbManagerDlgSqlLayerWindow)
        self.hasGeometryCol.setChecked(True)
        self.hasGeometryCol.setTristate(False)
        self.hasGeometryCol.setObjectName(_fromUtf8("hasGeometryCol"))
        self.horizontalLayout_6.addWidget(self.hasGeometryCol)
        self.geomCombo = QtGui.QComboBox(DbManagerDlgSqlLayerWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.geomCombo.sizePolicy().hasHeightForWidth())
        self.geomCombo.setSizePolicy(sizePolicy)
        self.geomCombo.setEditable(True)
        self.geomCombo.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.geomCombo.setObjectName(_fromUtf8("geomCombo"))
        self.horizontalLayout_6.addWidget(self.geomCombo)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.getColumnsBtn = QtGui.QPushButton(DbManagerDlgSqlLayerWindow)
        self.getColumnsBtn.setObjectName(_fromUtf8("getColumnsBtn"))
        self.horizontalLayout_6.addWidget(self.getColumnsBtn)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_5 = QtGui.QLabel(DbManagerDlgSqlLayerWindow)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_7.addWidget(self.label_5)
        self.layerNameEdit = QtGui.QLineEdit(DbManagerDlgSqlLayerWindow)
        self.layerNameEdit.setEnabled(True)
        self.layerNameEdit.setText(_fromUtf8(""))
        self.layerNameEdit.setReadOnly(True)
        self.layerNameEdit.setObjectName(_fromUtf8("layerNameEdit"))
        self.horizontalLayout_7.addWidget(self.layerNameEdit)
        self.layerTypeWidget = QtGui.QWidget(DbManagerDlgSqlLayerWindow)
        self.layerTypeWidget.setObjectName(_fromUtf8("layerTypeWidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layerTypeWidget)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_6 = QtGui.QLabel(self.layerTypeWidget)
        self.label_6.setIndent(40)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.vectorRadio = QtGui.QRadioButton(self.layerTypeWidget)
        self.vectorRadio.setChecked(True)
        self.vectorRadio.setObjectName(_fromUtf8("vectorRadio"))
        self.horizontalLayout_3.addWidget(self.vectorRadio)
        self.rasterRadio = QtGui.QRadioButton(self.layerTypeWidget)
        self.rasterRadio.setObjectName(_fromUtf8("rasterRadio"))
        self.horizontalLayout_3.addWidget(self.rasterRadio)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_7.addWidget(self.layerTypeWidget)
        self.btnSetFilter = QtGui.QPushButton(DbManagerDlgSqlLayerWindow)
        self.btnSetFilter.setAutoDefault(False)
        self.btnSetFilter.setObjectName(_fromUtf8("btnSetFilter"))
        self.horizontalLayout_7.addWidget(self.btnSetFilter)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)

        self.retranslateUi(DbManagerDlgSqlLayerWindow)
        QtCore.QObject.connect(self.hasGeometryCol, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.geomCombo.setEnabled)
        QtCore.QObject.connect(self.uniqueColumnCheck, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.uniqueCombo.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(DbManagerDlgSqlLayerWindow)
        DbManagerDlgSqlLayerWindow.setTabOrder(self.btnExecute, self.btnClear)
        DbManagerDlgSqlLayerWindow.setTabOrder(self.btnClear, self.viewResult)

    def retranslateUi(self, DbManagerDlgSqlLayerWindow):
        DbManagerDlgSqlLayerWindow.setWindowTitle(_translate("DbManagerDlgSqlLayerWindow", "SQL window", None))
        self.avoidSelectById.setToolTip(_translate("DbManagerDlgSqlLayerWindow", "<html><head/><body><p>Avoid selecting feature by id. Sometimes - especially when running expensive queries/views - fetching the data sequentially instead of fetching features by id can be much quicker.</p></body></html>", None))
        self.avoidSelectById.setText(_translate("DbManagerDlgSqlLayerWindow", "Avoid selecting by feature id", None))
        self.updateLayerBtn.setText(_translate("DbManagerDlgSqlLayerWindow", "Update", None))
        self.label.setText(_translate("DbManagerDlgSqlLayerWindow", "Saved query:", None))
        self.label_2.setText(_translate("DbManagerDlgSqlLayerWindow", "Name", None))
        self.presetStore.setText(_translate("DbManagerDlgSqlLayerWindow", "Store", None))
        self.presetDelete.setText(_translate("DbManagerDlgSqlLayerWindow", "Delete", None))
        self.btnExecute.setText(_translate("DbManagerDlgSqlLayerWindow", "&Execute (F5)", None))
        self.btnExecute.setShortcut(_translate("DbManagerDlgSqlLayerWindow", "F5", None))
        self.btnClear.setText(_translate("DbManagerDlgSqlLayerWindow", "&Clear", None))
        self.uniqueColumnCheck.setText(_translate("DbManagerDlgSqlLayerWindow", "Column(s) with\n"
"unique values", None))
        self.hasGeometryCol.setText(_translate("DbManagerDlgSqlLayerWindow", "Geometry column", None))
        self.getColumnsBtn.setText(_translate("DbManagerDlgSqlLayerWindow", "Retrieve\n"
"columns", None))
        self.label_5.setText(_translate("DbManagerDlgSqlLayerWindow", "Layer name (prefix)", None))
        self.label_6.setText(_translate("DbManagerDlgSqlLayerWindow", "Type", None))
        self.vectorRadio.setText(_translate("DbManagerDlgSqlLayerWindow", "Vector", None))
        self.rasterRadio.setText(_translate("DbManagerDlgSqlLayerWindow", "Raster", None))
        self.btnSetFilter.setText(_translate("DbManagerDlgSqlLayerWindow", "Set filter", None))

from qgis.gui import QgsCodeEditorSQL
