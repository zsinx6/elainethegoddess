#! python
# -*- coding: utf-8 -*-
"""Main Window.
"""

import sys
from PyQt5 import QtWidgets

from addpi import Ui_Form


class add_pi(QtWidgets.QWidget):
    """adiciona profissional de imprensa
    """
    def __init__(self, parent = None):
        super(add_pi, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = add_pi()
    mw.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
