#! python
# -*- coding: utf-8 -*-
"""Edit limites comite

"""

import sys
from PyQt5 import QtWidgets

from editlimitescomite import Ui_Form
from bdconn import showdialog, select, executa_select, executa_cmd


class edit_limitescomite(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(edit_limitescomite, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connect_signals()
        self.ui.qspinboxqtd.setMaximum(9999999)

        #seleciona todos os comites
        comites = select('comite', ['nome'])

        """verificacao
        """
        if not comites:
            showdialog('Alerta', 'Nenhum Comitê cadastrado')
        tipos = select('tipo_credencial', ['sigla'])
        if not tipos:
            showdialog('Alerta', 'Nenhum Tipo de Credencial cadastrado')
        if not tipos or not comites:
            return

        cmd = "SELECT quantidade FROM limites_comite WHERE comite = '" + comites[0][0] + """' AND
        tipo_credencial = '""" + tipos[0][0] + "';"
        qtd = executa_select(cmd)[0][0]
        self.ui.qspinboxqtd.setValue(qtd)
        self.eval_comcoboxtipo(tipos)
        self.eval_comcoboxcomite(comites)

    def eval_comcoboxcomite(self, lista):
        for item in lista:
            self.ui.qcomboboxcomite.addItem(str(item[0]))

    def eval_comcoboxtipo(self, lista):
        for item in lista:
            self.ui.qcomboboxtipocred.addItem(str(item[0]))

    def connect_signals(self):
        self.ui.updatebutton.clicked.connect(self.updatebutton_click)
        self.ui.qcomboboxcomite.currentIndexChanged.connect(self.changes)
        self.ui.qcomboboxtipocred.currentIndexChanged.connect(self.changes)

    def updatebutton_click(self):
        """trata o evento do click, aqui  no caso edita os limites do tipo de credencial selecionado para um certo OI
        """
        comite = self.ui.qcomboboxcomite.currentText()
        tipo = self.ui.qcomboboxtipocred.currentText()
        qtd = self.ui.qspinboxqtd.value()
        cmd = "UPDATE limites_comite SET quantidade = " + str(qtd)
        cmd += " WHERE comite = '" + comite + "' "
        cmd += "AND tipo_credencial ='" + tipo + "';"
        executa_cmd(cmd)

    def changes(self):
        """seleciona as quantidades disponiveis de um comite, relacionadas a um tipo de credencial
        """
        comite = self.ui.qcomboboxcomite.currentText()
        tipo = self.ui.qcomboboxtipocred.currentText()
        cmd = "SELECT quantidade FROM limites_comite WHERE comite = '" + comite + """' AND
        tipo_credencial = '""" + tipo + "'"
        try:
            qtd = executa_select(cmd)[0][0]
            self.ui.qspinboxqtd.setValue(qtd)
        except(Exception):
            pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = edit_limitescomite()
    mw.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
