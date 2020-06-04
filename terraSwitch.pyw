import tkinter
from os.path import exists
from subprocess import Popen
from sys import exit

PATH_VANILLA = "Terraria_1.4.0.4.exe"
PATH_TMODLOADER = "tModLoader/tModLoader.exe"


def start_Vanilla():
    Popen(PATH_VANILLA)
    exit()


def start_tModLoader():
    Popen(PATH_TMODLOADER, cwd="tModLoader")
    exit()


if __name__ == "__main__":
    # create a window and change the title
    window = tkinter.Tk()
    window.title("terraSwitch")

    # can be used to configure window size; fine without it
    # window.geometry('360x125')

    # add buttons that create child process with necessary .exe
    switch_Vanilla = tkinter.Button(
        window, text="Vanilla", command=start_Vanilla, font=("Roboto", 26))
    #switch_tModLoader.grid(padx=120, pady=30)
    if not exists(PATH_VANILLA):
        switch_Vanilla.config(bg="red", command='')

    switch_tModLoader = tkinter.Button(
        window, text="tModLoader", command=start_tModLoader, font=("Roboto", 26))
    # switch_Vanilla.grid(padx=120, pady=65)
    if not exists(PATH_TMODLOADER):
        switch_tModLoader.config(bg="red", command='')

    switch_tModLoader.pack(fill='x')
    switch_Vanilla.pack(fill='x')

    window.mainloop()
