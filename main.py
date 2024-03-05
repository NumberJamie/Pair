from pathlib import Path

from duplicate import Duplicate

if __name__ == '__main__':
    folder = Path('path/to/your/folder')
    Duplicate(folder).similar()
