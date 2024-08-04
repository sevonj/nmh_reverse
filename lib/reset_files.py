import shutil


def reset_files():
    """
    replaces ./filesystem_edited/ with a fresh copy.
    """
    print("reset: rmtree")
    shutil.rmtree("filesystem_edited", ignore_errors=True)

    print("reset: copytree")
    shutil.copytree("filesystem", "filesystem_edited")

    print("reset: done!\n")


if __name__ == "__main__":
    reset_files()
