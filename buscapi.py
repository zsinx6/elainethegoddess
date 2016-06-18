# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buscapi.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(617, 300)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.qlinenome = QtWidgets.QLineEdit(Form)
        self.qlinenome.setMaxLength(70)
        self.qlinenome.setObjectName("qlinenome")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.qlinenome)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.qsbutton = QtWidgets.QPushButton(Form)
        self.qsbutton.setObjectName("qsbutton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.qsbutton)
        self.qtable = QtWidgets.QTableWidget(Form)
        self.qtable.setObjectName("qtable")
        self.qtable.setColumnCount(10)
        self.qtable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.qtable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.qtable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.qtable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.qtable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.qtable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.qtable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.qtable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.qtable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.qtable.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.qtable.setHorizontalHeaderItem(9, item)
        self.qtable.horizontalHeader().setDefaultSectionSize(150)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.qtable)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Buscar Profissional de Imprensa"))
        self.label.setText(_translate("Form", "Nome"))
        self.qsbutton.setText(_translate("Form", "Buscar"))
        item = self.qtable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Nome"))
        item = self.qtable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Função"))
        item = self.qtable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Orgão de Imprensa"))
        item = self.qtable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Credencial"))
        item = self.qtable.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Tipo Credencial"))
        item = self.qtable.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Email"))
        item = self.qtable.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Data Nascimento"))
        item = self.qtable.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Nacionalidade"))
        item = self.qtable.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Passaporte"))
        item = self.qtable.horizontalHeaderItem(9)
        item.setText(_translate("Form", "CPF"))

