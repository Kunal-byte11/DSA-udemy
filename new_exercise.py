#!/usr/bin/env python3
import sys
import re
from pathlib import Path

def slugify(text: str) -> str:
    """Convert text to a clean URL-friendly slug."""
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text.strip("-")

def create_exercise(title: str, prefix: str = "", problem_text: str = ""):
    base_dir = Path(__file__).resolve().parent / "exercises"
    
    slug = slugify(title)
    if prefix:
        folder_name = f"{slugify(prefix)}-{slug}"
    else:
        folder_name = slug

    exercise_dir = base_dir / folder_name
    exercise_dir.mkdir(parents=True, exist_ok=True)

    readme_path = exercise_dir / "README.md"
    solution_path = exercise_dir / "solution.py"

    full_title = f"{prefix + ': ' if prefix else ''}{title}"

    # Generate README.md
    if not readme_path.exists():
        statement_content = problem_text.strip() if problem_text else "<!-- Paste or type the problem description from Udemy here -->"
        readme_content = f"""# {full_title}

## 📝 Problem Statement
{statement_content}

## 📥 Example
```text
Input: 
Output: 
Explanation: 
```

## ⚙️ Constraints
- 

## 💡 Notes & Complexity
- **Time Complexity:** $O()$
- **Space Complexity:** $O()$
"""
        readme_path.write_text(readme_content, encoding="utf-8")
        print(f"✅ Created: {readme_path}")
    else:
        print(f"ℹ️  Already exists: {readme_path}")

    # Generate solution.py
    if not solution_path.exists():
        solution_content = f'''"""
{full_title}

Solution implementation and test cases.
"""

def solution():
    # TODO: Implement your solution here
    pass


if __name__ == "__main__":
    # Test cases
    print("Testing solution...")
'''
        solution_path.write_text(solution_content, encoding="utf-8")
        print(f"✅ Created: {solution_path}")
    else:
        print(f"ℹ️  Already exists: {solution_path}")

    print(f"\n🎉 Exercise initialized at: exercises/{folder_name}/")
    print(f"👉 Edit problem:   exercises/{folder_name}/README.md")
    print(f"👉 Write solution: exercises/{folder_name}/solution.py")


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        # Interactive mode
        print("=== New Udemy Exercise Scaffolder ===")
        prefix = input("Enter prefix/number (e.g. '01', or press Enter to skip): ").strip()
        title = input("Enter exercise title (e.g. 'Two Sum'): ").strip()
        if not title:
            print("Error: Exercise title is required.")
            sys.exit(1)
        create_exercise(title, prefix)
    elif len(args) == 1:
        create_exercise(args[0])
    elif len(args) == 2:
        create_exercise(title=args[1], prefix=args[0])
    else:
        # 3 or more: join the rest as title
        create_exercise(title=" ".join(args[1:]), prefix=args[0])


if __name__ == "__main__":
    main()
