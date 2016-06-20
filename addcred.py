# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addcred.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(394, 190)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.qcombotipo = QtWidgets.QComboBox(Form)
        self.qcombotipo.setObjectName("qcombotipo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.qcombotipo)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.qcombooi = QtWidgets.QComboBox(Form)
        self.qcombooi.setObjectName("qcombooi")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.qcombooi)
        self.addbutton = QtWidgets.QPushButton(Form)
        self.addbutton.setObjectName("addbutton")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.addbutton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Adicionar Credencial "))
        self.label.setText(_translate("Form", "Tipo"))
        self.label_2.setText(_translate("Form", "Orgão de Imprensa"))
        self.addbutton.setText(_translate("Form", "Adicionar"))

