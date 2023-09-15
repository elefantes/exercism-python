def score(x, y):
    inner_radius = 1
    middle_radius = 5
    outer_radius = 10

    x2 = x**2
    y2 = y**2
    sum_x2_y2 = x2 + y2

    if sum_x2_y2 <= inner_radius**2:
        score = 10
    elif sum_x2_y2 <= middle_radius**2:
        score = 5
    elif sum_x2_y2 <= outer_radius**2:
        score = 1
    else:
        score = 0

    return score
