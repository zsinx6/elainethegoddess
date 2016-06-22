#! python
# -*- coding: utf-8 -*-
"""Add Orgão de Imprensa
"""

import sys
from PyQt5 import QtWidgets

from addoi import Ui_Form
from bdconn import insert, select, showdialog


class add_oi(QtWidgets.QWidget):
    def __init__(self, parent=None):
        """inicia a tela e seleciona o nome de todos os comites
            para adicionalos em um combobox
        """
        super(add_oi, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        comite = select('comite', ['nome'])
        if not comite:
            showdialog('Alerta', 'Nenhum Comitê cadastrado')
            return
        self.eval_combobox(comite)
        self.connect_signals()

    def eval_combobox(self, lista):
        """adiciona lista na combobox do comite
        """
        for item in lista:
            self.ui.qcombocomite.addItem(item[0])

    def connect_signals(self):
        self.ui.addbutton.clicked.connect(self.addbutton_click)

    def addbutton_click(self):
        """ pega do formulario nome, endereco, nome_representante,
            email_representante, comite e adiciona na tabela orgao_imprensa
        """
        nome = self.ui.qlinenome.text()
        endereco = self.ui.qlineend.text()
        nome_representante = self.ui.qlinenomerepr.text()
        email_representante = self.ui.qlineemailrepr.text()
        comite = self.ui.qcombocomite.currentText()

        """verifica se campo nome foi preenchido
        """
        if nome:
            kwargs = {'nome': "'" + nome + "'",
                      'comite': "'" + comite + "'"}
            if endereco:
                kwargs['endereco'] = "'" + endereco + "'"
            if nome_representante:
                kwargs['nome_representante'] = "'" + nome_representante + "'"
            if email_representante:
                kwargs['email_representante'] = "'" + email_representante + "'"
            if(insert('orgao_imprensa', kwargs)):
                self.parent().hide()
                self.parent().parent().setWindowTitle(self.parent().parent().title)
            else:
                showdialog ('Erro', 'Erro na insercao, verifique se um OI com esse nome ja nao esta cadastrado!');
        else:
            showdialog('Erro', 'O campo nome é obrigatório')


def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = add_oi()
    mw.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
