import tkinter

window = tkinter.Tk()
window.title("terraSwitcher")
window.geometry('350x170')

switch_tModLoader = tkinter.Button(window, text="tModLoader", command=print("yeet"), font=("Roboto", 24))
#switch_tModLoader.grid(padx=120, pady=30)
switch_Vanilla = tkinter.Button(window, text="Terraria Vanilla", command=print("oof"), font=("Roboto", 24))
# switch_Vanilla.grid(padx=120, pady=65)
switch_tModLoader.pack(fill='x')
switch_Vanilla.pack(fill='x')

window.mainloop()