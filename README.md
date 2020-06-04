# terraSwitch

A simple GUI to choose a Terraria executable for Windows.

## Requirements

python ^3.7  
pyinstaller

## Installation

- Rename Terraria.exe -> Terraria_1.4.0.4.exe
- Do

  ```cmd
  pyinstaller terraSwitch.pyw -F -w -n Terraria
  ```

- Put Terraria.exe generated in ./dist/ to Terraria folder.
- Launch the game as you usually do!
