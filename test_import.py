import sys

import PyQtX
from PyQtX import QtCore, QtWidgets, QtWebKitWidgets


app = QtWidgets.QApplication(sys.argv)
print(
	QtWidgets.QFileDialog.getOpenFileName(None, 'Test123', '.')
)