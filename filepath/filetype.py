import mimetypes
from pathlib import Path


class FileType:
    def __init__(self, path: Path):
        self._path = path
        mimetypes.add_type('image/webp', '.webp')

    def _guess(self) -> tuple[str:str]:
        variant, _ = mimetypes.guess_type(self._path)
        return variant.split('/') if variant else (None, None)

    def is_web(self) -> bool:
        _, t = self._guess()
        return t.startswith('web') if t else False

    def is_photo(self) -> bool:
        t, _ = self._guess()
        return t == 'image' if t else False

    def is_video(self) -> bool:
        t, _ = self._guess()
        return t == 'video' if t else False
