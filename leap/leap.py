def leap_year(year):
    divisible_by_4 = year % 4 == 0
    divisible_by_100 = year % 100 == 0
    divisible_by_400 = year % 400 == 0

    result = False

    if divisible_by_4:
        result = True
        if divisible_by_100:
            result = False
            if divisible_by_400:
                result = True

    return result
