# %%


def translate(text: str) -> str:
    phrase = text.split(" ")
    translated = [translate_helper(word) for word in phrase]
    result = " ".join(translated)
    return result


def translate_helper(text: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    #  consonants = set(string.ascii_letters.lower()).difference(set(vowels))
    vowel_sounds = set(vowels + ["xr", "yt"])
    starts_with_vowel_sound = text.startswith(tuple(vowel_sounds))

    # [Rule 4] : Contains 'y' after consonant cluster
    #            OR end of 2-letter word ==> makes a vowel
    if len(text) == 2 and text[1] == "y":
        print("[Rule: 4]")
        result = text[1] + text[0] + "ay"

    elif (y_idx := text[1::].find("y") != -1) and not starts_with_vowel_sound:
        result = text[y_idx + 1 : :] + text[0 : y_idx + 1] + "ay"

    # [Rule 3] : Starts with consonant followed by 'qu' ==> Move to end and add 'ay'
    elif not starts_with_vowel_sound and text[1::].startswith("qu"):
        print("[Rule: 3a]")
        result = text[3::] + text[0:3] + "ay"

    elif text.startswith("qu"):
        print("[Rule: 3b]")
        result = text[2::] + text[0:2] + "ay"

    # [Rule 2] : Starts with consonant ==> Move to end and add 'ay'
    elif not starts_with_vowel_sound:
        print("[Rule: 2]")
        # Find next vowel index
        next_vowel = next(c for c in text if c in vowel_sounds)
        idx = text.find(next_vowel)
        result = text[idx::] + text[0:idx] + "ay"

    # [Rule 1] : Starts with a vowel sound ==> Add 'ay' to the end
    elif starts_with_vowel_sound:
        print("[Rule: 1]")
        result = text + "ay"

    return result
