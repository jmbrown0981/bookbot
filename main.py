import sys
from stats import (get_num_words,
                   get_character_count,
                   character_report,)

def usage():
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as fh:
        file_contents = fh.read()
    return file_contents

def main(file):
    book_text = get_book_text(file)
    word_count = get_num_words(book_text)
    char_dict = get_character_count(book_text)
    sorted_list = character_report(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        for key, value in dict.items():
            print(f"{key}: {value}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()

    book = sys.argv[1]
    main(book)