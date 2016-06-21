#! python
# -*- coding: utf-8 -*-
"""Edit limites comite
"""

import sys
from PyQt5 import QtWidgets

from editlimitesoi import Ui_Form
from bdconn import showdialog, select, executa_select, executa_cmd


class edit_limitesoi(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(edit_limitesoi, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connect_signals()
        self.ui.qspinboxqtd.setMaximum(9999999)
        oi = select('orgao_imprensa', ['nome'])
        if not oi:
            showdialog('Alerta', 'Nenhum OI cadastrado')
        tipos = select('tipo_credencial', ['sigla'])
        if not tipos:
            showdialog('Alerta', 'Nenhum Tipo de Credencial cadastrada')
        if not tipos or not oi:
            return
        cmd = "SELECT quantidade from limites_oi JOIN orgao_imprensa "
        cmd += "ON orgao_imprensa = id WHERE nome = '" + oi[0][0] + "' "
        cmd += "AND tipo_credencial = '" + tipos[0][0] + "';"
        qtd = executa_select(cmd)[0][0]
        if qtd:
            self.oldqtd = qtd
        else:
            self.oldqtd = 0
        self.ui.qspinboxqtd.setValue(qtd)
        self.eval_comcoboxtipo(tipos)
        self.eval_comcoboxoi(oi)

    def eval_comcoboxoi(self, lista):
        for item in lista:
            self.ui.qcomboboxoi.addItem(str(item[0]))

    def eval_comcoboxtipo(self, lista):
        for item in lista:
            self.ui.qcomboboxtipocred.addItem(str(item[0]))

    def connect_signals(self):
        self.ui.updatebutton.clicked.connect(self.updatebutton_click)
        self.ui.qcomboboxoi.currentIndexChanged.connect(self.changes)
        self.ui.qcomboboxtipocred.currentIndexChanged.connect(self.changes)

    def updatebutton_click(self):
        oi = self.ui.qcomboboxoi.currentText()
        tipo = self.ui.qcomboboxtipocred.currentText()
        qtd = self.ui.qspinboxqtd.value()
        cmd = "UPDATE limites_oi SET quantidade = " + str(qtd) + " "
        cmd += "WHERE tipo_credencial = '" + tipo + "' "
        cmd += "AND orgao_imprensa IN (SELECT id FROM orgao_imprensa "
        cmd += "WHERE nome = '" + oi + "');"
        if not executa_cmd(cmd):
            showdialog('Alerta', 'Verificar se o Comite possui Limite de Credenciais')
            self.ui.qspinboxqtd.setValue(self.oldqtd)
        else:
            self.oldqtd = qtd

    def changes(self):
        oi = self.ui.qcomboboxoi.currentText()
        tipo = self.ui.qcomboboxtipocred.currentText()
        cmd = "SELECT quantidade from limites_oi JOIN orgao_imprensa "
        cmd += "ON orgao_imprensa = id WHERE nome = '" + oi + "' "
        cmd += "AND tipo_credencial = '" + tipo + "';"
        try:
            qtd = executa_select(cmd)[0][0]
            self.ui.qspinboxqtd.setValue(qtd)
        except(Exception):
            pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = edit_limitesoi()
    mw.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
