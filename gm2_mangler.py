import os
import random
from nmh_gm2 import NmhGm2
from glob import glob
import struct
import sys
from reset_files import reset_files

TOOL_NAME = "Jyl's NMH GM2 exporter"

DIR = "filesystem/DATA/files/STG_HI"
OUT_DIR = "filesystem_edited/DATA/files/STG_HI"


def mangle(in_path: str, out_path: str):
    print(f"mangling: {in_path}...")
    gm2: NmhGm2 = NmhGm2.from_file(in_path)

    with open(out_path, "r+b") as f:

        for obj in gm2.world_objects:
            f.seek(obj.off + 96)
            f.write(struct.pack("<f", 0))
            f.write(struct.pack("<f", 0))
            f.write(struct.pack("<f", 200))

            f.seek(obj.off + 112)
            f.write(struct.pack("<f", 0.01))
            f.write(struct.pack("<f", 0.01))
            f.write(struct.pack("<f", 0.01))

        """ Geometry """
        # for obj in gm2.world_objects:
        #     if obj.surfaces == None:
        #         continue
        #     f.seek(obj.off_i_buf)
        #     for _ in range(obj.surfaces[0].num_i):
        #         f.write(random.randbytes(6))

        """ Materials """
        # for mat in gm2.materials:
        #    f.seek(mat.off_data)
        #    f.write(struct.pack("<i", 0x0F0))
        #    # f.seek(mat.off_data + 8 + 16)
        #    # f.write(struct.pack("<f", random.random()))
        #    # f.write(struct.pack("<f", random.random()))
        #    # f.write(struct.pack("<f", random.random()))
        #    # f.write(struct.pack("<f", random.random()))

    print("mangling: done!\n")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        reset_files()

        in_file = os.path.join(DIR, sys.argv[1])
        out_file = os.path.join(OUT_DIR, sys.argv[1])
        mangle(in_file, out_file)
    else:
        print("Provide 1 arg, which is the filename.")
