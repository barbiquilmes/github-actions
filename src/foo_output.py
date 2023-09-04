import os
import datetime
from settings import DATA_PATH

PATH_1 = os.path.join(DATA_PATH, "file1.txt")
PATH_2 = os.path.join(DATA_PATH, "file2.txt")


def create_output_file(path: str):
    with open(path, "w") as f:
        f.write(f"Hello World at {datetime.datetime.now()}!")


if __name__ == "__main__":
    create_output_file(PATH_1)
    create_output_file(PATH_2)
