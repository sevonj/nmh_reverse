import os
import shutil
import unpack_flcg
import unpack_gmf2
from glob import glob

TOOL_NAME = "Jyl's FLCG exporter"

DIR = "filesystem/DATA/files/STG_HI"
OUT_DIR = "out/STG_HI"


def unpack_all(dir: str, out_dir: str):
    # out dir exists
    os.makedirs(out_dir, exist_ok=True)

    # rm old files
    shutil.rmtree(OUT_DIR, ignore_errors=True)

    # convert all
    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        subdir = os.path.join(out_dir, file)

        magic = None
        with open(path, "rb") as f:
            magic = f.read(4)

        if file.lower().endswith(".txt"):
            print(f"Skipped text file {path}")
            continue

        match magic:
            case b"FLCG":
                os.makedirs(subdir)
                try:
                    unpack_flcg.unpack(path, subdir)
                except:
                    print(f"FAILED - {path}")

            case b"GMF2":
                try:
                    unpack_gmf2.unpack(path, subdir)
                except:
                    print(f"FAILED - {path}")

            case _:
                print(f"unknown id: {magic} - {path}")


if __name__ == "__main__":
    unpack_all(DIR, OUT_DIR)
