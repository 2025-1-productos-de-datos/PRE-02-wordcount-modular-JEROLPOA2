import os


def read_all_lines(input_dir:str) -> list[str]:
    
    lines = []
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            lines.extend(f.readlines())
    return lines
