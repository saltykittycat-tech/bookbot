def word_count(book_text):
    word_list = book_text.split()
    word_count = len(word_list)
    print(f"{word_count} words found in the document")

def get_character_count(book_text):
    character_count={}
    for character in book_text:
        character = character.lower()
        if character in character_count:
            character_amount = character_count[character]
            character_amount += 1
            character_count[character] = character_amount
        else:
            character_count[character] = 1
    return character_count
