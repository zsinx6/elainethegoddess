#! python
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

from buscaoi1 import Ui_Form
from bdconn import insert, showdialog, executa_select, executa_cmd
import buscaoi2_tela


class busca_oi1(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(busca_oi1, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connect_signals()


    def connect_signals(self):
        self.ui.qsbutton.clicked.connect(self.addbutton_click)
        self.ui.qtable.doubleClicked.connect(self.item_click)

    def item_click(self):
        row = self.ui.qtable.currentRow()
        item = self.ui.qtable.item(row, 0)
        id_oi = item.text()
        try:
            self.dw.hide()
        except(Exception):
            pass
        self.dw = QtWidgets.QDockWidget(self.parent())
        self.dw.setMinimumWidth(400)
        self.dw.setFeatures(QtWidgets.QDockWidget.DockWidgetClosable)
        self.widget = buscaoi2_tela.busca_oi2(id_oi, self.dw.widget())
        self.dw.setWidget(self.widget)
        self.parent().parent().addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dw)

    def addbutton_click(self):
        """ manipulador do evento click do mouse para adicionar comite
            utiliza a funcao insert (definida no arquivo bdconn.py) passando
            como argumento kwargs
        """
        nome = self.ui.qlinenome.text()
        cmd = "SELECT id, comite, nome FROM orgao_imprensa "
        if nome:
            cmd += "WHERE UPPER(nome) LIKE '%" + nome.upper() + "%'"
        else:
            cmd += ";"
        query = executa_select(cmd)
        if not query:
            showdialog('Alerta', 'Nenhuma informação encontrada')
        self.fill_table(query)

    def fill_table(self, lista):
        """ recebe lista e adiciona na interface
        """
        while self.ui.qtable.rowCount():
            self.ui.qtable.removeRow(0)
        row = 0
        for id_oi, comite, nome in lista:
            self.ui.qtable.insertRow(row)
            item_id = QtWidgets.QTableWidgetItem(str(id_oi))
            item_comite = QtWidgets.QTableWidgetItem(comite)
            item_nome = QtWidgets.QTableWidgetItem(nome)
            flags = QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            item_id.setFlags(flags)
            item_comite.setFlags(flags)
            item_nome.setFlags(flags)
            self.ui.qtable.setItem(row, 0, item_id)
            self.ui.qtable.setItem(row, 1, item_comite)
            self.ui.qtable.setItem(row, 2, item_nome)
            row += 1


def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = busca_oi1()
    mw.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
