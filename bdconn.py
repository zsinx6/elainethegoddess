import psycopg2
from PyQt5 import QtWidgets


def select(tabela, attr=None):
    try:
        conn = psycopg2.connect("dbname=BD user=lucas")
        cur = conn.cursor()
    except(Exception):
        showdialog("Erro no banco",
                   "Problema ao conectar no banco de dados")
        return []
    if not attr:
        attr = '*'
    else:
        attr = ','.join(attr)
    cmd = 'SELECT ' + attr + ' FROM ' + tabela + ';'
    print(cmd)
    try:
        cur.execute(cmd)
        conn.commit()
        ret = cur.fetchall()
    except(Exception):
        showdialog("Erro ao consultar",
                   "Verifique a conexão")
        ret = []
    cur.close()
    conn.close()
    return ret


def insert(tabela, kwargs):
    try:
        conn = psycopg2.connect("dbname=BD user=lucas")
        cur = conn.cursor()
    except(Exception):
        showdialog("Erro no banco",
                   "Problema ao conectar no banco de dados")
        return False
    cmd = 'INSERT INTO ' + tabela + ' ('
    attr = ','.join(kwargs.keys())
    values = ','.join(kwargs.values())
    cmd += attr + ') VALUES('
    cmd += values + ');'
    print(cmd)
    try:
        cur.execute(cmd)
        conn.commit()
        ret = True
    except(Exception):
        showdialog("Erro ao inserir",
                   "Verifique os campos e tente novamente")
        ret = False
    cur.close()
    conn.close()
    return ret


def showdialog(titulo, texto):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Critical)
    msg.setText(texto)
    msg.setWindowTitle(titulo)
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.exec_()
