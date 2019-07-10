# terraSwitch

A simple GUI to choose a terraria launcher for Windows.

## Requirements

python ^3.7  
tkinter  
pyinstaller  

## Installation

- Rename and put into Terraria folder:
  - Vanilla terraria -> Terraria_Vanilla.exe
  - tModLoader terraria -> Terraria_tModLoader.exe
- Do

    ```cmd
    pyinstaller terraSwitch.pyw -F -w -n Terraria
    ```

- Put Terraria.exe generated in ./dist/ to Terraria folder.
