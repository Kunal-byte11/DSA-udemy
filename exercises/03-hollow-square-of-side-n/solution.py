"""
03: Hollow Square of side 'N'

Problem:
Return a hollow square pattern of size n x n made up of '*', represented as a list of strings.
Border has '*', middle has spaces ' '.
"""

from typing import List


def generate_hollow_square_grid(n: int) -> List[str]:
    """
    Approach 1: Kunal's 2D Grid Coordinate Concept
    Check every cell (i, j):
    If on any boundary (i == 0 or i == n - 1 or j == 0 or j == n - 1) -> '*'
    Otherwise (inside the square) -> ' '
    """
    if n <= 0:
        return []

    result = []
    for i in range(n):
        row_chars = []
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                row_chars.append("*")
            else:
                row_chars.append(" ")
        result.append("".join(row_chars))
    return result


def generate_hollow_square(n: int) -> List[str]:
    """
    Approach 2: Pythonic Row-Level Optimization
    Constructs entire rows directly using string multiplication.
    """
    if n <= 0:
        return []
    if n == 1:
        return ["*"]

    result = []
    for i in range(n):
        if i == 0 or i == n - 1:
            result.append("*" * n)
        else:
            result.append("*" + " " * (n - 2) + "*")
    return result


if __name__ == "__main__":
    test_cases = [
        (3, ["***", "* *", "***"]),
        (5, ["*****", "*   *", "*   *", "*   *", "*****"]),
        (2, ["**", "**"]),
        (1, ["*"]),
        (0, []),
    ]

    print("--- Testing Approach 1 (Kunal's 2D Coordinate Concept) ---")
    for n_val, expected in test_cases:
        actual = generate_hollow_square_grid(n_val)
        assert actual == expected, f"Failed for n={n_val}. Expected {expected}, got {actual}"
        print(f"✅ n={n_val} Passed: {actual}")

    print("\n--- Testing Approach 2 (Row-Level Shortcut) ---")
    for n_val, expected in test_cases:
        actual = generate_hollow_square(n_val)
        assert actual == expected, f"Failed for n={n_val}. Expected {expected}, got {actual}"
        print(f"✅ n={n_val} Passed: {actual}")

    print("\n🎉 All test cases passed successfully for both approaches!")
