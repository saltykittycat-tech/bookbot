from stats import word_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

book_text = get_book_text("books/frankenstein.txt")

word_count(book_text)