import shutil
import subprocess
import tkinter as tk
from pathlib import Path
from tkinter import messagebox

from calculation import calculate_gear_parameters


def get_data():
    return calculate_gear_parameters(
        float(entries["rpm_input"].get()),
        float(entries["rpm_output"].get()),
        float(entries["motor_power"].get()),
        int(entries["pinion_teeth"].get()),
        float(entries["module"].get()),
        float(entries["efficiency"].get()),
        float(entries["pressure_angle"].get()),
        float(entries["face_width"].get()),
        float(entries["shaft_diameter"].get())
    )


def find_freecad():
    # First check if FreeCADCmd is available in the system PATH
    freecad_path = shutil.which("FreeCADCmd")

    if freecad_path:
        return freecad_path

    # Common FreeCAD installation folders on Windows
    possible_paths = [
        Path.home() / "AppData/Local/Programs/FreeCAD 1.1/bin/freecadcmd.exe",
        Path(r"C:\Program Files\FreeCAD 1.1\bin\FreeCADCmd.exe"),
        Path(r"C:\Program Files\FreeCAD 1.0\bin\FreeCADCmd.exe")
    ]

    for path in possible_paths:
        if path.exists():
            return str(path)

    return None


def calculate():
    try:
        data = get_data()

        results = (
            f"Gear ratio: {data['gear_ratio']:.2f}\n"
            f"Gear teeth: {data['gear_teeth']}\n"
            f"Input torque: {data['input_torque']:.2f} Nm\n"
            f"Output torque: {data['actual_output_torque']:.2f} Nm\n"
            f"Center distance: {data['center_distance']:.2f} mm"
        )

        result_label.config(text=results)

    except ValueError:
        messagebox.showerror(
            "Invalid input",
            "Please enter valid numerical values."
        )


def generate_3d_model():
    try:
        data = get_data()
    except ValueError:
        messagebox.showerror(
            "Invalid input",
            "Please enter valid numerical values."
        )
        return

    freecad_path = find_freecad()

    if freecad_path is None:
        messagebox.showerror(
            "FreeCAD not found",
            "FreeCAD could not be found on this computer."
        )
        return

    project_folder = Path(__file__).resolve().parent
    freecad_script = project_folder / "freecad_gear.py"

    subprocess.Popen([
        freecad_path,
        str(freecad_script),
        str(data["pinion_teeth"]),
        str(data["gear_teeth"]),
        str(data["module"]),
        str(data["pressure_angle"]),
        str(data["face_width"]),
        str(data["shaft_diameter"]),
        str(data["center_distance"])
    ], cwd=project_folder)


window = tk.Tk()
window.title("Gear Ratio Designer")
window.geometry("500x750")
window.configure(bg="lightblue")
window.resizable(False, False)

tk.Label(
    window,
    text="GEAR RATIO DESIGNER",
    font=("Arial", 18, "bold")
).pack(pady=20)

input_frame = tk.Frame(window)
input_frame.pack(pady=10)

fields = [
    ("rpm_input", "Input speed (rpm)"),
    ("rpm_output", "Output speed (rpm)"),
    ("motor_power", "Motor power (kW)"),
    ("pinion_teeth", "Pinion teeth"),
    ("module", "Module (mm)"),
    ("efficiency", "Efficiency (%)"),
    ("pressure_angle", "Pressure angle (°)"),
    ("face_width", "Face width (mm)"),
    ("shaft_diameter", "Shaft diameter (mm)")
]

entries = {}

for row, (name, label) in enumerate(fields):
    tk.Label(
        input_frame,
        text=label
    ).grid(
        row=row,
        column=0,
        padx=10,
        pady=5
    )

    entry = tk.Entry(input_frame)
    entry.grid(
        row=row,
        column=1,
        padx=10,
        pady=5
    )

    entries[name] = entry

result_label = tk.Label(
    window,
    text="Results will appear here",
    justify="left"
)
result_label.pack(pady=15)

tk.Button(
    window,
    text="Calculate",
    command=calculate
).pack(pady=20)

tk.Button(
    window,
    text="Generate 3D Model",
    command=generate_3d_model
).pack(pady=10)

window.mainloop()