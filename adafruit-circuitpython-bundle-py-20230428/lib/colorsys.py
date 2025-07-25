# SPDX-FileCopyrightText: Python Software Foundation
#
# SPDX-License-Identifier: PSF-2.0

"""
`colorsys`
====================================================

Subset of CPython module colorsys for use in CircuitPython.

Conversion functions between RGB and other color systems

* Author(s): Python Software Foundation

Implementation Notes
--------------------

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

try:
    from typing import Tuple
except ImportError:
    pass


__version__ = "2.0.14"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Colorsys.git"
__all__ = ["hls_to_rgb", "hsv_to_rgb"]

# Some floating point constants

ONE_THIRD = 1.0 / 3.0
ONE_SIXTH = 1.0 / 6.0
TWO_THIRD = 2.0 / 3.0

# HLS: Hue, Luminance, Saturation
# H: position in the spectrum
# L: color lightness
# S: color saturation


def hls_to_rgb(hue: float, light: float, sat: float) -> Tuple[float, float, float]:
    """Converts HLS to RGB values

    :param float hue: The hue of the color to convert
    :param float light: The lightness of the color to convert
    :param float sat: The saturation of the color to convert
    """

    if sat == 0.0:
        return light, light, light
    if light <= 0.5:
        chroma2 = light * (1.0 + sat)
    else:
        chroma2 = light + sat - (light * sat)
    chroma1 = 2.0 * light - chroma2
    return (
        int(_v(chroma1, chroma2, hue + ONE_THIRD) * 255),
        int(_v(chroma1, chroma2, hue) * 255),
        int(_v(chroma1, chroma2, hue - ONE_THIRD) * 255),
    )


def _v(chroma1: float, chroma2: float, hue: float) -> float:
    hue = hue % 1.0
    if hue < ONE_SIXTH:
        return chroma1 + (chroma2 - chroma1) * hue * 6.0
    if hue < 0.5:
        return chroma2
    if hue < TWO_THIRD:
        return chroma1 + (chroma2 - chroma1) * (TWO_THIRD - hue) * 6.0
    return chroma1


# HSV: Hue, Saturation, Value
# H: position in the spectrum
# S: color saturation ("purity")
# V: color brightness


def hsv_to_rgb(  # pylint: disable=too-many-return-statements,inconsistent-return-statements
    hue: float, sat: float, val: float
) -> Tuple[float, float, float]:
    """Converts HSV to RGB values

    :param float hue: The hue of the color to convert
    :param float sat: The saturation of the color to convert
    :param float val: The value (or brightness) of the color to convert
    """
    if sat == 0.0:
        return val, val, val
    i = int(hue * 6.0)  # assume int() truncates!
    hue1 = (hue * 6.0) - i
    chroma1 = val * (1.0 - sat)
    chroma2 = val * (1.0 - sat * hue1)
    chroma3 = val * (1.0 - sat * (1.0 - hue1))
    i = i % 6
    if i == 0:
        return int(val * 255), int(chroma3 * 255), int(chroma1 * 255)
    if i == 1:
        return int(chroma2 * 255), int(val * 255), int(chroma1 * 255)
    if i == 2:
        return int(chroma1 * 255), int(val * 255), int(chroma3 * 255)
    if i == 3:
        return int(chroma1 * 255), int(chroma2 * 255), int(val * 255)
    if i == 4:
        return int(chroma3 * 255), int(chroma1 * 255), int(val * 255)
    if i == 5:
        return int(val * 255), int(chroma1 * 255), int(chroma2 * 255)
    # Cannot get here
