def get_word_count(book_text):
    return len(book_text.split())

def get_character_count(book_text):
    character_count = {}
    for character in book_text:
        character = character.lower()
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def sort_character_count(character_count):
    def get_num(dict_item):
        return dict_item["num"]
    
    char_list = []
    for char, count in character_count.items():
        char_list.append({"char": char, "num": count})
    
    char_list.sort(key=get_num, reverse=True)
    return char_list