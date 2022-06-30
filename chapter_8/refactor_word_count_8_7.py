"""
LAB 8: REFACTOR WORD_COUNT
Rewrite the word-count program from section 8.7 to make it shorter.
You may want to look at the string and list operations
already discussed, as well as think about different ways to organize the code.
You may also want to make the program smarter so that only alphabetic
strings (not symbols or punctuation) count as words.
"""

import pathlib


def find_words(compare_to: str, words: dict[str, int]) -> None:
    """Print all the words which have the same number of repeats to the one provided to us"""
    for word, count in words.items():
        if count == words[compare_to]:
            print(f"*** {word} repeated {count} times")


def main():
    """Start of the application"""
    file_name = "moby_01_clean.txt"

    # Get the path to the file
    dir_path = pathlib.Path(__file__).parent.parent / "chapter_6" / file_name

    words: dict[str, int] = {}

    # Open the file
    with open(dir_path, "r", encoding="utf-8") as file:
        # Read the file
        for line in file:
            # Split the line into word
            word = line.strip()
            # this is the same as the following but pylance has a problem with it on lines 33 and 34
            words[word] = words.setdefault(word, 0) + 1
            # if word in words:
            #     words[word] += 1
            # else:
            #     words[word] = 1

    # Print the most and least common word
    most_common: str = max(words, key=words.get)  # type: ignore
    least_common: str = min(words, key=words.get)  # type: ignore

    # how many words did we have that repeated the most
    find_words(most_common, words)

    # how many words did we have that repeated the least
    find_words(least_common, words)

    print(
        f"Most common word: {most_common}, with {words[most_common]} repeats."
    )
    print(
        f"Least common word: {least_common}, with {words[least_common]} repeats."
    )


if __name__ == "__main__":
    main()
