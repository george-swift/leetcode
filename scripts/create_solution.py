import os
import re

def sanitize_filename(name):
    """Converts problem name to a valid filename format."""
    return re.sub(r'[^a-zA-Z0-9-]', '-', name.lower().strip())

def prompt_for_problem():
    print("\n🚀 LeetCode Solution Generator")

    problem_number = input("Enter problem number (e.g., 0001): ").zfill(4)
    problem_title = input("Enter problem title (e.g., Two Sum): ").strip()
    difficulty = input("Enter difficulty (easy/medium/hard): ").lower()

    if difficulty not in ["easy", "medium", "hard"]:
        print("❌ Invalid difficulty. Please use easy, medium, or hard.")
        return None

    tags = input("Enter tags (comma-separated, e.g., array,hashmap): ").split(',')
    tags = [tag.strip() for tag in tags if tag.strip()]

    return problem_number, problem_title, difficulty, tags

def create_solution_file(problem_number, problem_title, difficulty, tags):
    filename = f"{problem_number}-{sanitize_filename(problem_title)}.py"
    folder_path = os.path.join(os.getcwd(), difficulty)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, filename)

    # Solution template
    content = f'''"""
LeetCode Problem: {problem_number} - {problem_title}

Difficulty: {difficulty.title()}
Tags: {', '.join(tags) if tags else 'N/A'}

Problem Description:
    [Add a brief summary or copy-paste the problem prompt]
"""

from typing import List, Optional

class Solution:
    def solve(self, *args) -> any:
        """
        Main solution method.

        Args:
            *args: Variable input based on problem requirements.

        Returns:
            any: Solution output.
        """
        pass


# Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Example tests (modify as needed)
    print(solution.solve())  # Expected: <output>
'''

    with open(file_path, 'w') as f:
        f.write(content)

    print(f"✅ Created: {file_path}")

if __name__ == "__main__":
    problem_details = prompt_for_problem()

    if problem_details:
        create_solution_file(*problem_details)
