#! python
# -*- coding: utf-8 -*-
"""Main Window.
"""

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

from mainwindow import Ui_MainWindow
import addpi_tela
import addtipocred_tela
import addcomite_tela
import addoi_tela
import addcred_tela
import editlimitescomite_tela
import editlimitesoi_tela


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_signals()
        self.cont = 0

    def connect_signals(self):
        self.ui.actionProfissional_de_Imprensa.\
                triggered.connect(lambda: self.add_widget('pi'))
        self.ui.actionTipo_Credencial.triggered.\
                connect(lambda: self.add_widget('tipocred'))
        self.ui.actionComite.triggered.\
                connect(lambda: self.add_widget('comite'))
        self.ui.actionOrg_o_de_Imprensa.triggered.\
                connect(lambda: self.add_widget('oi'))
        self.ui.actionCredencial.triggered.\
                connect(lambda: self.add_widget('cred'))
        self.ui.actionLimites_Comite.triggered.\
                connect(lambda: self.add_widget('limitescomite'))
        self.ui.actionLimites_Org_o_de_Imprensa.triggered.\
                connect(lambda: self.add_widget('limitesoi'))

    def add_widget(self, tipo):
        try:
            self.dw.hide()
        except(Exception):
            pass
        self.dw = QtWidgets.QDockWidget(self)
        self.dw.setMinimumWidth(400)
        self.dw.setFeatures(QtWidgets.QDockWidget.DockWidgetClosable)

        if(tipo == 'pi'):
            self.widget = addpi_tela.add_pi(self.dw.widget())
        elif(tipo == 'tipocred'):
            self.widget = addtipocred_tela.add_tipocred(self.dw.widget())
        elif(tipo == 'comite'):
            self.widget = addcomite_tela.add_comite(self.dw.widget())
        elif(tipo == 'oi'):
            self.widget = addoi_tela.add_oi(self.dw.widget())
        elif(tipo == 'cred'):
            self.widget = addcred_tela.add_credencial(self.dw.widget())
        elif(tipo == 'limitescomite'):
            self.widget = editlimitescomite_tela.edit_limitescomite(self.dw.widget())
        elif(tipo == 'limitesoi'):
            self.widget = editlimitesoi_tela.edit_limitesoi(self.dw.widget())
        self.dw.setWidget(self.widget)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dw)

    def change_text(self):
        self.cont += 1


def main():
    app = QtWidgets.QApplication(sys.argv)
    mw_editor = MainWindow()
    mw_editor.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
