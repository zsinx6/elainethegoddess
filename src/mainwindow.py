# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(415, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 415, 19))
        self.menubar.setObjectName("menubar")
        self.menuAdicionar = QtWidgets.QMenu(self.menubar)
        self.menuAdicionar.setObjectName("menuAdicionar")
        self.menuBuscar = QtWidgets.QMenu(self.menubar)
        self.menuBuscar.setObjectName("menuBuscar")
        self.menuAlterar = QtWidgets.QMenu(self.menubar)
        self.menuAlterar.setObjectName("menuAlterar")
        MainWindow.setMenuBar(self.menubar)
        self.actionProfissional_de_Imprensa = QtWidgets.QAction(MainWindow)
        self.actionProfissional_de_Imprensa.setObjectName("actionProfissional_de_Imprensa")
        self.actionTipo_Credencial = QtWidgets.QAction(MainWindow)
        self.actionTipo_Credencial.setObjectName("actionTipo_Credencial")
        self.actionComite = QtWidgets.QAction(MainWindow)
        self.actionComite.setObjectName("actionComite")
        self.actionOrg_o_de_Imprensa = QtWidgets.QAction(MainWindow)
        self.actionOrg_o_de_Imprensa.setObjectName("actionOrg_o_de_Imprensa")
        self.actionCredencial = QtWidgets.QAction(MainWindow)
        self.actionCredencial.setObjectName("actionCredencial")
        self.actionLimites_Comite = QtWidgets.QAction(MainWindow)
        self.actionLimites_Comite.setObjectName("actionLimites_Comite")
        self.actionLimites_Org_o_de_Imprensa = QtWidgets.QAction(MainWindow)
        self.actionLimites_Org_o_de_Imprensa.setObjectName("actionLimites_Org_o_de_Imprensa")
        self.actionOrg_os_de_Imprensa = QtWidgets.QAction(MainWindow)
        self.actionOrg_os_de_Imprensa.setObjectName("actionOrg_os_de_Imprensa")
        self.actionProfissionais_de_Imprensa = QtWidgets.QAction(MainWindow)
        self.actionProfissionais_de_Imprensa.setObjectName("actionProfissionais_de_Imprensa")
        self.actionComit = QtWidgets.QAction(MainWindow)
        self.actionComit.setObjectName("actionComit")
        self.menuAdicionar.addAction(self.actionProfissional_de_Imprensa)
        self.menuAdicionar.addAction(self.actionTipo_Credencial)
        self.menuAdicionar.addAction(self.actionComite)
        self.menuAdicionar.addAction(self.actionOrg_o_de_Imprensa)
        self.menuBuscar.addAction(self.actionOrg_os_de_Imprensa)
        self.menuBuscar.addAction(self.actionProfissionais_de_Imprensa)
        self.menuBuscar.addAction(self.actionComit)
        self.menuAlterar.addAction(self.actionLimites_Comite)
        self.menuAlterar.addAction(self.actionLimites_Org_o_de_Imprensa)
        self.menubar.addAction(self.menuAdicionar.menuAction())
        self.menubar.addAction(self.menuAlterar.menuAction())
        self.menubar.addAction(self.menuBuscar.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Janela Principal"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menuAdicionar.setTitle(_translate("MainWindow", "Adicionar"))
        self.menuBuscar.setTitle(_translate("MainWindow", "Buscar"))
        self.menuAlterar.setTitle(_translate("MainWindow", "Alterar"))
        self.actionProfissional_de_Imprensa.setText(_translate("MainWindow", "Profissional de Imprensa"))
        self.actionTipo_Credencial.setText(_translate("MainWindow", "Tipo de Credencial"))
        self.actionComite.setText(_translate("MainWindow", "Comite"))
        self.actionOrg_o_de_Imprensa.setText(_translate("MainWindow", "Orgão de Imprensa"))
        self.actionCredencial.setText(_translate("MainWindow", "Credencial"))
        self.actionLimites_Comite.setText(_translate("MainWindow", "Limites Comitê"))
        self.actionLimites_Org_o_de_Imprensa.setText(_translate("MainWindow", "Limites Orgão de Imprensa"))
        self.actionOrg_os_de_Imprensa.setText(_translate("MainWindow", "Orgãos de Imprensa"))
        self.actionProfissionais_de_Imprensa.setText(_translate("MainWindow", "Profissionais de Imprensa"))
        self.actionComit.setText(_translate("MainWindow", "Comitê"))

