from stats import word_count
from stats import get_character_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

book_text = get_book_text("books/frankenstein.txt")
character_count = get_character_count(book_text)

word_count(book_text)
print(character_count)