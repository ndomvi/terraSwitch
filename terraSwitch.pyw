import tkinter
import subprocess

# create a window and change the title
window = tkinter.Tk()
window.title("terraSwitch")

# can be used to configure window size; fine without it
# window.geometry('360x125')

switch_tModLoader = tkinter.Button(
    window, text="Terraria Vanilla", command=lambda: subprocess.run("Terraria_Vanilla.exe"), font=("Roboto", 24))
#switch_tModLoader.grid(padx=120, pady=30)
switch_Vanilla = tkinter.Button(
    window, text="tModLoader", command=lambda: subprocess.run("Terraria_tModLoader.exe"), font=("Roboto", 24))
# switch_Vanilla.grid(padx=120, pady=65)

switch_tModLoader.pack(fill='x')
switch_Vanilla.pack(fill='x')

window.mainloop()
