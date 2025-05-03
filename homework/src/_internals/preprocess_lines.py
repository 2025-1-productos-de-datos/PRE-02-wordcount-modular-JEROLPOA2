def preprocess_lines(lines: list[str]) -> list[str]:
    return [line.strip().lower() for line in lines]
