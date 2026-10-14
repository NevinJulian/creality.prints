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
