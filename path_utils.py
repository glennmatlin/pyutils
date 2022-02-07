from pathlib import Path
from typing import List


def ls(source_path: Path, recursive=False) -> List[Path]:
    results = []
    if recursive:
        paths = Path(source_path).glob('**/*')
    else:
        paths = Path(source_path).iterdir()
    for path in paths:
        if path.is_file():
            results.append(path)
    return results
