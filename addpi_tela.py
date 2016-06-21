#! python
# -*- coding: utf-8 -*-
"""Add Profissional de Imprensa
"""

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

from addpi import Ui_Form
from bdconn import insert, select, showdialog, executa_select


class add_pi(QtWidgets.QWidget):
    def __init__(self, parent=None):
        """inicia a tela e seleciona o nome de todos os comites
            para adiciona-los em um combobox
        """
        super(add_pi, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        oi = select('orgao_imprensa', ['nome'])
        if not oi:
            showdialog('Erro', 'Não existem OIs registrados')
            self.parent().hide()
            self.parent().parent().setWindowTitle(self.parent().parent().title)
            return
        cred = select('tipo_credencial', ['sigla'])
        if not cred:
            showdialog('Erro', 'Não existem tipos de credenciais registrados')
            self.parent().hide()
            self.parent().parent().setWindowTitle(self.parent().parent().title)
            return
        # oi e cred são listas do retorno do select, vão ser
        # adicionados nos combobox
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
        """adiciona o profissional de imprensa de acordo com os campos
        preenchidos
        """
        passaporte = self.ui.qlinepass.text()
        cpf = self.ui.qlinecpf.text()
        data = self.ui.qdate.date().toString(QtCore.Qt.ISODate)
        func = self.ui.qlinefunc.text()
        nome = self.ui.qlinenome.text()
        email = self.ui.qlineemail.text()
        nacio = self.ui.qlinenacio.text()
        oi = self.ui.qcomboboxoi.currentText()
        cred = self.ui.qcomboboxcred.currentText()
        cmd = "SELECT id FROM orgao_imprensa "
        cmd += "WHERE nome = '" + oi + "';"
        oi2 = executa_select(cmd)[0][0]
        kwargs1 = {'tipo': "'" + cred + "'",
                   'orgao_imprensa': str(oi2)
                  }
        if(insert('credencial', kwargs1)):
            if nome and func:
                cmd = "SELECT codigo FROM credencial "
                cmd += "WHERE tipo = '" + cred + "' AND "
                cmd += "codigo NOT IN (SELECT credencial "
                cmd += "FROM profissional_imprensa);"
                id_cred = executa_select(cmd)
                if not id_cred:
                    showdialog("Erro",
                               "Nenhuma credencial livre do Tipo: " + cred +
                               " para o Orgão de Imprensa: " + oi + "!")
                else:
                    cred = id_cred[0][0]
                    cmd = "SELECT id from orgao_imprensa "
                    cmd += "WHERE nome = '" + oi + "';"
                    id_oi = executa_select(cmd)[0][0]
                    kwargs = {'nome': "'" + nome + "'",
                              'funcao': "'" + func + "'",
                              'orgao_imprensa': str(id_oi),
                              'credencial': str(cred),
                             }
                    if email:
                        kwargs['email'] = "'" + email + "'"
                    if data:
                        kwargs['data_nascimento'] = "'" + data + "'"
                    if nacio:
                        kwargs['nacionalidade'] = "'" + nacio + "'"
                    if passaporte:
                        kwargs['passaporte'] = "'" + passaporte + "'"
                    if cpf:
                        kwargs['cpf'] = "'" + cpf + "'"
                    if insert('profissional_imprensa', kwargs):
                        self.parent().hide()
                        self.parent().parent().setWindowTitle(self.parent().parent().title)
            else:
                showdialog('Erro', 'Os campos nome e função são obrigatórios')
        else:
            showdialog('Alerta', 'O OI não tem credenciais disponiveis')

def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = add_pi()
    mw.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
