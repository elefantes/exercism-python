def response(hey_bob):
    if hey_bob.strip().endswith('?') and hey_bob.strip().isupper():
        result = "Calm down, I know what I'm doing!"
    elif hey_bob.strip().endswith('?'):
        result = "Sure."
    elif hey_bob.strip().isupper() :
        result = "Whoa, chill out!"
    elif len(hey_bob.strip()) == 0:
        result = "Fine. Be that way!"
    else:
        result = "Whatever."
    return result
