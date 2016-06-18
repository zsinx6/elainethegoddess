#! python
# -*- coding: utf-8 -*-
"""Add Orgão de Imprensa
"""

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

from addpi import Ui_Form
from bdconn import insert, select, showdialog


class add_pi(QtWidgets.QWidget):
    def __init__(self, parent=None):
        """inicia a tela e seleciona o nome de todos os comites
            para adicionalos em um combobox
        """
        super(add_pi, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        oi = select('orgao_imprensa', ['nome'])
        cred = select('tipo_credencial', ['sigla'])
        self.eval_comboboxoi(oi)
        self.eval_comboboxcred(cred)
        self.connect_signals()

    def eval_comboboxoi(self, lista):
        """adiciona lista na combobox do orgao de imprensa
        """
        for item in lista:
            self.ui.qcomboboxoi.addItem(item[0])

    def eval_comboboxcred(self, lista):
        """adiciona lista na combobox do tipo credencial
        """
        for item in lista:
            self.ui.qcomboboxcred.addItem(item[0])

    def connect_signals(self):
        self.ui.addbutton.clicked.connect(self.addbutton_click)

    def addbutton_click(self):
        passaporte = self.ui.qlinepass.text()
        cpf = self.ui.qlinecpf.text()
        data = self.ui.qdate.date().toString(QtCore.Qt.ISODate)
        func = self.ui.qlinefunc.text()
        nome = self.ui.qlinenome.text()
        email = self.ui.qlineemail.text()
        nacio = self.ui.qlinenacio.text()
        oi = self.ui.qcomboboxoi.currentText()
        cred = self.ui.qcomboboxcred.currentText()
        if nome and data and func and email and nacio:
                kwargs = {'nome': "'" + nome + "'",
                          'email': "'" + email + "'",
                          'data_nascimento': "'" + data + "'",
                          'funcao': "'" + func + "'",
                          'nacionalidade': "'" + nacio + "'",
                          }
                if passaporte:
                    kwargs['passaporte'] = "'" + passaporte + "'"
                if cpf:
                    kwargs['cpf'] = "'" + cpf + "'"
        else:
            showdialog("Erro", """Todos os campos
                       devem ser preenchidos!""")


def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = add_pi()
    mw.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
