"""
02: Square of side 'N'

Problem:
Return a square pattern of size n x n made up of '*', represented as a list of strings.
"""

from typing import List


def generate_square_loop(n: int) -> List[str]:
    """
    Approach 1: Using a standard for-loop.
    Easy to read and understand step-by-step.
    """
    result = []
    for _ in range(n):
        # In Python, '*' * n repeats the character n times
        row = '*' * n
        result.append(row)
    return result


def generate_square(n: int) -> List[str]:
    """
    Approach 2: Pythonic one-liner using List Comprehension.
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    """
    return ['*' * n for _ in range(n)]


if __name__ == "__main__":
    # Test Case 1: n = 3
    expected_3 = ['***', '***', '***']
    assert generate_square(3) == expected_3, f"Expected {expected_3}, got {generate_square(3)}"
    print("✅ Test Case 1 Passed (n = 3):", generate_square(3))

    # Test Case 2: n = 5
    expected_5 = ['*****', '*****', '*****', '*****', '*****']
    assert generate_square(5) == expected_5, f"Expected {expected_5}, got {generate_square(5)}"
    print("✅ Test Case 2 Passed (n = 5):", generate_square(5))

    # Test Case 3: n = 1 (edge case)
    expected_1 = ['*']
    assert generate_square(1) == expected_1, f"Expected {expected_1}, got {generate_square(1)}"
    print("✅ Test Case 3 Passed (n = 1):", generate_square(1))

    # Test Case 4: n = 0 (edge case)
    expected_0 = []
    assert generate_square(0) == expected_0, f"Expected {expected_0}, got {generate_square(0)}"
    print("✅ Test Case 4 Passed (n = 0):", generate_square(0))

    print("\n🎉 All test cases passed successfully!")
