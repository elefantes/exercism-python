def rotate(text: str, key: int) -> str:
    result = []

    for character in text.strip():
        ordinal = ord(character)
        rotated_ordinal = ordinal  # No nothing by default

        if character.islower():
            rotated_ordinal = (((ordinal - ord("a")) + key) % 26) + ord("a")
        elif character.isupper():
            rotated_ordinal = (((ordinal - ord("A")) + key) % 26) + ord("A")

        rotated_character = chr(rotated_ordinal)
        result.append(rotated_character)

    return "".join(result)
