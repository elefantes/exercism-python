def equilateral(sides):
    a, b, c = sides
    return is_triangle(sides) and a == b and b == c


def isosceles(sides):
    a, b, c = sides
    return is_triangle(sides) and (a == b or b == c or c == a)


def scalene(sides):
    a, b, c = sides
    return is_triangle(sides) and a != b and a != c and b != c


def is_triangle(sides):
    a, b, c = sides
    return a + b >= c and b + c >= a and c + a >= b and a > 0 and b > 0 and c > 0
