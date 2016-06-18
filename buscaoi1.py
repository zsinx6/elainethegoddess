# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buscaoi1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 313)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.qlinenome = QtWidgets.QLineEdit(Form)
        self.qlinenome.setMaxLength(50)
        self.qlinenome.setObjectName("qlinenome")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.qlinenome)
        self.qsbutton = QtWidgets.QPushButton(Form)
        self.qsbutton.setObjectName("qsbutton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.qsbutton)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.qtable = QtWidgets.QTableWidget(Form)
        self.qtable.setObjectName("qtable")
        self.qtable.setColumnCount(3)
        self.qtable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.qtable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.qtable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.qtable.setHorizontalHeaderItem(2, item)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.qtable)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Buscar Orgão de Imprensa"))
        self.label.setText(_translate("Form", "Nome do Orgão de Imprensa"))
        self.qsbutton.setText(_translate("Form", "Buscar"))
        self.label_2.setText(_translate("Form", "Orgãos de Imprensa"))
        item = self.qtable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.qtable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Comite"))
        item = self.qtable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Nome"))

