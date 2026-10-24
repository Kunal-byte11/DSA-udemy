# 02: Square of side 'N'

## 📝 Problem Description
You are given an integer `n`. Your task is to return a square pattern of size `n x n` made up of the character `'*'`, represented as a list of strings.

## 📥 Input Parameters
- `n` (`int`): The size of the square (number of rows and columns).

## 📤 Output
- A list of strings (`List[str]`), where each string is a row of `n` `'*'` characters.

## 📥 Examples

### Example 1
```text
Input: n = 3
Output: ['***', '***', '***']
```

### Example 2
```text
Input: n = 5
Output: ['*****', '*****', '*****', '*****', '*****']
```

## ⚙️ Constraints
- `n >= 0`

## 💡 Notes & Complexity
- **Time Complexity:** $O(n^2)$ - Creating $n$ rows, each with $n$ characters.
- **Space Complexity:** $O(n^2)$ - To store $n \times n$ characters in the output list.
