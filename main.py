import sys
from stats import get_word_count, get_character_count, analyse_char_count

def get_book_text(file_path):
    file_contents = None

    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def main():

    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_file_path = sys.argv[1]
    book_text = get_book_text(book_file_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(book_text)} total words")
    print("--------- Character Count -------")
    sorted_list = analyse_char_count(get_character_count(book_text))
    for dict in sorted_list:
        print(f"{dict["char"]}: {dict["count"]}")
    print("============= END ===============")

main()