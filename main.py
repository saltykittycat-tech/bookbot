from stats import word_count
from stats import get_character_count
from stats import dictionary_to_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



book_path = sys.argv[1]
book_text = get_book_text(book_path)
character_count = get_character_count(book_text)
character_list = dictionary_to_list(character_count)
print("=============== BOOKBOT ===============")
print(f"Analyzing book found at {book_path}")
print("---------- Word Count ---------")
word_count(book_text)
print("----------- Character Count ------------")
for i in character_list:
    if i["char"].isalpha():
        print(f"{i["char"]}: {i["amount"]}")
print("================ END =============")