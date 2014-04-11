try:
	from PyQt5.QtWidgets import *
except ImportError:
	from PyQt4.QtGui import *

	class QFileDialog(QtWidgets.QFileDialog):
		def getOpenFileName(self):
			super(QFileDialog, self).getOpenFileNameAndFilter()
			print('Called getOpenFileNameAndFilter()')

		def getOpenFileNames(self):
			super(QFileDialog, self).getOpenFileNamesAndFilter()
			print('Called getOpenFileNamesAndFilter()')

		def getSaveFileName(self):
			super(QFileDialog, self).getSaveFileNameAndFilter()
			print('Called getSaveFileNameAndFilter()')

print('Imported QtWidgets')