def is_armstrong_number(number):
    digits = number.__repr__()
    num_digits = len(digits)

    sum = 0
    for d in digits:
        sum += int(d) ** num_digits

    return sum == number
