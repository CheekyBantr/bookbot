import sys
from stats import word_count
from stats import letter_count
from stats import sorted_letter_count

def get_book_text(filepath):
    #take filepath as input and return string of file contents
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    num_words = word_count(get_book_text(sys.argv[1]))
    num_letters = letter_count(get_book_text(sys.argv[1]))
    num_letters_sorted = sorted_letter_count(letter_count(get_book_text(sys.argv[1])))
    print(f"Found {num_words} total words")
    for each_letter in num_letters_sorted:
        print(f"{each_letter["char"]}: {each_letter["num"]}")
main()