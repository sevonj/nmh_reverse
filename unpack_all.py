import os
import shutil
import unpack_flcg
import unpack_gmf2
from glob import glob

TOOL_NAME = "Jyl's FLCG exporter"

GAMEPATH = "filesystem/DATA/files"
OUTPATH = "out"


def unpack_all(in_dir: str, out_dir: str):
    # rm old files
    shutil.rmtree(out_dir, ignore_errors=True)

    # out dir exists
    os.makedirs(out_dir, exist_ok=True)

    # Walk the entire game dir
    for root, _, files in os.walk(in_dir):
        for filename in files:

            inputfile = os.path.join(root, filename)
            relpath = os.path.relpath(inputfile, in_dir)
            outputdir = os.path.join(out_dir, relpath)

            magic = None
            with open(inputfile, "rb") as f:
                magic = f.read(4)

            # -- Decide what to do with the file

            if filename.lower().endswith(".txt"):
                continue

            if filename.lower().endswith(".bat"):
                continue

            if filename.lower().endswith(".tga"):
                continue

            if filename.lower().endswith(".rsid"):
                continue

            match magic:

                case b"FLCG":
                    os.makedirs(outputdir)
                    try:
                        unpack_flcg.unpack(inputfile, outputdir)
                    except Exception as e:
                        print(f"FAILED - {inputfile}")
                        log_error(e, outputdir)

                case b"GAN2":
                    pass

                case b"GCT0":
                    pass

                case b"GMF2":
                    try:
                        unpack_gmf2.unpack(inputfile, outputdir)
                    except Exception as e:
                        print(f"FAILED - {inputfile}")
                        log_error(e, outputdir)

                case b"RMHG":
                    pass

                case b"RSAR":
                    pass

                case b"RSTM":
                    pass

                case b"SEST":
                    pass

                case b"STMD":
                    pass

                case b"STSD":
                    pass

                case b"STRI":  # STRIMAG2
                    pass

                case b"THP\x00":
                    pass

                case _:
                    print(f"unknown id: {magic} - {inputfile}")


def log_error(e: Exception, outputdir: str):
    with open(os.path.join(outputdir, "_error_log.txt"), "w") as error_log:
        error_log.write(f"--- I HAVE FAILED ---\n\nException:\n")
        error_log.write(f"{e}")


if __name__ == "__main__":
    unpack_all(GAMEPATH, OUTPATH)
