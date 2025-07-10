from stats import get_words
from stats import get_letters

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents


def main():
    total_words = get_words("books/frankenstein.txt")
    total_count = get_letters("books/frankenstein.txt")
    print (total_words)
    print (total_count)
    
main()