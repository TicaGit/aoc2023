from pathlib import Path


def read_input(path: Path):
    with open(path, "r") as f:
        return f.readlines()
