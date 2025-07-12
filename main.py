from stats import get_words
from stats import get_letters
from stats import get_sort

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents


def main():
    total_words = get_words("books/frankenstein.txt")
    total_count = get_letters("books/frankenstein.txt")
    list_dict = get_sort(total_count)
    print("============ BOOKBOT ============\n"
"Analyzing book found at books/frankenstein.txt...\n"
"----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for i in list_dict:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")
    
    
main()