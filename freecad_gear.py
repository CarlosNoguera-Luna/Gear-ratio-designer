import os
import sys

import FreeCAD as App
import Part
from freecad.gears import commands


pinion_teeth = int(sys.argv[2])
gear_teeth = int(sys.argv[3])
module = float(sys.argv[4])
pressure_angle = float(sys.argv[5])
face_width = float(sys.argv[6])
shaft_diameter = float(sys.argv[7])
center_distance = float(sys.argv[8])

doc = App.newDocument("Gear_Transmission")

pinion = commands.CreateInvoluteGear.create()
pinion.num_teeth = pinion_teeth
pinion.module = module
pinion.pressure_angle = pressure_angle
pinion.height = face_width

gear = commands.CreateInvoluteGear.create()
gear.num_teeth = gear_teeth
gear.module = module
gear.pressure_angle = pressure_angle
gear.height = face_width

doc.recompute()

shaft_hole = Part.makeCylinder(shaft_diameter / 2, face_width)
pinion.Shape = pinion.Shape.cut(shaft_hole)

gear_hole = Part.makeCylinder(shaft_diameter / 2, face_width)
gear.Shape = gear.Shape.cut(gear_hole)

gear.Placement.Base.x = center_distance

gear_tooth_angle = 360 / gear_teeth
gear.Placement.Rotation = App.Rotation(
    App.Vector(0, 0, 1),
    gear_tooth_angle / 2
)

file_number = 1

while True:
    file_name = f"gear_transmission_{file_number}.FCStd"

    if not os.path.exists(file_name):
        break

    file_number += 1

doc.saveAs(file_name)

print("Model saved as:", os.path.abspath(file_name))