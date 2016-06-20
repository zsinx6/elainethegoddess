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
        """ manipulador do evento click do mouse para adicionar comite
            utiliza a funcao insert (definida no arquivo bdconn.py) passando
            como argumento kwargs
        """
        pais = self.ui.qlinepais.text()
        nome = self.ui.qlinenome.text()
        presidente = self.ui.qlinepres.text()
        email_contato = self.ui.qlineemail.text()
        endereco = self.ui.qlineend.text()
        if pais and nome and presidente:
            kwargs = {'pais': "'" + pais + "'",
                      'nome': "'" + nome + "'",
                      'presidente': "'" + presidente + "'"}
            if email_contato:
                kwargs'[email_contato'] = "'" + email_contato + "'"
            if endereco:
                kwargs['endereco'] =  "'" + endereco + "'"
            if(insert('comite', kwargs)):
                self.parent().hide()
                self.parent().parent().setWindowTitle(self.parent().parent().title)
        else:
            showdialog('Erro', 'Os campos país, nome e presidente são obrigatórios')


def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = add_comite()
    mw.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
