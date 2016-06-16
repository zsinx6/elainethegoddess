#! python
# -*- coding: utf-8 -*-
"""Add Credencial
"""

import sys
from PyQt5 import QtWidgets

from addcred import Ui_Form
from bdconn import insert, select


class add_credencial(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(add_credencial, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        oi = select('orgao_imprensa', ['id'])
        self.eval_comboboxoi(oi)
        tipo = select('tipo_credencial', ['sigla'])
        self.eval_comboboxtipo(tipo)
        self.connect_signals()

    def eval_comboboxoi(self, lista):
        for item in lista:
            self.ui.qcombooi.addItem(str(item[0]))

    def eval_comboboxtipo(self, lista):
        for item in lista:
            self.ui.qcombotipo.addItem(str(item[0]))

    def connect_signals(self):
        self.ui.addbutton.clicked.connect(self.addbutton_click)

    def addbutton_click(self):
        tipo = self.ui.qcombotipo.currentText()
        oi = self.ui.qcombooi.currentText()
        kwargs = {'tipo': "'" + tipo + "'",
                  'orgao_imprensa': oi}
        if(insert('credencial', kwargs)):
            self.parent().hide()


def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = add_credencial()
    mw.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
