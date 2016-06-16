# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addoi.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 314)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.qlinenome = QtWidgets.QLineEdit(Form)
        self.qlinenome.setMaxLength(50)
        self.qlinenome.setObjectName("qlinenome")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.qlinenome)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.qcombocomite = QtWidgets.QComboBox(Form)
        self.qcombocomite.setObjectName("qcombocomite")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.qcombocomite)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.qlineend = QtWidgets.QLineEdit(Form)
        self.qlineend.setMaxLength(100)
        self.qlineend.setObjectName("qlineend")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.qlineend)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.qlinenomerepr = QtWidgets.QLineEdit(Form)
        self.qlinenomerepr.setMaxLength(70)
        self.qlinenomerepr.setObjectName("qlinenomerepr")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.qlinenomerepr)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.qlineemailrepr = QtWidgets.QLineEdit(Form)
        self.qlineemailrepr.setMaxLength(80)
        self.qlineemailrepr.setObjectName("qlineemailrepr")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.qlineemailrepr)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(10, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.addbutton = QtWidgets.QPushButton(Form)
        self.addbutton.setObjectName("addbutton")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.addbutton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.qlinenome, self.qcombocomite)
        Form.setTabOrder(self.qcombocomite, self.qlineend)
        Form.setTabOrder(self.qlineend, self.qlinenomerepr)
        Form.setTabOrder(self.qlinenomerepr, self.qlineemailrepr)
        Form.setTabOrder(self.qlineemailrepr, self.addbutton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Adicionar Orgão de Imprensa"))
        self.label.setText(_translate("Form", "Nome"))
        self.label_2.setText(_translate("Form", "Comite"))
        self.label_3.setText(_translate("Form", "Endereço"))
        self.label_4.setText(_translate("Form", "Nome Representante"))
        self.label_5.setText(_translate("Form", "E-mail Representante"))
        self.addbutton.setText(_translate("Form", "Adicionar"))

