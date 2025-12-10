import sys
def word_count(text):
    words = text.split()
    count = len(words)
    print(f"Found {count} total words")
    

def character_count(text):
    characters = {}
    text = text.lower()
    for char in text:
        if char not in characters:
            characters[char] = 1
        else: characters[char] += 1
    return characters

def sort_on(items):
    return items["num"]

def sort_characters(characters):
    dict_characters = []
    for key, value in characters.items():
        if key.isalpha():
            dict_pair = {"char":key, "num": value}
            dict_characters.append(dict_pair)
    dict_characters.sort(reverse=True, key=sort_on)
    print(sys.argv)
    return dict_characters



