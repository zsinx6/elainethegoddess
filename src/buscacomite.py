# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buscacomite.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 373)
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
        self.qlinepais = QtWidgets.QLineEdit(Form)
        self.qlinepais.setMaxLength(30)
        self.qlinepais.setObjectName("qlinepais")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.qlinepais)
        self.qsbutton = QtWidgets.QPushButton(Form)
        self.qsbutton.setObjectName("qsbutton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.qsbutton)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.qtable = QtWidgets.QTableWidget(Form)
        self.qtable.setObjectName("qtable")
        self.qtable.setColumnCount(5)
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
        self.qtable.horizontalHeader().setDefaultSectionSize(120)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.qtable)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Busca Comitê"))
        self.label.setText(_translate("Form", "Nome"))
        self.label_2.setText(_translate("Form", "País"))
        self.qsbutton.setText(_translate("Form", "Buscar"))
        self.label_3.setText(_translate("Form", "Comitês"))
        item = self.qtable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "País"))
        item = self.qtable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nome"))
        item = self.qtable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Presidente"))
        item = self.qtable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Email de Contato"))
        item = self.qtable.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Endereço"))

