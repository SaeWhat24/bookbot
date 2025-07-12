def get_words(file):
    num_words = 0
    with open(file) as f:
        words = f.read()
        words_split = words.split()
        for word in words_split:
            num_words += 1
        return num_words

def get_letters(file):
    letter_count = {}
    with open(file) as f:
        words = f.read()
        lower_words = words.lower()
        for char in lower_words:
            if char not in letter_count:
                letter_count[char] = 1
            else:
                letter_count[char] += 1
        return letter_count
    
def get_sort(a):
    list_of_dict = []
    none_alpha = []
    for char, num in a.items():
        if char.isalpha():
            new_entry = {"char": char, "num": num}
            list_of_dict.append(new_entry)
    list_of_dict.sort(reverse=True, key=sort_by)
        
    return list_of_dict

def sort_by(items):
    return items["num"]

