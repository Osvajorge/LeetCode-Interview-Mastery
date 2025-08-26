#!/usr/bin/env python3
"""
Simple script to create SQL problem structure
Usage: python create_problem.py 1757 "Recyclable and Low Fat Products" 01-Select
"""

import os
import sys
from pathlib import Path

def create_problem(number, name, category):
    # Create folder
    folder_name = f"{number}-{name.replace(' ', '-')}"
    problem_path = Path("SQL50") / category / folder_name
    problem_path.mkdir(parents=True, exist_ok=True)
    
    # Create README.md
    readme_content = f"""# [{number}. {name}](https://leetcode.com/problems/{name.lower().replace(' ', '-')}/)

**Difficulty:** Easy  
**Category:** {category.split('-')[1]}

## Problem

[Add problem description here]

## Solution Approach

[Add approach explanation here]

**Files:**
- `solution.sql` - Standard approach
- `solution_cte.sql` - CTE version
- `solution.py` - Pandas implementation
"""
    
    with open(problem_path / "README.md", "w") as f:
        f.write(readme_content)
    
    # Create solution.sql
    with open(problem_path / "solution.sql", "w") as f:
        f.write("-- Add your SQL solution here\nSELECT * FROM table_name WHERE condition;\n")
    
    # Create solution_cte.sql
    with open(problem_path / "solution_cte.sql", "w") as f:
        f.write("-- CTE approach\nWITH cte AS (\n    SELECT * FROM table_name\n)\nSELECT * FROM cte WHERE condition;\n")
    
    # Create solution.py
    with open(problem_path / "solution.py", "w") as f:
        f.write("""import pandas as pd

def solve_problem(df: pd.DataFrame) -> pd.DataFrame:
    # Add pandas solution here
    return df[df['column'] == 'value']
""")
    
    print(f"✅ Created: {problem_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python create_problem.py <number> <name> <category>")
        print("Example: python create_problem.py 1757 'Recyclable and Low Fat Products' 01-Select")
        sys.exit(1)
    
    number, name, category = sys.argv[1], sys.argv[2], sys.argv[3]
    create_problem(number, name, category)