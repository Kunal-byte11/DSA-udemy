# 03: Hollow Square of side 'N'

## 📝 Problem Description
You are given an integer `n`. Your task is to return a hollow square pattern of size `n x n` made up of the character `'*'`, represented as a list of strings. 

The hollow square has `'*'` on the border, and spaces `' '` in the middle (except for side lengths of 1 and 2).

## 📥 Input Parameters
- `n` (`int`): The size of the square (number of rows and columns).

## 📤 Output
- A list of strings (`List[str]`), where each string is a row of `n` characters representing a hollow square.

## 📥 Examples

### Example 1
```text
Input: n = 3
Output: ['***', '* *', '***']
```

### Example 2
```text
Input: n = 5
Output: ['*****', '*   *', '*   *', '*   *', '*****']
```

## ⚙️ Constraints
- `n >= 0`

## 💡 Notes & Complexity
- **Time Complexity:** $O(n^2)$ - We inspect or generate $n \times n$ total cells.
- **Space Complexity:** $O(n^2)$ - To store the output list of strings.
