import string


def is_pangram(sentence):
    characters = {char.lower() for char in sentence if char in string.ascii_letters}
    return len(characters) == len(string.ascii_lowercase)
