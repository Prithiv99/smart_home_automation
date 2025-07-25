# SPDX-FileCopyrightText: 2018 Scott Shawcroft for Adafruit Industries
# SPDX-FileCopyrightText: 2022-2023 Matt Land
# SPDX-FileCopyrightText: Brooke Storm
# SPDX-FileCopyrightText: Sam McGahan
#
# SPDX-License-Identifier: MIT

"""
`adafruit_imageload.pnm.pbm_ascii`
====================================================

Load pixel values (indices or colors) into a bitmap and for an ascii ppm,
return None for pallet.

* Author(s):  Matt Land, Brooke Storm, Sam McGahan

"""

try:
    from typing import Tuple, Optional
    from io import BufferedReader
    from displayio import Palette, Bitmap
except ImportError:
    pass

__version__ = "1.17.1"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_ImageLoad.git"


def load(
    file: BufferedReader,
    width: int,
    height: int,
    bitmap: Bitmap,
    palette: Optional[Palette] = None,
) -> Tuple[Bitmap, Optional[Palette]]:
    """
    Load a P1 'PBM' ascii image into the displayio.Bitmap
    """
    next_byte = b"1"  # just to start the iterator
    for y in range(height):
        x = 0
        while next_byte:
            next_byte = file.read(1)
            if not next_byte.isdigit():
                continue
            bitmap[x, y] = 1 if next_byte == b"1" else 0
            if x == width - 1:
                break
            x += 1
    return bitmap, palette
