from typing import List, Tuple

def read_data(file_path: str) -> List[Tuple[str, int]]:
    """
    Reads a file where each line is "Name,Age" and returns a list of (name, age).
    Ignores empty lines and strips whitespace. Raises ValueError for invalid lines.
    """
    results = []
    with open(file_path, "r", encoding="utf-8") as f:
        for lineno, raw in enumerate(f, start=1):
            line = raw.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 2:
                raise ValueError(f"Invalid format on line {lineno}: {raw!r}")
            name = parts[0].strip()
            age_str = parts[1].strip()
            try:
                age = int(age_str)
            except ValueError:
                raise ValueError(f"Invalid age on line {lineno}: {age_str!r}")
            results.append((name, age))
    return results
