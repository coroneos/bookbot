def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for item in chars_sorted_list:
        if item["char"].isalpha():
            print(f"The '{item["char"]}' character was found {item["num"]} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = text.lower()
    char_dict = {}
    for c in chars:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for c in num_chars_dict:
        sorted_list.append({ "char": c, "num": num_chars_dict[c] })
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["num"]

main()
