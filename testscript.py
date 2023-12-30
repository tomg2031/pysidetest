import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader

from_directory = ""
to_directory = ""

loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)  # This is a very common line bc of sys

window = loader.load("TestWindow.ui", None)
# add functionality here
print(type(window))

my_buttons = window.findChildren(
    QtWidgets.QPushButton
)  # underneath this QTwidget called window, I want to find children of all type and return those as a list

for i in my_buttons:
    print(i)

my_line_edit = window.findChildren(
    QtWidgets.QLineEdit
)  # now we have a way of grabbing these child elements we can do things to them

for i in my_line_edit:
    print(i)

my_buttons[0].clicked.connect(
    lambda: button_clicked()
)  # specifies the element that clicked is under

my_buttons[1].clicked.connect(
    lambda: get_from_directory()
)  # specifies the element that clicked is under

my_buttons[2].clicked.connect(
    lambda: get_to_directory()
)  # specifies the element that clicked is under


# # we have to tell the button what to do when it is clicked
def get_from_directory():
    from_directory = QtWidgets.QFileDialog.getExistingDirectory()  # changed this to be able to select Folder in browser. We will implement this into the testWindow.ui when ready to select file origin, destinatiuon
    print(from_directory)
    my_line_edit[0].setText(from_directory)


def get_to_directory():
    to_directory = QtWidgets.QFileDialog.getExistingDirectory()  # changed this to be able to select Folder in browser. We will implement this into the testWindow.ui when ready to select file origin, destinatiuon
    print(to_directory)
    my_line_edit[1].setText(to_directory)


def button_clicked():
    my_text = my_line_edit[
        0
    ].text()  # this will grab contents of text box. Needs [0] to know that it needs the first (asnd only) value in the list.
    print(f"Got super cool text from button: {my_text}")
    print(f"Got super cool text from button again: {my_text}")


window.show()
app.exec()
