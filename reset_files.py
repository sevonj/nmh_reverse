import shutil


def reset_files():
    """
    replaces ./filesystem_edited/ with a fresh copy.
    """

    shutil.rmtree("filesystem_edited", ignore_errors=True)
    shutil.copytree("filesystem", "filesystem_edited")


if __name__ == "__main__":
    reset_files()
