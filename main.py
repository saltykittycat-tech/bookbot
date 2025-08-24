def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def word_count(filepath):
    book_text = get_book_text(filepath)
    word_list = book_text.split()
    word_count = len(word_list)
    print(f"{word_count} words found in the document")

word_count("books/frankenstein.txt")