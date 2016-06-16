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
        Form.resize(438, 231)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(50)
        self.lineEdit.setFrame(True)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setMaxLength(14)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(286, 55, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Adicionar Profissional de Imprensa"))
        self.label.setText(_translate("Form", "Nome"))
        self.lineEdit.setToolTip(_translate("Form", "Nome"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Nome"))
        self.label_2.setText(_translate("Form", "CPF"))
        self.lineEdit_2.setInputMask(_translate("Form", "000.000.000-00"))
        self.lineEdit_2.setText(_translate("Form", "..-"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "CPF"))
        self.label_3.setText(_translate("Form", "Credêncial"))
        self.pushButton.setText(_translate("Form", "Adicionar"))

