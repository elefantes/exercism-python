def is_number(n):
    result = n.isdigit() if not n.startswith("-") else n[1::].isdigit()
    return result


def is_even(n):
    result = n % 2 == 0
    return result


def answer(question):
    operators = {"plus": "+", "minus": "-", "multiplied_by": "*", "divided_by": "/"}

    expr = (
        question.lower()
        .strip()
        .replace("multiplied by", "multiplied_by")
        .replace("divided by", "divided_by")
        .removeprefix("what is")
        .removesuffix("?")
        .split()
    )

    if (
        not question.lower().startswith("what is")
        or not question.lower().endswith("?")
        or not all(is_number(token) or token in operators.keys() for token in expr)
    ):
        raise ValueError("unknown operation")
    elif (
        len(expr) == 0
        or not is_number(expr[-1])
        or not all(
            (is_number(token) and is_even(idx))
            or (not is_number(token) and not is_even(idx) and token in operators.keys())
            for idx, token in enumerate(expr)
        )
    ):
        raise ValueError("syntax error")

    print(f"{question}\n{'-'*4}> {expr}")

    total_so_far = eval(expr[0])
    for idx, token in enumerate(expr):
        if token in operators.keys():
            operation = operators[token]
            next_operand = expr[idx + 1]
            subexpr = f"{total_so_far} {operation} {next_operand}"
            total_so_far = eval(subexpr)
    return total_so_far
