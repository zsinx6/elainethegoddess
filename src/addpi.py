# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addpi.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(348, 319)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.qlinenome = QtWidgets.QLineEdit(Form)
        self.qlinenome.setInputMask("")
        self.qlinenome.setText("")
        self.qlinenome.setMaxLength(70)
        self.qlinenome.setFrame(True)
        self.qlinenome.setPlaceholderText("")
        self.qlinenome.setObjectName("qlinenome")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.qlinenome)
        self.qlineemail = QtWidgets.QLineEdit(Form)
        self.qlineemail.setMaximumSize(QtCore.QSize(150, 500))
        self.qlineemail.setMaxLength(80)
        self.qlineemail.setObjectName("qlineemail")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.qlineemail)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_9)
        self.qlinecpf = QtWidgets.QLineEdit(Form)
        self.qlinecpf.setText("")
        self.qlinecpf.setMaxLength(11)
        self.qlinecpf.setPlaceholderText("")
        self.qlinecpf.setObjectName("qlinecpf")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.qlinecpf)
        self.qlinepass = QtWidgets.QLineEdit(Form)
        self.qlinepass.setMaximumSize(QtCore.QSize(150, 16777215))
        self.qlinepass.setObjectName("qlinepass")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.qlinepass)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.qcomboboxcred = QtWidgets.QComboBox(Form)
        self.qcomboboxcred.setObjectName("qcomboboxcred")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.qcomboboxcred)
        self.qcomboboxoi = QtWidgets.QComboBox(Form)
        self.qcomboboxoi.setMaximumSize(QtCore.QSize(150, 16777215))
        self.qcomboboxoi.setObjectName("qcomboboxoi")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.qcomboboxoi)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_7)
        self.qdate = QtWidgets.QDateEdit(Form)
        self.qdate.setDate(QtCore.QDate(2016, 6, 17))
        self.qdate.setObjectName("qdate")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.qdate)
        self.qlinenacio = QtWidgets.QLineEdit(Form)
        self.qlinenacio.setMaximumSize(QtCore.QSize(150, 16777215))
        self.qlinenacio.setMaxLength(20)
        self.qlinenacio.setObjectName("qlinenacio")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.qlinenacio)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.qlinefunc = QtWidgets.QLineEdit(Form)
        self.qlinefunc.setMaxLength(30)
        self.qlinefunc.setObjectName("qlinefunc")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.qlinefunc)
        self.addbutton = QtWidgets.QPushButton(Form)
        self.addbutton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.addbutton.setObjectName("addbutton")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.addbutton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(10, QtWidgets.QFormLayout.FieldRole, spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Adicionar Profissional de Imprensa"))
        self.label.setText(_translate("Form", "Nome"))
        self.label_5.setText(_translate("Form", "Email"))
        self.qlinenome.setToolTip(_translate("Form", "Nome"))
        self.label_2.setText(_translate("Form", "CPF"))
        self.label_9.setText(_translate("Form", "Passaporte"))
        self.qlinecpf.setInputMask(_translate("Form", "00000000000"))
        self.qlinepass.setInputMask(_translate("Form", "00000000"))
        self.label_3.setText(_translate("Form", "Credêncial"))
        self.label_4.setText(_translate("Form", "Orgão de Imprensa"))
        self.label_6.setText(_translate("Form", "Data Nascimento"))
        self.label_7.setText(_translate("Form", "Nacionalidade"))
        self.label_8.setText(_translate("Form", "Função"))
        self.addbutton.setText(_translate("Form", "Adicionar"))

