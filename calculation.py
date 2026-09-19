def calculate_gear_parameters(
    rpm_input,
    rpm_output,
    motor_power,
    pinion_teeth,
    module,
    efficiency_percent,
    pressure_angle,
    face_width,
    shaft_diameter
):
    gear_ratio = rpm_input / rpm_output
    gear_teeth = round(pinion_teeth * gear_ratio)
    actual_gear_ratio = gear_teeth / pinion_teeth

    efficiency = efficiency_percent / 100

    input_torque = 9550 * motor_power / rpm_input
    output_torque = input_torque * actual_gear_ratio * efficiency

    pinion_diameter = pinion_teeth * module
    gear_diameter = gear_teeth * module
    center_distance = (pinion_diameter + gear_diameter) / 2

    error = abs(actual_gear_ratio - gear_ratio) / gear_ratio * 100

    return {
        "pinion_teeth": pinion_teeth,
        "gear_teeth": gear_teeth,
        "module": module,
        "pressure_angle": pressure_angle,
        "face_width": face_width,
        "shaft_diameter": shaft_diameter,
        "gear_ratio": gear_ratio,
        "actual_gear_ratio": actual_gear_ratio,
        "error": error,
        "input_torque": input_torque,
        "actual_output_torque": output_torque,
        "center_distance": center_distance
    }