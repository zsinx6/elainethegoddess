#! python
# -*- coding: utf-8 -*-
"""Add Comite
"""

import sys
from PyQt5 import QtWidgets

from addcomite import Ui_Form
from bdconn import insert, showdialog


class add_comite(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(add_comite, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connect_signals()

    def connect_signals(self):
        self.ui.addbutton.clicked.connect(self.addbutton_click)

    def addbutton_click(self):
        pais = self.ui.qlinepais.text()
        nome = self.ui.qlinenome.text()
        presidente = self.ui.qlinepres.text()
        email_contato = self.ui.qlineemail.text()
        endereco = self.ui.qlineend.text()
        if pais and nome and presidente and email_contato and endereco:
            kwargs = {'pais': "'" + pais + "'",
                      'nome': "'" + nome + "'",
                      'presidente': "'" + presidente + "'",
                      'email_contato': "'" + email_contato + "'",
                      'endereco': "'" + endereco + "'"}
            if(insert('comite', kwargs)):
                self.parent().hide()
        else:
            showdialog("Erro", """Todos os campos
                       devem ser preenchidos!""")


def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = add_comite()
    mw.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
