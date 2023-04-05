from typing import Union, List


class Colors:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    HEADER = '\033[95m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


line = '-------------------------------------------------------------------'


def print_color(text: ..., colors: Union[Colors, List[Colors]]) -> None:
    """
    Print the text with the given colors
    :param text: the text to be printed
    :param colors: the colors to be used
    """
    if not isinstance(colors, list):
        colors = [colors]

    joined_colors = ''
    for color in colors:
        joined_colors += color
    print(f'{joined_colors}{text}{Colors.ENDC}')
