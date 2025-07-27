from stats import word_count
from stats import letter_count

def get_book_text(filepath):
    #take filepath as input and return string of file contents
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    num_words = word_count(get_book_text("books/frankenstein.txt"))
    num_letters = letter_count(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")
    print(num_letters)
    
main()