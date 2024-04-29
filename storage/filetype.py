import mimetypes
from pathlib import Path


class FileType:
    @staticmethod
    def __guess_type(path: str | Path) -> tuple[str:str]:
        variant, _ = mimetypes.guess_type(path, False)
        return variant.split('/') if variant else (None, None)

    def is_photo(self, path: str | Path) -> bool:
        category, _ = self.__guess_type(path)
        return category == 'image' if category else False

    def is_video(self, path: str | Path) -> bool:
        category, _ = self.__guess_type(path)
        return category == 'video' if category else False


filetype = FileType()
