#this is a bookbot program that pulls ever character and
#counts how times they occur
import sys

from stats import get_words
from stats import get_letters
from stats import get_sort


def main():
    
    if len(sys.argv) < 2:
        print("Usage: must include python3 main.py <path_to_book>")
        sys.exit(1)
    
    total_words = get_words(sys.argv[1])
    total_count = get_letters(sys.argv[1])
    list_dict = get_sort(total_count)

    print(f"============ BOOKBOT ============\n"
f"Analyzing book found at {sys.argv[1]}...\n"
"----------- Word Count ----------")
    
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")

# looping to print list of chracters
    for i in list_dict:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

    
main()