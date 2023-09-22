import string as String


def is_isogram(string):
    chars = [char.lower() for char in string if char in String.ascii_letters]
    unique_chars = set(chars)
    return len(chars) == len(unique_chars)
