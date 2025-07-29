def convert_temp(value, units = "k"):
    match units:
        case "c":
            return round(value - 273.15)
        case "f":
            return round(((value - 273.15) * 1.8) + 32)
        case "k":
            return value
        case _:
            return value

def convert_speed(value):
    converted = round(value * 3.6,2)
    return converted