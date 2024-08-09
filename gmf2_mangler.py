import os
import random
from lib.kaitai_defs.gmf2 import Gmf2
from glob import glob
import struct
import sys
from lib.reset_files import reset_files

TOOL_NAME = "Jyl's GMF2 Mangler"

DIR = "filesystem/DATA/files/STG_HI"
OUT_DIR = "filesystem_edited/DATA/files/STG_HI"


def mangle(in_path: str, out_path: str):
    print(f"mangling: {in_path}...")
    gm2: Gmf2 = Gmf2.from_file(in_path)

    with open(out_path, "r+b") as f:

        for i, obj in enumerate(gm2.world_objects):
            if obj.surfaces == None:
                continue

            print(f"obj[{i}]-{obj.name}")

            # -- Object flags
            # f.seek(obj.off + 8)
            # f.write(struct.pack("<I", 0b0000_1111_0000_0000_0000_0000_1001))

            if obj.data_c != None:
                continue

            for ii, surf in enumerate(obj.surfaces):
                print(f"    surf[{ii}] - {hex(surf.data.unk_2)}")

                # -- Destroy surf data
                if True:
                    if surf.off_next != 0:
                        f.seek(surf.off_next + 0x1A)
                        f.write(random.randbytes(2))
                        # f.seek(2, 1)
                        # f.write(random.randbytes(12))

                    if surf.off_prev == obj.off_surf_list:
                        f.seek(surf.off_prev + 0x1A)
                        f.write(random.randbytes(2))
                        # f.seek(2, 1)
                        # f.write(random.randbytes(12))

                if False:
                    f.seek(surf.off_data + 6)
                    f.write(random.randbytes(2))

                # -- Destroy Vertex Data
                if False:
                    f.seek(surf.off_data + 32)

                    i_remaining = surf.data.num_v_smthn_total
                    while i_remaining > 0:
                        unk_0 = struct.unpack(">H", f.read(2))[0]

                        # Unknown format guard
                        if unk_0 != 0x99:
                            print(f"unk_0 == {hex(unk_0)}", end="    ")
                            print(f"obj[{i}]", end="    ")
                            print(f"surf[{ii}]")
                            break

                        num_idx = struct.unpack(">H", f.read(2))[0]
                        for _ in range(num_idx):

                            # 9B: iinnnuuuu

                            _idx = struct.unpack(">H", f.read(2))[0]

                            f.read(3)  # Normals

                            # Flip uv
                            if False:
                                u = struct.unpack(">h", f.read(2))[0]
                                v = struct.unpack(">h", f.read(2))[0]
                                f.seek(-4, 1)
                                f.write(struct.pack(">h", -u))
                                f.write(struct.pack(">h", -v))

                            if False:
                                f.read(1)
                                f.write(b"\x00")
                                f.read(1)
                                f.write(b"\x00")

                            if True:
                                f.write(struct.pack(">h", -1))
                                f.write(struct.pack(">h", -1))

                            # f.write(random.randbytes(1))

                            # _v_normal = f.read(3)

                            # Vertex Color
                            # f.read(2)
                            # f.write(struct.pack(">H", 0xFFF0))

                            # UV
                            # _u = struct.unpack(">h", f.read(2))[0]
                            # _v = struct.unpack(">h", f.read(2))[0]

                        i_remaining -= num_idx
            print("")

        # for obj in gm2.world_objects:
        #    f.seek(obj.off + 96)
        #    f.write(struct.pack("<f", 0))
        #    f.write(struct.pack("<f", 0))
        #    f.write(struct.pack("<f", 200))
        #
        #    f.seek(obj.off + 112)
        #    f.write(struct.pack("<f", 0.01))
        #    f.write(struct.pack("<f", 0.01))
        #    f.write(struct.pack("<f", 0.01))

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
