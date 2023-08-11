from typing import Callable


def sum_multiples(n: int = 999):
    operand_three = n // 3
    operand_five = n // 5
    operand_fifteen = n // 15

    sum_formula: Callable[[int, int], int] = lambda x, y: x * y * (y + 1)

    return 0.5 * (
        sum_formula(3, operand_three)
        + sum_formula(5, operand_five)
        - sum_formula(15, operand_fifteen)
    )


if __name__ == "__main__":
    print(sum_multiples())
