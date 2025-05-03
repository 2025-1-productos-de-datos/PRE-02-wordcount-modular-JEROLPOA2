def split_into_words(lines: list[str]) -> list[str]:
    words = []
    for line in lines:
        for word in line.split():
            word = word.strip(",.!?")
            words.append(word)
    return words
