import flask
import sqlalchemy
import PySimpleGUI as sg

location = (600,600)

layout = [[sg.Text('Hello from PySimpleGUI')], [sg.Button("ADD")], [sg.Button("OK")]]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break
    if event == "ADD" or event == sg.WIN_CLOSED:
        layout.append([sg.Button("NEW")])
        window1 = sg.Window('Demo', location=location).Layout(layout)
        window.close()
        window=window1


        
window.close()