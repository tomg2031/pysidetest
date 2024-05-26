import sys
from Holderbot import Holderbot
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

from_directory = ""
to_directory = ""
holder = Holderbot()  # this instantiates the class, so self does not trigger an error
loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)  # This is a very common line bc of sys

window = loader.load("TestWindow.ui", None)
# add functionality here
print(type(window))

executeButton = window.findChild(QtWidgets.QPushButton, "Execute")
fromButton = window.findChild(QtWidgets.QPushButton, "getFromDirectory")
toButton = window.findChild(QtWidgets.QPushButton, "getToDirectory")


# my_buttons = window.findChildren(
#     QtWidgets.QPushButton
# )  # underneath this QTwidget called window, I want to find children of all type and return those as a list

# for i in my_buttons:
#     print(i)

fromLineEdit = window.findChild(QtWidgets.QLineEdit, "getFromLineEdit")
toLineEdit = window.findChild(QtWidgets.QLineEdit, "getToLineEdit")

# my_line_edit = window.findChildren(
#     QtWidgets.QLineEdit
# )  # now we have a way of grabbing these child elements we can do things to them

executeButton.clicked.connect(
    lambda: button_clicked()
)  # specifies the element that clicked is under

fromButton.clicked.connect(
    lambda: get_from_directory()
)  # specifies the element that clicked is under

toButton.clicked.connect(
    lambda: get_to_directory()
)  # specifies the element that clicked is under


# # we have to tell the button what to do when it is clicked
def get_from_directory():
    from_directory = QtWidgets.QFileDialog.getExistingDirectory()  # changed this to be able to select Folder in browser. We will implement this into the testWindow.ui when ready to select file origin, destinatiuon
    # print(from_directory)
    fromLineEdit.setText(from_directory + "/")


def get_to_directory():
    to_directory = QtWidgets.QFileDialog.getExistingDirectory()  # changed this to be able to select Folder in browser. We will implement this into the testWindow.ui when ready to select file origin, destinatiuon
    # print(to_directory)
    toLineEdit.setText(to_directory + "/")


def button_clicked():
    from_directory = fromLineEdit.text()  # this will grab contents of text box. Needs [0] to know that it needs the first (asnd only) value in the list.
    to_directory = toLineEdit.text()
    print(f"from_directory is {from_directory}")
    print(f"to_directory is {to_directory}")
    holder.unzip(from_directory, to_directory)


window.show()
app.exec()
