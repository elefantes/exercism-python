def convert(number):
    divisible_by_3 = number % 3 == 0
    divisible_by_5 = number % 5 == 0
    divisible_by_7 = number % 7 == 0
    not_divisible = not divisible_by_3 and not divisible_by_5 and not divisible_by_7
    result = []

    if divisible_by_3:
        result.append("Pling")
    if divisible_by_5:
        result.append("Plang")
    if divisible_by_7:
        result.append("Plong")
    if not_divisible:
        result.append(str(number))

    return "".join(result)
