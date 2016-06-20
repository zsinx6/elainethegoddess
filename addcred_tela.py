#! python
# -*- coding: utf-8 -*-
"""Add Credencial
"""

import sys
from PyQt5 import QtWidgets

from addcred import Ui_Form
from bdconn import insert, select, executa_select, showdialog


class add_credencial(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(add_credencial, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        #busca do banco de dados os ids de todos orgaos de imprensa
        oi = select('orgao_imprensa', ['nome'])
        self.eval_comboboxoi(oi)

        #seleciona a sigla de todos os tipos de credencial
        tipo = select('tipo_credencial', ['sigla'])
        self.eval_comboboxtipo(tipo)
        self.connect_signals()

    def eval_comboboxoi(self, lista):
        """adiciona o retorno do select no combobox
        """
        for item in lista:
            self.ui.qcombooi.addItem(str(item[0]))

    def eval_comboboxtipo(self, lista):
        """adiciona o retorno do select no combobox
        """
        for item in lista:
            self.ui.qcombotipo.addItem(str(item[0]))

    def connect_signals(self):
        self.ui.addbutton.clicked.connect(self.addbutton_click)

    def addbutton_click(self):
        """adiciona crendencial
        """
        tipo = self.ui.qcombotipo.currentText()
        oi = self.ui.qcombooi.currentText()
        cmd = "SELECT id FROM orgao_imprensa "
        cmd += "WHERE nome = '" + oi + "';"
        if oi:
            oi = executa_select(cmd)[0][0]
            kwargs = {'tipo': "'" + tipo + "'",
                      'orgao_imprensa': str(oi)}
            if(insert('credencial', kwargs)):
                self.parent().hide()
                self.parent().parent().setWindowTitle(self.parent().parent().title)
        else:
            showdialog('Erro', 'Nenhum OI registrado')


def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = add_credencial()
    mw.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
