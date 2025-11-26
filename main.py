from pathlib import Path
from stats import count_words, count_letters, sort_dictionary
import sys


def read_file(file: Path):
    with open(file, "r", encoding="utf-8") as file:
        content = file.read()
    return content

def print_report(file: Path):

    content = read_file(Path(file))
    count_dict = count_letters(content)
    sorted_count = sort_dictionary(count_dict)

    num_words = count_words(content)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {str(file)}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count ------- ")
    for key, value in sorted_count.items():
        if key.isalpha():
            print(f"{key}: {value}")


if __name__=="__main__":
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")

    book = sys.argv[1]
    print_report(Path(book))