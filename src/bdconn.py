import psycopg2
from PyQt5 import QtWidgets

DB_CONNECT_PARAMETERS = 'dbname=DATABASE_NAME_HERE user=POSTGRES_USER_NAME_HERE'

def select(tabela, attr=None):
    """ recebe o nome da tabela e os atributos a serem selecionados
        se attr=None seleciona todos atributos
    """
    try:
        conn = psycopg2.connect(DB_CONNECT_PARAMETERS)
        cur = conn.cursor()
    except(Exception):
        showdialog("Erro no banco",
                   "Problema ao conectar no banco de dados")
        exit()
    if not attr:
        attr = '*'
    else:
        #concatena a lista seperando cada item com uma comma
        attr = ','.join(attr)
    cmd = 'SELECT ' + attr + ' FROM ' + tabela + ';'
    try:
        #executa o sql
        cur.execute(cmd)
        ret = cur.fetchall()
    except(Exception):
        showdialog("Erro ao consultar",
                   "Verifique a conexão")
        ret = []
    cur.close()
    conn.close()
    return ret


def insert(tabela, kwargs):
    """ insere dados passados no kwargs na table tabela
        formato do kwargs:
        [nome_attr1 => valor1, ..., nome_attr_k => valor_k]
    """
    try:
        conn = psycopg2.connect(DB_CONNECT_PARAMETERS)
        cur = conn.cursor()
    except(Exception):
        showdialog("Erro no banco",
                   "Problema ao conectar no banco de dados")
        exit()
    cmd = 'INSERT INTO ' + tabela + ' ('
    attr = ','.join(kwargs.keys())
    values = ','.join(kwargs.values())
    cmd += attr + ') VALUES('
    cmd += values + ');'
    try:
        cur.execute(cmd)
        conn.commit()
        ret = True
    except(Exception):
        ret = False
    cur.close()
    conn.close()
    return ret


def executa_select(cmd):
    try:
        conn = psycopg2.connect(DB_CONNECT_PARAMETERS)
        cur = conn.cursor()
    except(Exception):
        showdialog("Erro no banco",
                   "Problema ao conectar no banco de dados")
        exit()
    try:
        # executa o sql
        cur.execute(cmd)
        ret = cur.fetchall()
    except(Exception):
        showdialog("Erro ao consultar",
                   "Verifique a conexão")
        ret = []
    cur.close()
    conn.close()
    return ret


def executa_cmd(cmd):
    try:
        conn = psycopg2.connect(DB_CONNECT_PARAMETERS)
        cur = conn.cursor()
    except(Exception):
        showdialog("Erro no banco",
                   "Problema ao conectar no banco de dados")
        exit()
    try:
        cur.execute(cmd)
        conn.commit()
        ret = True
    except(Exception):
        ret = False
    cur.close()
    conn.close()
    return ret


def showdialog(titulo, texto):
    """ mostra em uma janela de dialogo com o titulo passado como arg.
        Mostrando o valor da variavel texto
    """
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Critical)
    msg.setText(texto)
    msg.setWindowTitle(titulo)
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.exec_()
