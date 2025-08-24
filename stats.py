def word_count(book_text):
    word_list = book_text.split()
    word_count = len(word_list)
    print(f"Found {word_count} total words")

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

def sort_on(items):
    return items["amount"]

def dictionary_to_list(character_count):
    list = []
    for key in character_count:
        char = key
        amount = character_count[key]
        char_dictionary = {"char":char, "amount":amount}
        list.append(char_dictionary)
    list.sort(reverse=True, key=sort_on)
    return list