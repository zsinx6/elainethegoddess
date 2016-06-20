# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buscacomite2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(426, 439)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.qtablelimites = QtWidgets.QTableWidget(Form)
        self.qtablelimites.setObjectName("qtablelimites")
        self.qtablelimites.setColumnCount(2)
        self.qtablelimites.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.qtablelimites.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.qtablelimites.setHorizontalHeaderItem(1, item)
        self.qtablelimites.horizontalHeader().setDefaultSectionSize(120)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.qtablelimites)
        self.qtableoi = QtWidgets.QTableWidget(Form)
        self.qtableoi.setObjectName("qtableoi")
        self.qtableoi.setColumnCount(5)
        self.qtableoi.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.qtableoi.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.qtableoi.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.qtableoi.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.qtableoi.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.qtableoi.setHorizontalHeaderItem(4, item)
        self.qtableoi.horizontalHeader().setDefaultSectionSize(150)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.qtableoi)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Exibir informações do comitê"))
        self.label_4.setText(_translate("Form", "Limites"))
        self.label.setText(_translate("Form", "Orgãos de Imprensa"))
        item = self.qtablelimites.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Tipo de Credencial"))
        item = self.qtablelimites.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Quantidade"))
        item = self.qtableoi.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Nome"))
        item = self.qtableoi.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Id"))
        item = self.qtableoi.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Nome do Representante"))
        item = self.qtableoi.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Email do Representante"))
        item = self.qtableoi.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Endereço"))

