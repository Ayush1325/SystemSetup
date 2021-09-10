import shutil
import os
from pathlib import Path


def create_direcories():
    home = Path.home()
    home_paths = ["Games", "Documents/Programming", "Documents/Harddrive", "Documents/Books",
                  "Documents/CollegeStuff", "Videos/Hollywood", "Videos/Lbry", "Pictures/Harddrive",
                  "Documents/Notes"]
    for i in home_paths:
        os.makedirs(os.path.join(home, i))


if __name__ == "__main__":
    create_direcories()
