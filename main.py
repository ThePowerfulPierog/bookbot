def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    counter = word_count(text)
    letters = char_count(text)
    dict_list = sort_dict(letters)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{counter} words found in the document")
    #print(dict_list)
    print()
    for i in range(0,len(dict_list)):
        print(f"the '{dict_list[i]['name']}' character was found {dict_list[i]['num']} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count

def sort_on(dict):
    return dict["num"]

def sort_dict(dict_in):
    list_of_dict = []
    for dic in dict_in:
        temp_dict = {"name": dic, "num": dict_in[dic]}
        list_of_dict.append(temp_dict)
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict


def char_count(text):
    letters_dict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }
    lowered_text = text.lower()
    for word in lowered_text:
        characters = word.split()
        for char in characters:
            if char in letters_dict:
                letters_dict[char] += 1
    return letters_dict


main()