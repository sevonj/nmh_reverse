from collections import namedtuple
from enum import Enum
import os
from pathlib import Path
import struct
import sys
from PIL import Image


TOOL_NAME = "Jyl's GCT0 exporter"

GCT0 = namedtuple("GCT0", ["encoding", "w", "h"])


class Encoding(Enum):
    """
    A guess.
    https://wiki.tockdom.com/wiki/TEX0_(File_Format)
    """

    I4 = 0x00
    I8 = 0x01
    IA4 = 0x02
    IA8 = 0x03
    RGB565 = 0x04
    RGB5A3 = 0x05
    RGBA32 = 0x06
    C4 = 0x08
    C8 = 0x09
    C14X2 = 0x0A
    CMPR = 0x0E


def parse_file(in_path: str):
    with open(in_path, "rb") as f:
        magic = f.read(4)
        if magic != b"GCT0":
            print(f"ERR: Not a GCT0 file! {in_path}")
            return

        encoding = struct.unpack(">i", f.read(4))[0]
        w = struct.unpack(">H", f.read(2))[0]
        h = struct.unpack(">H", f.read(2))[0]

        return GCT0(encoding, w, h)


def unpack(path: str, out_dir: str):
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, Path(path).stem + ".png")
    gct0 = parse_file(path)

    img = None

    match Encoding(gct0.encoding):
        case Encoding.RGB5A3:
            img = unpack_rgb5a3(gct0, path)

        # case Encoding.RGBA32:
        #    img = unpack_rgba32(gct0, path)

        case _:
            print("Unsupported encoding. Skipping.")

    if img != None:
        img.save(out_path)


def unpack_rgb5a3(gct0: GCT0, filepath: str):
    img = Image.new("RGBA", (gct0.w, gct0.h), "black")

    with open(filepath, "rb") as f:
        f.seek(0x40)

        for y in range(gct0.h):
            for x in range(gct0.w):
                block = x // 4 + (y // 4) * (x // 4)

                block_off = 0x40 + block * 32
                px_off = (x % 4) * 2
                px_off += (y % 4) * 4 * 2

                # px_off = 0
                f.seek(block_off + px_off)
                px = struct.unpack(">H", f.read(2))[0]
                if px & 0x8000 != 0:
                    r = (px >> 10) & 0b11111
                    g = (px >> 5) & 0b11111
                    b = px & 0b11111
                    a = 0xFF
                    img.putpixel((x, y), (r * 8, g * 8, b * 8, a))
                else:
                    r = (px >> 8) & 0b1111
                    g = (px >> 4) & 0b111
                    b = px & 0b1111
                    a = px >> 12
                    img.putpixel((x, y), (r * 0x11, g * 0x11, b * 0x11, a * 0x20))

    return img


if __name__ == "__main__":
    match len(sys.argv):
        case 2:
            in_path = sys.argv[1]
            out_path = os.path.join(".", Path(in_path).stem + "_extracted")
            unpack(in_path, out_path)

        case 3:
            in_path = sys.argv[1]
            out_path = sys.argv[2]
            unpack(in_path, out_path)

        case _:
            print(
                "Provide 1 or 2 args:\n    - input file path\n    - output dir path (optional)"
            )
