import string


def is_valid(isbn):
    isbn_filtered = isbn.lower().replace("-", "").strip()

    if not (
        len(isbn_filtered) == 10  # correct length
        and all(d in string.digits for d in isbn_filtered[0:-2])  # all 0-9 digits
        and isbn_filtered[-1] in "x" + string.digits  # valid last char (check-digit)
    ):
        return False

    integers = [int(i) if i in string.digits else 10 for i in isbn_filtered]

    sum = summation(integers)

    return sum % 11 == 0


def summation(digits):
    sum = 0
    multiplier = 10
    for digit in digits:
        product = digit * multiplier
        sum += product
        multiplier -= 1
    return sum
