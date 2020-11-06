from pathlib import Path
import os


def subHandle(path_dir):
    for root, dirs, files in os.walk(path_dir):
        if len(dirs) > 0:
            for file in files:
                if file != '__init__.py':
                    print(os.path.join(root, file))


def FileEach(BASE_DIR=Path(__file__).resolve().parent.parent):
    for root, dirs, files in os.walk(BASE_DIR):
        for dir in dirs:
            if dir == 'migrations':
                subHandle(os.path.join(root, dir))


if __name__ == '__main__':
    FileEach()
