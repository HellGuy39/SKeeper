import os
import platform
from domain.state.ColorSchema import ColorSchema


class Colorizer:

    @staticmethod
    def set_terminal_color(schema: ColorSchema):

        if schema is ColorSchema.default:
            return

        if platform.system() == 'Windows':
            os.system(f'color {Colorizer.__schema_to_windows_color_format(schema)}')
        else:
            pass

    # CMD
    # 1 - Dark Blue
    # 2 - Dark Green
    # 6 - Dark Yellow
    # F - White
    # A - Green
    # 7 - Gray
    # 0 - Black
    @staticmethod
    def __schema_to_windows_color_format(schema: ColorSchema) -> str:
        match schema:
            case ColorSchema.gray_and_dark_blue:
                return '7' + '1'
            case ColorSchema.green_and_white:
                return 'A' + 'F'
            case ColorSchema.white_and_black:
                return 'F' + '0'
            case ColorSchema.white_and_dark_blue:
                return 'F' + '1'
            case ColorSchema.dark_blue_and_white:
                return '1' + 'F'
            case ColorSchema.dark_green_and_black:
                return '2' + '0'
            case ColorSchema.dark_yellow_dark_blue:
                return '6' + '1'
            case _:
                return '0' + '7'
