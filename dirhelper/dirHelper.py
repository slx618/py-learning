import os


def check_dir(dir):
    try:
        return os.path.isdir(dir)
    except IsADirectoryError as e:
        print(e)
