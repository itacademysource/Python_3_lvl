def calculate(expression):
    """Performs 1 mathematical operation on two values

    :param expression: expression
    :return: result
    """
    allowed = ('+', '-', '*', '/')
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'Выражение должно содержать арифметический знак {"".join(allowed)}')

    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)

                results = {
                    '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b,
                    '*': lambda a, b: a * b,
                    '/': lambda a, b: a / b,
                }
                return results[sign](left, right)
            except (ValueError, TypeError):
                raise ValueError('Выражение должно содержать только 2 целых числа и 1 знак')


if __name__ == '__main__':
    print(calculate('2 * 5'))
