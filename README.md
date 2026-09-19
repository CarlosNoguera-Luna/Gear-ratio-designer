# Gear-ratio-designer
Python application for preliminary spur gear transmission design with CATIA integration.
# Gear Ratio Designer

Gear Ratio Designer is a small engineering project developed in Python to explore the connection between mechanical calculations, programming and parametric CAD.

The application performs the basic calculations required to define a spur gear transmission and uses the resulting parameters to automatically generate a 3D gear pair in FreeCAD.

The project was developed as a learning project while studying Mechanical Engineering.

## What it does

The user defines the main operating and geometric parameters of the transmission:

- Input speed (rpm)
- Output speed (rpm)
- Motor power (kW)
- Pinion teeth
- Module (mm)
- Transmission efficiency (%)
- Pressure angle (°)
- Face width (mm)
- Shaft diameter (mm)

From these values, the program calculates:

- Theoretical transmission ratio
- Required number of gear teeth
- Actual transmission ratio
- Transmission ratio error
- Input torque
- Output torque considering efficiency
- Center distance

The calculated parameters can then be sent directly to FreeCAD to generate the corresponding 3D gear pair.

## Interface

The graphical interface was developed with Tkinter and provides a simple way to enter the transmission parameters and view the main calculated results.

![Gear Ratio Designer interface](docs/figures/interface.png)

## FreeCAD integration

The application communicates with FreeCAD through a separate Python script.

Using the calculated parameters, FreeCAD generates two involute spur gears with the selected:

- Number of teeth
- Module
- Pressure angle
- Face width
- Shaft diameter
- Center distance

The gears are positioned as a pair and each generated design is saved as a new `.FCStd` file so previous models are not overwritten.

![Generated gear transmission](docs/figures/freecad_model.png)

## Engineering basis

For an external spur gear pair, the required transmission ratio is obtained from the input and output rotational speeds:

    i = n_input / n_output

The number of teeth of the driven gear is estimated from:

    z2 = z1 * i

Since the number of teeth must be an integer, the result is rounded. The actual transmission ratio is then recalculated using the final number of teeth:

    i_actual = z2 / z1

The pitch diameter of each gear follows:

    d = m * z

which allows the center distance to be calculated as:

    a = (d1 + d2) / 2

Input torque is estimated from motor power and rotational speed:

    T = 9550 * P / n

The output torque is calculated using the actual transmission ratio and the specified transmission efficiency.

These calculations are intended for preliminary gear design. Detailed gear strength, contact stress, material selection, manufacturing tolerances and other design checks are outside the current scope of the project.

## Project structure

    Gear-ratio-designer/
    ├── main.py
    ├── gui.py
    ├── calculation.py
    ├── freecad_gear.py
    ├── docs/
    │   └── figures/
    │       ├── interface.png
    │       └── freecad_model.png
    └── .gitignore

### `main.py`

Entry point of the application.

### `gui.py`

Contains the Tkinter interface and connects the user inputs with the calculation and CAD generation parts of the program.

### `calculation.py`

Contains the main mechanical calculations used by the application.

### `freecad_gear.py`

Receives the calculated gear parameters and uses FreeCAD and the FreeCAD Gears Workbench to generate and save the 3D model.

## Requirements

- Python 3
- Tkinter
- FreeCAD
- FreeCAD Gears Workbench

FreeCAD and the FreeCAD Gears Workbench must be installed separately.

## Running the project

Clone or download the repository and open a terminal in the project folder.

Run:

    python main.py

The graphical interface will open.

After entering the required parameters:

- **Calculate** displays the main transmission results.
- **Generate 3D Model** creates the corresponding gear pair using FreeCAD.

## Current scope

The project currently focuses on a simple external spur gear transmission.

It is not intended to replace dedicated gear design software. Its purpose is to combine fundamental mechanical engineering calculations with Python programming and basic CAD automation in a practical project.

Possible future developments include additional design checks, more gear configurations and further CAD automation.