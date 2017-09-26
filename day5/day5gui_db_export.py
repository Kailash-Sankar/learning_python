import sys, sqlite3
from PyQt4 import QtGui
import day5db2 as exporter


def save_book():
    id = int(textbox_p.text())
    name = str(textbox_t.text())
    author = str(textbox_r.text())
    insert_book(id, name, author)


def insert_book(id, name, author):
    # connection string
    conn = sqlite3.connect("dev.db")

    # receive something like a file handle
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books VALUES(?,?,?)', (id, name, author))
    conn.commit()


def export_to_xls():
    exporter.export_to_xls('qt.xls', 'books')


app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.setGeometry(100, 100, 300, 250)
window.setWindowTitle("Book Keeper")

label_p = QtGui.QLabel("ID", window)
label_p.move(20, 20)

label_t = QtGui.QLabel("Name", window)
label_t.move(20, 40)

label_r = QtGui.QLabel("Author", window)
label_r.move(20, 60)

textbox_p = QtGui.QLineEdit(window)
textbox_p.move(100, 20)

textbox_t = QtGui.QLineEdit(window)
textbox_t.move(100, 40)

textbox_r = QtGui.QLineEdit(window)
textbox_r.move(100, 60)

button = QtGui.QPushButton('Save', window)
button.move(100, 100)
button.clicked.connect(save_book)

button2 = QtGui.QPushButton('Export xls', window)
button2.move(100, 140)
button2.clicked.connect(export_to_xls)

window.show()

raw_input("Press enter to quit")
