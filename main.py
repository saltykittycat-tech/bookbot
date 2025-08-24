from stats import word_count
from stats import get_character_count
from stats import dictionary_to_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

book_text = get_book_text("books/frankenstein.txt")
character_count = get_character_count(book_text)
character_list = dictionary_to_list(character_count)
print("=============== BOOKBOT ===============")
print("Analyzing book found at books/frankenstein.txt")
print("---------- Word Count ---------")
word_count(book_text)
print("----------- Character Count ------------")
for i in character_list:
    if i["char"].isalpha():
        print(f"{i["char"]}: {i["amount"]}")
print("================ END =============")