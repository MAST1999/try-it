"""
LAB 6: PREPROCESSING TEXT In processing raw text, it’s quite often necessary
to clean and normalize the text before doing anything else. If you want to
find the frequency of words in text, for example, you can make the job easier
if, before you start counting, you make sure that everything is lowercase (or
uppercase, if you prefer) and that all punctuation has been removed. You can
also make things easier by breaking the text into a series of words. In this lab,
the task is to read the first part of the first chapter of Moby Dick (found in the
book's source code), make sure that everything is one case, remove all punctuation, and
write the words one per line to a second file. Because I haven’t
yet covered reading and writing files, here’s the code for those operations:
"""
import pathlib
import string


def main():
    """This is the start of the application"""
    file_name = "moby_01.txt"
    file_name2 = "moby_01_clean.txt"
    # file path for the file_name file
    dir_path = pathlib.Path(pathlib.Path(__file__).parent) / file_name
    dir_path2 = pathlib.Path(pathlib.Path(__file__).parent) / file_name2

    removing_punctuation_translation = str.maketrans(
        string.punctuation, " " * len(string.punctuation)
    )

    with open(dir_path, encoding="utf-8") as infile, open(
        dir_path2, "w", encoding="utf-8"
    ) as outfile:
        for line in infile:
            # make all one case
            line = line.lower()
            # remove punctuation
            line = line.translate(removing_punctuation_translation)
            # split into words
            cleaned_words = line.split()
            # write all words for line
            for word in cleaned_words:
                outfile.write(word + "\n")


if __name__ == "__main__":
    main()
