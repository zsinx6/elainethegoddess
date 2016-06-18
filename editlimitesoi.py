# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editlimitesoi.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.qcomboboxoi = QtWidgets.QComboBox(Form)
        self.qcomboboxoi.setObjectName("qcomboboxoi")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.qcomboboxoi)
        self.qspinboxqtd = QtWidgets.QSpinBox(Form)
        self.qspinboxqtd.setMaximum(999999999)
        self.qspinboxqtd.setObjectName("qspinboxqtd")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.qspinboxqtd)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.qcomboboxtipocred = QtWidgets.QComboBox(Form)
        self.qcomboboxtipocred.setObjectName("qcomboboxtipocred")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.qcomboboxtipocred)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label)
        self.updatebutton = QtWidgets.QPushButton(Form)
        self.updatebutton.setObjectName("updatebutton")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.updatebutton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.FieldRole, spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Editar Quantidades Credencias do OI"))
        self.label_2.setText(_translate("Form", "Orgão de Imprensa"))
        self.label_3.setText(_translate("Form", "Quantidade"))
        self.label.setText(_translate("Form", "Tipo Credencial"))
        self.updatebutton.setText(_translate("Form", "Atualizar"))

