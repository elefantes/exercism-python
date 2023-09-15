def classify(number):
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    summation = sum_divisors(number)

    if summation == number:
        result = "perfect"
    elif summation > number:
        result = "abundant"
    else:
        result = "deficient"

    return result


def sum_divisors(number: int) -> int:
    sum = 0
    for d in range(1, number):
        if number % d == 0:
            sum += d
    return sum
