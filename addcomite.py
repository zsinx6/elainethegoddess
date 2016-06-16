# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addcomite.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(404, 300)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.qlinepais = QtWidgets.QLineEdit(Form)
        self.qlinepais.setMaxLength(30)
        self.qlinepais.setObjectName("qlinepais")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.qlinepais)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.qlinenome = QtWidgets.QLineEdit(Form)
        self.qlinenome.setMaxLength(50)
        self.qlinenome.setObjectName("qlinenome")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.qlinenome)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.qlinepres = QtWidgets.QLineEdit(Form)
        self.qlinepres.setMaxLength(70)
        self.qlinepres.setObjectName("qlinepres")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.qlinepres)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.qlineemail = QtWidgets.QLineEdit(Form)
        self.qlineemail.setMaxLength(80)
        self.qlineemail.setObjectName("qlineemail")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.qlineemail)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.addbutton = QtWidgets.QPushButton(Form)
        self.addbutton.setObjectName("addbutton")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.addbutton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.qlineend = QtWidgets.QLineEdit(Form)
        self.qlineend.setMaxLength(80)
        self.qlineend.setObjectName("qlineend")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.qlineend)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.qlinepais, self.qlinenome)
        Form.setTabOrder(self.qlinenome, self.qlinepres)
        Form.setTabOrder(self.qlinepres, self.qlineemail)
        Form.setTabOrder(self.qlineemail, self.qlineend)
        Form.setTabOrder(self.qlineend, self.addbutton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Adicionar Comite"))
        self.label.setText(_translate("Form", "País"))
        self.label_2.setText(_translate("Form", "Nome"))
        self.label_3.setText(_translate("Form", "Presidente"))
        self.label_4.setText(_translate("Form", "E-mail"))
        self.label_5.setText(_translate("Form", "Endereço"))
        self.addbutton.setText(_translate("Form", "Adicionar"))

