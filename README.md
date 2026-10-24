# Udemy DSA Exercises & Solutions

A structured repository tracking Python Data Structures and Algorithms exercises from Udemy, pairing problem statements with clean solutions.

---

## 📁 Repository Structure

```text
udemy-pyqs/
├── exercises/
│   ├── 01-exercise-title/
│   │   ├── README.md       # Problem statement, examples, constraints
│   │   └── solution.py     # Python solution with comments & test cases
│   └── ...
├── new_exercise.py         # Helper script to create a new exercise folder
├── push.sh                 # One-command script to commit & push to GitHub
└── README.md
```

---

## 🚀 Workflow

### 1. Create a New Exercise
To start working on an exercise from Udemy, run:
```bash
python3 new_exercise.py "Exercise Title"
```
Or specify a section/number prefix:
```bash
python3 new_exercise.py "01" "Two Sum"
```
This generates:
- `exercises/<title>/README.md`: Problem template with sections for Problem Statement, Constraints, and Examples.
- `exercises/<title>/solution.py`: Starter Python file ready for your code.

### 2. Solve & Save
- Paste or summarize the Udemy problem prompt in `exercises/<title>/README.md`.
- Write and test your solution in `exercises/<title>/solution.py`.

### 3. Push to GitHub with One Command
Once you're satisfied with your solution, push it to GitHub:
```bash
./push.sh "Solved 01 Two Sum"
```
If you omit the message, it will prompt you or use an automatic timestamp:
```bash
./push.sh
```
