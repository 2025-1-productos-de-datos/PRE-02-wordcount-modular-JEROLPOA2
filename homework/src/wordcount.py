import sys

from ._internals.count_words import count_words
from ._internals.preprocess_lines import preprocess_lines
from ._internals.read_all_lines import read_all_lines
from ._internals.split_into_words import split_into_words
from ._internals.write_word_counts import write_word_counts


def main():
    
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    lines = read_all_lines(input_dir)
    preprocessed = preprocess_lines(lines)
    words = split_into_words(preprocessed)
    word_counts = count_words(words)
    write_word_counts(output_dir, word_counts)

if __name__ == "__main__":
    main()
