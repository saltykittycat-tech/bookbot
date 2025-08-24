def word_count(book_text):
    word_list = book_text.split()
    word_count = len(word_list)
    print(f"{word_count} words found in the document")
