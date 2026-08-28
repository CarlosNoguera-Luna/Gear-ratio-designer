
import math
print("GEAR RATIO DESIGN")
rpm1=float(input("Input speed rpm:"))
rpm2=float(input("Output speed rpm:"))
gear_ratio=rpm1/rpm2
motor_power=float(input("Motor power (kW):"))
pinion_teeth = int(input("Pinion teeth: "))
gear_teeth= round( pinion_teeth* gear_ratio)
input_torque=float((9550*motor_power)/rpm1)
module = int(input("Module (mm): "))
efficiency_percent = float(input("Transmission efficiency (%): "))
efficiency = efficiency_percent / 100
pressure_angle = float(input("Pressure angle (degrees): "))
pressure_angle_radians = math.radians(pressure_angle)
face_width = float(input("Face width (mm): "))
shaft_diameter = float(input("Shaft diameter (mm): "))
primitive_diameter_gear= gear_teeth*module

primitive_diameter_pinion= pinion_teeth*module
pinion_base_diameter = primitive_diameter_pinion*math.cos(pressure_angle_radians)
gear_base_diameter = primitive_diameter_gear*math.cos(pressure_angle_radians)

output_torque=input_torque*gear_ratio
actual_gear_ratio= gear_teeth/pinion_teeth


center_distance=primitive_diameter_gear/2+primitive_diameter_pinion/2
error=abs(actual_gear_ratio-gear_ratio)/gear_ratio*100
actual_output_torque = input_torque * actual_gear_ratio * efficiency
pinion_outside_diameter= module*(pinion_teeth+2)
gear_outside_diameter= module*(gear_teeth+2)

pinion_root_diameter = primitive_diameter_pinion - 2.5 * module
gear_root_diameter = primitive_diameter_gear - 2.5 * module
addendum = module
dedendum = 1.25 * module
whole_depth = addendum + dedendum
circular_pitch = math.pi * module
base_pitch = circular_pitch * math.cos(pressure_angle_radians)
tooth_thickness=(math.pi*module)/2
pinion_primitive_radius = primitive_diameter_pinion / 2
pinion_outside_radius = pinion_outside_diameter / 2
pinion_root_radius = pinion_root_diameter / 2

print(f"theoretical transmission ratio = {gear_ratio:.2f}: 1")
print(f"actual transmission ratio = {actual_gear_ratio:.2f}: 1")
print (f"error = {error}%")
print(f"motor power = {motor_power} kW")
print(f"input torque = {input_torque} Nm")
print(f"theoretical_output_torque = {output_torque} Nm")
print (f"gear_teeth = {gear_teeth}")
print (f"primitive_diameter_pinion = {primitive_diameter_pinion}mm")
print (f"primitive_diameter_gear = {primitive_diameter_gear}mm")
print (f"center_distance = {center_distance}mm")
print (f"transmission_efficiency = {efficiency_percent}%")
print (f"actual_output_torque = {actual_output_torque}Nm")
print (f"pinion_outside_diameter = {pinion_outside_diameter}mm")
print (f"pinion_root_diameter = {pinion_root_diameter}mm")
print (f"gear_root_diameter = {gear_root_diameter}")
print (f"gear_outside_diameter = {gear_outside_diameter}")
print(f"addendum = {addendum} mm")
print(f"dedendum = {dedendum} mm")
print(f"whole_depth = {whole_depth} mm")
print(f"tooth_thickness = {tooth_thickness} mm")
print(f"pressure_angle = {pressure_angle} ")
print(f"face_width = {face_width}mm")
print(f"shaft_diameter = {shaft_diameter}mm")
print(f"pinion_base_diameter = {pinion_base_diameter} mm")
print(f"gear_base_diameter = {gear_base_diameter} mm")
print(f"circular_pitch = {circular_pitch} mm")
print(f"base_pitch = {base_pitch} mm")


pinion_base_radius = pinion_base_diameter / 2



x_points = []
y_points = []

t_max = math.sqrt((pinion_outside_radius / pinion_base_radius) ** 2 - 1)

for i in range(101):

    t = t_max * i / 100

   

    x = pinion_base_radius * (math.cos(t) + t * math.sin(t))

    y = pinion_base_radius * (math.sin(t) - t * math.cos(t))

    x_points.append(x)
    y_points.append(y)

x_points_mirror = []
y_points_mirror = []

for i in range(len(x_points)):
    x_points_mirror.append(x_points[i])
    y_points_mirror.append(-y_points[i])
circle_x_base = []
circle_y_base = []

circle_x_primitive = []
circle_y_primitive = []

circle_x_outside = []
circle_y_outside = []


for i in range(361):

    angle = math.radians(i)

    
    circle_x_base.append( pinion_base_radius * math.cos(angle))

    circle_y_base.append(pinion_base_radius * math.sin(angle))

   
    circle_x_primitive.append(pinion_primitive_radius * math.cos(angle))

    circle_y_primitive.append(pinion_primitive_radius * math.sin(angle))

    
    circle_x_outside.append( pinion_outside_radius * math.cos(angle))

    circle_y_outside.append(pinion_outside_radius * math.sin(angle))

#movemos las involuciones para dejar bien definidos los dientes 
tooth_angle= 2*math.pi/pinion_teeth
half_tooth_angle=tooth_angle/4
print("half_tooth_angle",half_tooth_angle)


tooth_thickness_angle=tooth_thickness/pinion_primitive_radius
t_pitch = math.sqrt((pinion_primitive_radius / pinion_base_radius) ** 2 - 1)
involute_angle_at_pitch = t_pitch - math.atan(t_pitch)
theta = (half_tooth_angle + involute_angle_at_pitch)
x_points_left = []
y_points_left = []

x_points_right = []
y_points_right = []
for j in range(len(x_points)):
    x = x_points[j]
    y = y_points[j]
    x_right = x * math.cos(-theta) - y * math.sin(-theta)

    y_right = x * math.sin(-theta) + y * math.cos(-theta)
    
    x_points_right.append(x_right)
    y_points_right.append(y_right)
    
for j in range(len(x_points)):
    x = x_points_mirror[j]
    y = y_points_mirror[j]
    x_left = x * math.cos(theta) - y * math.sin(theta)
    y_left = x * math.sin(theta) + y * math.cos(theta)
    
    x_points_left.append(x_left)
    y_points_left.append(y_left)


left_tip_angle = math.atan2(
    y_points_left[-1],
    x_points_left[-1]
)

right_tip_angle = math.atan2(
    y_points_right[-1],
    x_points_right[-1]
)
tip_x_points= []
tip_y_points= []
number_tip_points = 51
for i in range(number_tip_points):
    tip_angle = (right_tip_angle+ (left_tip_angle - right_tip_angle )* i/ (number_tip_points - 1))

    tip_x = (pinion_outside_radius* math.cos(tip_angle))

    tip_y = (pinion_outside_radius* math.sin(tip_angle))

    tip_x_points.append(tip_x)
    tip_y_points.append(tip_y)


import matplotlib.pyplot as plt
plt.figure(figsize=(7, 7))





plt.plot(
    circle_x_base,
    circle_y_base,
    label="Base circle")

plt.plot(
    circle_x_primitive,
    circle_y_primitive,
    label="Pitch circle")

plt.plot(
    circle_x_outside,
    circle_y_outside,
    label="Outside circle")

plt.plot(
    x_points,
    y_points,
    linewidth=2,
    label="Involute")
plt.plot(
    x_points_mirror,
    y_points_mirror,
    linewidth=2,
    label="Mirrored involute"
)
plt.plot(
    x_points_left,
    y_points_left,
    linewidth=2,
    label="Left tooth flank"
)

plt.plot(
    x_points_right,
    y_points_right,
    linewidth=2,
    label="Right tooth flank"
)
plt.plot(
    tip_x_points,
    tip_y_points,
    linewidth=2,
    label="Tooth tip"
)
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.xlabel("X (mm)")
plt.ylabel("Y (mm)")
plt.title("Pinion involute geometry")
last_radius = math.sqrt( x_points[-1] ** 2 + y_points[-1] ** 2)
left_root_angle = math.atan2(
    y_points_left[0],
    x_points_left[0]
)

right_root_angle = math.atan2(
    y_points_right[0],
    x_points_right[0]
)
left_root_x = pinion_root_radius * math.cos(left_root_angle)
left_root_y = pinion_root_radius * math.sin(left_root_angle)

right_root_x = pinion_root_radius * math.cos(right_root_angle)
right_root_y = pinion_root_radius * math.sin(right_root_angle)
print("Final involute radius:", last_radius)
print("Outside radius:", pinion_outside_radius)
print("Number of involute points:", len(x_points))
print("Number of tip points:", len(tip_x_points))
 
plt.show()