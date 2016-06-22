# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editlimitescomite.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 207)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.qcomboboxcomite = QtWidgets.QComboBox(Form)
        self.qcomboboxcomite.setObjectName("qcomboboxcomite")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.qcomboboxcomite)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.qcomboboxtipocred = QtWidgets.QComboBox(Form)
        self.qcomboboxtipocred.setObjectName("qcomboboxtipocred")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.qcomboboxtipocred)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.qspinboxqtd = QtWidgets.QSpinBox(Form)
        self.qspinboxqtd.setObjectName("qspinboxqtd")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.qspinboxqtd)
        self.updatebutton = QtWidgets.QPushButton(Form)
        self.updatebutton.setObjectName("updatebutton")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.updatebutton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Editar Quantidades de Credenciais do Comite"))
        self.label.setText(_translate("Form", "Comite"))
        self.label_2.setText(_translate("Form", "Tipo Credencial"))
        self.label_3.setText(_translate("Form", "Quantidade"))
        self.updatebutton.setText(_translate("Form", "Atualizar"))

