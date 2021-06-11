"""
graphic_pov.py

This file creates a graphic user interface (GUI)
for the change_pov program
"""


import change_pov as cp
import PySimpleGUI as sg
import os.path


def event_loop(window):
    # Create an event loop
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-FOLDER-":
            folder = values["-FOLDER-"]
            try:
                # Get list of files in folder
                file_list = os.listdir(folder)
            except:
                file_list = []

            fnames = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(folder, f))
                   and f.lower().endswith(".txt")
            ]
            window["-FILE LIST-"].update(fnames)
        if event == "-FILE LIST-":
            file_name = values["-FILE LIST-"][0]



def main():
    cp

    layout = [
        [
            sg.Text("Files"),
            sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse(),
        ],
        [
            sg.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"),
        ]

    ]

    # Create the window
    window = sg.Window(title="Point of View", layout=layout, margins=(300, 150))

    event_loop(window)

    window.close()


if __name__ == '__main__':
    main()
