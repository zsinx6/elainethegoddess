# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buscaoi2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(321, 468)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.qlimites = QtWidgets.QTableWidget(Form)
        self.qlimites.setMinimumSize(QtCore.QSize(300, 200))
        self.qlimites.setObjectName("qlimites")
        self.qlimites.setColumnCount(2)
        self.qlimites.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.qlimites.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.qlimites.setHorizontalHeaderItem(1, item)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.qlimites)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.qpi = QtWidgets.QTableWidget(Form)
        self.qpi.setMinimumSize(QtCore.QSize(300, 200))
        self.qpi.setObjectName("qpi")
        self.qpi.setColumnCount(2)
        self.qpi.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.qpi.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.qpi.setHorizontalHeaderItem(1, item)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.qpi)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Exibir informações do Orgão de Imprensa"))
        self.label.setText(_translate("Form", "Limites"))
        item = self.qlimites.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Tipo"))
        item = self.qlimites.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Quantidade"))
        self.label_2.setText(_translate("Form", "Profissionais de Imprensa"))
        item = self.qpi.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Credencial"))
        item = self.qpi.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nome"))

