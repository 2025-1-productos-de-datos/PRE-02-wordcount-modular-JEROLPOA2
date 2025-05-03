import os


def write_word_counts(output_dir:str, word_counts: dict[str, int]) -> None:
    
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "wordcount.tsv"), "w", encoding="utf-8") as f:
        for word, count in word_counts.items():
            f.write(f"{word}\t{count}\n")
