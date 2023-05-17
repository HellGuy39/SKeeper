import enum


class ColorSchema(enum.Enum):
    default = 0
    gray_and_dark_blue = 1
    green_and_white = 2
    white_and_black = 3
    white_and_dark_blue = 4
    dark_blue_and_white = 5
    dark_green_and_black = 6
    dark_yellow_dark_blue = 7


def int_to_color_schema(value) -> ColorSchema:
    match value:
        case 0:
            return ColorSchema.default
        case 1:
            return ColorSchema.gray_and_dark_blue
        case 2:
            return ColorSchema.green_and_white
        case 3:
            return ColorSchema.white_and_black
        case 4:
            return ColorSchema.white_and_dark_blue
        case 5:
            return ColorSchema.dark_blue_and_white
        case 6:
            return ColorSchema.dark_green_and_black
        case 7:
            return ColorSchema.dark_yellow_dark_blue
        case _:
            return ColorSchema.default
