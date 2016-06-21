#! python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

from buscaoi2 import Ui_Form
from bdconn import insert, showdialog, executa_select, executa_cmd

"""Busca todos os profisionais de Imprensa relacionados ao OI em questao, busca tbm sua credencial
    Busca os limites para cada tipo de credencial relacionada ao OI em questao
"""

class busca_oi2(QtWidgets.QWidget):
    def __init__(self, id_oi, parent=None):
        super(busca_oi2, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connect_signals()
        cmd = "SELECT credencial, nome FROM profissional_imprensa "
        cmd += "WHERE orgao_imprensa = " + id_oi + ";"
        pis = executa_select(cmd)
        cmd = "SELECT tipo_credencial, quantidade FROM limites_oi "
        cmd += "WHERE orgao_imprensa = " + id_oi + ";"
        limites = executa_select(cmd)

        self.fill_table(pis, self.ui.qpi)
        self.fill_table(limites, self.ui.qlimites)

    def connect_signals(self):
        pass

    def item_click(self):
        pass

    def fill_table(self, lista, table):
        while table.rowCount():
            table.removeRow(0)
        row = 0
        for item0, item1 in lista:
            table.insertRow(row)
            item_0 = QtWidgets.QTableWidgetItem(str(item0))
            item_1 = QtWidgets.QTableWidgetItem(str(item1))
            flags = QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            item_0.setFlags(flags)
            item_1.setFlags(flags)
            table.setItem(row, 0, item_0)
            table.setItem(row, 1, item_1)
            row += 1


def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = busca_oi2()
    mw.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
