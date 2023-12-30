#import PYSimpleGUI
import PySimpleGUI as sg
#Draw the button
layout = [[sg.Button('Select Origin Folder', size=(15,4))]]
layout = [[sg.Button('Select Destination Folder', size=(15,4))]]
#Draw the window
window = sg.Window('GUI SAMPLE', layout, size=(200,200))
#Define what happens when the button is clicked 
event, values = window.read()