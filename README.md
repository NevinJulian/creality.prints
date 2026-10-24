# creality.prints

My 3D printing projects for the Creality K2 with CFS. Every print is modelled in Python with [build123d](https://github.com/gumyr/build123d), one folder per print.

## Setup

Needs Python 3.11 to 3.14.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

In VS Code, select `.venv` as the interpreter and install the OCP CAD Viewer extension.

## Usage

Open the script of a print and run it while the OCP CAD Viewer is open. The model shows up in the viewer and the STL files are written next to the script. Slice them in Creality Print.

## Prints

| Folder | Description |
| --- | --- |
| [clearance-test](clearance-test) | Pin and hole plate to find the fit clearance for this printer |
| [cup-holder](cup-holder) | Clamp-on cup holder for a table edge, reaches past a bevelled underside |
| [cutlery](cutlery) | Fork, spoon and knife with the sun inlaid in the handle, printed flat for strength |
| [golf-ball-clip](golf-ball-clip) | Clip for the golf bag with snap-in pockets for three balls and holes for nine tees |
| [keychain](keychain) | Keychain with the Le Nerima sun inlaid flush in the face |
| [plant-pole](plant-pole) | Modular moss pole with a diamond lattice, twist lock, pot, stand, cap, watering aid and stem clips |
| [purge-bin](purge-bin) | Bin behind the K2 that catches the purge waste from the colour changes, held by two magnets |
| [ruler](ruler) | 20 cm ruler with marks, numbers and the Le Nerima sun inlaid flush in the face |
