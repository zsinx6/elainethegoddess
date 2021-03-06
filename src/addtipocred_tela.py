#! python
# -*- coding: utf-8 -*-
"""Add Tipo Crecencial
Adiciona novo tipo de credencial
Precisa ser informado a sigla do tipo de credencial, a funcao e se possui direito de transmissao
"""

import sys
from PyQt5 import QtWidgets

from addtipocred import Ui_Form
from bdconn import insert, showdialog


class add_tipocred(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(add_tipocred, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connect_signals()

    def connect_signals(self):
        self.ui.addbutton.clicked.connect(self.addbutton_click)

    def addbutton_click(self):
        sigla = self.ui.qlinesigla.text()
        funcao = self.ui.qlinefunc.text()
        transmissao = self.ui.qcombotrans.currentIndex()
        if transmissao == 0:
            transmissao = 's'
        else:
            transmissao = 'n'

        """verifica se os dados foram informados
        """
        if sigla and funcao:
            kwargs = {'sigla': "'" + sigla + "'",
                      'funcao': "'" + funcao + "'",
                      'direito_transmissao': "'" + transmissao + "'"}

            #insere o novo tipo de credencial
            if(insert('tipo_credencial', kwargs)):
                self.parent().hide()
                self.parent().parent().setWindowTitle(self.parent().parent().title)
            else:
                showdialog ('Erro', 'Erro na inserção, verifique se esse tipo de credencial, já não existe');
        else:
            showdialog("Erro", "Todos os campos devem ser preenchidos!")


def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = add_tipocred()
    mw.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
