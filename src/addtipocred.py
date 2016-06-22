# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addtipocred.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 229)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.qlinesigla = QtWidgets.QLineEdit(Form)
        self.qlinesigla.setMaxLength(4)
        self.qlinesigla.setObjectName("qlinesigla")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.qlinesigla)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.qlinefunc = QtWidgets.QLineEdit(Form)
        self.qlinefunc.setMaxLength(30)
        self.qlinefunc.setObjectName("qlinefunc")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.qlinefunc)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.qcombotrans = QtWidgets.QComboBox(Form)
        self.qcombotrans.setEditable(False)
        self.qcombotrans.setObjectName("qcombotrans")
        self.qcombotrans.addItem("")
        self.qcombotrans.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.qcombotrans)
        spacerItem = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.addbutton = QtWidgets.QPushButton(Form)
        self.addbutton.setObjectName("addbutton")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.addbutton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Adicionar Tipo Credencial"))
        self.label.setText(_translate("Form", "Sigla"))
        self.label_2.setText(_translate("Form", "Função"))
        self.label_3.setText(_translate("Form", "Direito de Transmissão"))
        self.qcombotrans.setItemText(0, _translate("Form", "Sim"))
        self.qcombotrans.setItemText(1, _translate("Form", "Não"))
        self.addbutton.setText(_translate("Form", "Adicionar"))

