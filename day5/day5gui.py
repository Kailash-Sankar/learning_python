import sys
from PyQt4 import QtGui
app=QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.setGeometry(100,100,500,300)
window.setWindowTitle("Hello Hyderabad")
window.show()
raw_input("Enter any key to quit")
