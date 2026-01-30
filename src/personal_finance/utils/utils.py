from dataclasses import asdict
import json
from pathlib import Path


class StrMixin:
    def __str__(self) -> str:
        return json.dumps(asdict(self), indent=4)


def find_files_in_dir(directory: Path, ext: str) -> list[Path]:
    if not ext.startswith("."):
        raise ValueError("Extension must start with a dot (e.g., '.csv')")

    files_in_dir = [file for file in directory.expanduser().rglob(f"*{ext}") if file.is_file()]

    return files_in_dir
