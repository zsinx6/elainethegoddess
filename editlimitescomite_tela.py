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
        comites = select('comite', ['nome'])
        tipos = select('tipo_credencial', ['sigla'])
        cmd = "SELECT quantidade from limites_comite where comite = '" + comites[0][0] + """' AND
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
        comite = self.ui.qcomboboxcomite.currentText()
        tipo = self.ui.qcomboboxtipocred.currentText()
        qtd = self.ui.qspinboxqtd.value()
        cmd = "UPDATE limites_comite set quantidade = " + str(qtd)
        cmd += " where comite = '" + comite + "' "
        cmd += "AND tipo_credencial ='" + tipo + "';"
        executa_cmd(cmd)

    def changes(self):
        comite = self.ui.qcomboboxcomite.currentText()
        tipo = self.ui.qcomboboxtipocred.currentText()
        cmd = "SELECT quantidade from limites_comite where comite = '" + comite + """' AND
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