import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)  # This is a very common line bc of sys

window = loader.load("TestWindow.ui", None)
# add functionality here
print(type(window))

my_button = window.findChildren(
    QtWidgets.QPushButton
)  # underneath this QTwidget called window, I want to find children of all type and return those as a list
my_line_edit = window.findChildren(
    QtWidgets.QLineEdit
)  # now we have a way of grabbing these child elements we can do things to them
# # print(myButton)
# # print(my_line_edit[0].objectName())  # you guessed this right ()

my_button[0].clicked.connect(
    lambda: button_clicked()
)  # specifies the element that clicked is under


# # we have to tell the button what to do when it is clicked
def button_clicked():
    my_text = my_line_edit[
        0
    ].text()  # this will grab contents of text box. Needs [0] to know that it needs the first (asnd only) value in the list.
    print(f'Got text from button: {my_text}')


window.show()
app.exec()
print(my_button)  # this gives you the full list associated with the variable
print(
    my_button[0]
)  # this gives you the individual value in the list at the first index position.
print("\n")
print(type(my_button))
print(type(my_button[0]))
