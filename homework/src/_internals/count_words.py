def count_words(words: list[str]) -> dict[str, int]:
    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1
    return counter
