def get_tshirt_size(shoulder_width):
    if shoulder_width <= 38:
        return "S"
    elif shoulder_width <= 40:
        return "M"
    elif shoulder_width <= 43:
        return "L"
    elif shoulder_width <= 45:
        return "XL"
    else:
        return "XXL"


