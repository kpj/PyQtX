try:
	from PyQt5 import QtWidgets
except ImportError:
	from PyQt4 import QtGui as QtWidgets

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
print(QtWidgets.QFileDialog)