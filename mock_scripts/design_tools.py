"""
HealthData Labelling System
===========================

module: design tools

Notes
-----
    This module is not really needed it is made just make the mock terminal
    actions a bit more fancy.
"""


import importlib
from platform import system as get_os_name


def colored(text : str, foreground_color : str) -> str:
    """
    Colorize text
    =============

    Parameters
    ----------
    text : str
        Text to colorize.
    foreground_color : str
        Name of the Foreground color.

    Returns
    -------
    str
        Colorited text string.

    Notes
    -----
        This function requires colorama on windows.
    """

    fore = {'BLACK' : '30;',
            'RED' : '31;',
            'GREEN' : '32;',
            'YELLOW' : '33;',
            'BLUE' : '34;',
            'MAGENTA' : '35;',
            'CYAN' : '36;',
            'WHITE' : '37;'}
    fore_color = foreground_color.upper()
    if fore_color in fore.keys():
        result = '\033[{};1m{}\033[0m'.format(fore[fore_color], text)
    else:
        result = text
    return result


def not_colored(text : str, foreground_color : str) -> str:
    """
    Do not colorize text
    ====================

    Parameters
    ----------
    text : str
        Text to colorize.
    foreground_color : str
        Name of the Foreground color. (Not used.)

    Returns
    -------
    str
        Colorited text string.

    Notes
    -----
        This function is used when colorama doesn't present.
    """

    # pylint: disable=unused-argument
    #         The unused argument is the point of the function, since this
    #         provides compatibility.

    return text


if get_os_name() == 'Windows':
    if importlib.util.find_spec("colorama") is not None:
        import colorama
        colorama.init()
    else:
        colored = not_colored
