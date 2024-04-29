import multiprocessing
from itertools import combinations, product
from pathlib import Path

from PIL import Image

from storage.filetype import filetype


class ImageHash:
    _cache = {}
    
    def __init__(self, size: int = 8):
        self.size = size

    def create(self, path: Path) -> hex:
        if path.stem in self._cache:
            return self._cache[path.stem]
        with Image.open(path) as image:
            image_hash = self.__hash(image)
        self._cache[path.stem] = image_hash
        return image_hash

    def __hash(self, image: Image) -> hex:
        image = image.resize((self.size + 1, self.size), Image.Resampling.BICUBIC).convert('L')
        difference = []
        pixels = image.load()
        for row, col in product(range(self.size), repeat=2):
            difference.append(1 if pixels[col, row] > pixels[col + 1, row] else 0)
        return hex(int(''.join(map(str, difference)), 2))[2:]


class Dupelicate:
    def __init__(self, threshold: int = 8, cores: int = 6):
        self.threshold = threshold
        self.cores = min(multiprocessing.cpu_count(), cores)
        self.__hash = ImageHash()

    def find(self, path: str | Path) -> set:
        with multiprocessing.Pool(processes=self.cores) as pool:
            results = pool.map(self.difference, combinations(Path(path).iterdir(), 2))
        return set(result for result in results if result)
            
    @staticmethod
    def distance(first: hex, second: hex) -> int:
        return sum(char != char2 for char, char2 in zip(first, second))

    def difference(self, files: tuple[Path:Path]) -> None | tuple:
        if any(file.is_dir() or filetype.is_video(file) for file in files):
            return
        distance = self.distance(self.__hash.create(files[0]), self.__hash.create(files[1]))
        if not distance <= self.threshold:
            return
        return distance, files[0].as_posix(), files[1].as_posix()
        

dupelicate = Dupelicate()
