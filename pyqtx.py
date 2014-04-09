try:
	from PyQt5 import *
except ImportError:
	from PyQt4 import *

try:
	from PyQt5 import QtCore
except ImportError:
	from PyQt4 import QtCore

try:
	from PyQt5 import QtWidgets
except ImportError:
	from PyQt4 import QtGui as QtWidgets

try:
	from PyQt5 import QtWebKitWidgets
except:
	from PyQt4 import QtWebKit as QtWebKitWidgets


# TODO:
## Only import submodule if actually needed
## how to deal with modules which are separated into multiple ones in PyQt4