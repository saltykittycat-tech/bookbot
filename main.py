def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main(relative_file_path):
    book_text = get_book_text(relative_file_path)
    print (book_text)

main("books/frankenstein.txt")
