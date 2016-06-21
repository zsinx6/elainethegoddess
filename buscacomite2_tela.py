#! python
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

from buscacomite2 import Ui_Form
from bdconn import insert, showdialog, executa_select, executa_cmd


class busca_comite2(QtWidgets.QWidget):
    def __init__(self, nome_comite, parent=None):
        super(busca_comite2, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        """seleciona (tipo_credencial, qtd) pra o comite especificado
        """
        cmd = "SELECT quantidade, tipo_credencial FROM comite "
        cmd += "join limites_comite on nome = comite "
        cmd += "WHERE comite = '" + nome_comite + "';"
        limites = executa_select(cmd)

        """seleciona os OI's que detem essas credenciais do comite especificado
        """
        cmd = "SELECT O.nome, O.id, O.nome_representante, O.email_representante, O.endereco "
        cmd += "FROM orgao_imprensa O JOIN comite C ON C.nome = O.comite "
        cmd += "WHERE O.comite = '" + nome_comite + "';"
        ois = executa_select(cmd)
        self.fill_table(limites, self.ui.qtablelimites)
        self.fill_table(ois, self.ui.qtableoi)

    """ preenche a tabela exibida na tela
    """
    def fill_table(self, lista, table):
        while table.rowCount():
            table.removeRow(0)
        row = 0
        for line in lista:
            table.insertRow(row)
            col = 0
            for item in line:
                qtable_item = QtWidgets.QTableWidgetItem(str(item))
                flags = QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                qtable_item.setFlags(flags)
                table.setItem(row, col, qtable_item)
                col += 1
            row += 1


def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = busca_comite2()
    mw.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
