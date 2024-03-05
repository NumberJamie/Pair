from itertools import product
from pathlib import Path

from PIL import Image


def distance(hex_one: str, hex_two: str) -> int:
    return sum(b1 != b2 for b1, b2 in zip(bin(int(hex_one, 16)), bin(int(hex_two, 16))))


class ImageHash:
    _cache = {}

    def __init__(self, image_path: Path, size: int = 24):
        self.__image = image_path
        self.__size = size

    def hash(self) -> str:
        if self.__image in self._cache:
            return self._cache[self.__image]
        with Image.open(self.__image) as image:
            image_hash = self.__hash(image)
        self._cache[self.__image] = image_hash
        return image_hash

    def __hash(self, image: Image) -> str:
        image = image.resize((self.__size + 1, self.__size), Image.BICUBIC).convert('L')
        difference = self.__difference(image)
        return hex(int(difference, 2))[2:]

    def __difference(self, image: Image) -> str:
        difference = []
        pixels = image.load()
        for row, col in product(range(self.__size), repeat=2):
            difference.append(1 if pixels[col, row] > pixels[col + 1, row] else 0)
        return ''.join(map(str, difference))
