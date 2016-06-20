#! python
# -*- coding: utf-8 -*-
"""Add Comite
"""

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

from buscacomite import Ui_Form
from bdconn import insert, showdialog, executa_select, executa_cmd


class busca_comite(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(busca_comite, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connect_signals()

    def connect_signals(self):
        self.ui.qsbutton.clicked.connect(self.addbutton_click)

    def addbutton_click(self):
        """ manipulador do evento click do mouse para adicionar comite
            utiliza a funcao insert (definida no arquivo bdconn.py) passando
            como argumento kwargs
        """
        nome = self.ui.qlinenome.text()
        pais = self.ui.qlinepais.text()
        cmd = "SELECT * FROM comite "
        if nome and pais:
            cmd += "WHERE UPPER(nome) LIKE '%" + nome.upper() + "%' "
            cmd += "AND UPPER(pais) LIKE '%" + pais.upper() + "%';"
        elif nome:
            cmd += "WHERE UPPER(nome) LIKE '%" + nome.upper() + "%';"
        elif pais:
            cmd += "WHERE UPPER(pais) LIKE '%" + pais.upper() + "%';"
        else:
            cmd += ";"
        query = executa_select(cmd)
        if not query:
            showdialog("Alerta",
                       "Nenhuma informação encontrada")
        else:
            self.fill_table(query)

    def fill_table(self, lista):
        while self.ui.qtable.rowCount():
            self.ui.qtable.removeRow(0)
        row = 0
        for line in lista:
            self.ui.qtable.insertRow(row)
            col = 0
            for item in line:
                qtable_item = QtWidgets.QTableWidgetItem(str(item))
                flags = QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                qtable_item.setFlags(flags)
                self.ui.qtable.setItem(row, col, qtable_item)
                col += 1
            row += 1


def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = busca_comite()
    mw.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
