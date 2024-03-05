import multiprocessing
from itertools import combinations
from pathlib import Path

from duplicate.hasher import ImageHash, distance
from filepath import FileType


class Duplicate:
    def __init__(self, folder: Path, threshold: int = 40, max_cores: int = 6):
        self.__folder = folder
        self.__threshold = threshold
        self.__cores = min(multiprocessing.cpu_count(), max_cores)

    def similar(self) -> None:
        with multiprocessing.Pool(processes=self.__cores) as pool:
            pool.map(self._process_difference, combinations(self.__folder.iterdir(), 2))

    def _process_difference(self, files: tuple[Path:Path]) -> None:
        if any(file.is_dir() for file in files) or any(FileType(file).is_photo() for file in files):
            return
        h1, h2 = ImageHash(files[0]).hash(), ImageHash(files[1]).hash()
        if not distance(h1, h2) < self.__threshold:
            return
        print(distance(h1, h2))
        print(', '.join(file for file in files))
