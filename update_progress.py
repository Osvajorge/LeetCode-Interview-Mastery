#!/usr/bin/env python3
"""
Auto-update progress statistics across all README files in the repository.
This script scans the SQL50 directory structure and updates:
1. Main README.md - Overall progress and badges
2. SQL50/README.md - Category breakdown and totals

Usage: python update_progress.py
"""

import os
import re
from pathlib import Path
from typing import Dict, Tuple

def scan_problems() -> Dict[str, Dict[str, int]]:
    """
    Scan the SQL50 directory to count problems in each category.
    Returns a dictionary with category info and problem counts.
    """
    sql50_path = Path("SQL50")
    if not sql50_path.exists():
        print("❌ SQL50 directory not found!")
        return {}
    
    categories = {
        "01-Select": {"name": "Select", "total": 5},
        "02-Basic-Joins": {"name": "Basic Joins", "total": 6},
        "03-Basic-Aggregate-Functions": {"name": "Aggregate Functions", "total": 7},
        "04-Sorting-and-Grouping": {"name": "Sorting & Grouping", "total": 5},
        "05-Advanced-Select-and-Joins": {"name": "Advanced Joins", "total": 12},
        "06-Subqueries": {"name": "Subqueries", "total": 8},
        "07-Advanced-String-Functions": {"name": "String Functions", "total": 7}
    }
    
    results = {}
    total_completed = 0
    total_problems = 50
    
    print("🔍 Scanning SQL50 directory structure...")
    
    for category_dir, category_info in categories.items():
        category_path = sql50_path / category_dir
        completed = 0
        
        if category_path.exists():
            # Count problem directories (exclude __pycache__ and other non-problem dirs)
            problem_dirs = [d for d in category_path.iterdir() 
                          if d.is_dir() and not d.name.startswith('__')]
            completed = len(problem_dirs)
            
            print(f"  📁 {category_info['name']}: {completed}/{category_info['total']} problems")
        else:
            print(f"  📁 {category_info['name']}: 0/{category_info['total']} problems (directory not found)")
        
        results[category_dir] = {
            "name": category_info["name"],
            "completed": completed,
            "total": category_info["total"]
        }
        total_completed += completed
    
    results["_totals"] = {
        "completed": total_completed,
        "total": total_problems,
        "percentage": round((total_completed / total_problems) * 100)
    }
    
    print(f"\n📊 Total Progress: {total_completed}/{total_problems} ({results['_totals']['percentage']}%)")
    return results

def get_progress_color(percentage: int) -> str:
    """Return appropriate color for progress badge based on percentage."""
    if percentage >= 80:
        return "green"
    elif percentage >= 60:
        return "yellow"
    elif percentage >= 30:
        return "orange"
    else:
        return "red"

def update_main_readme(progress_data: Dict) -> bool:
    """Update the main README.md with current progress statistics."""
    readme_path = Path("README.md")
    if not readme_path.exists():
        print("❌ Main README.md not found!")
        return False
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    totals = progress_data["_totals"]
    
    # Update progress badge
    progress_color = get_progress_color(totals["percentage"])
    new_progress_badge = f'![Progress](https://img.shields.io/badge/Progress-{totals["percentage"]}%25-{progress_color})'
    content = re.sub(
        r'!\[Progress\]\(https://img\.shields\.io/badge/Progress-\d+%25-\w+\)',
        new_progress_badge,
        content
    )
    
    # Update total progress text
    new_progress_text = f'**Total Progress: {totals["completed"]}/{totals["total"]} problems ({totals["percentage"]}%)** 🎯'
    content = re.sub(
        r'\*\*Total Progress: \d+/\d+ problems \(\d+%\)\*\* 🎯[^*]*',
        new_progress_text + ' *Building momentum!*' if totals["percentage"] < 50 else new_progress_text + ' *Great progress!*',
        content
    )
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Updated main README.md - {totals['percentage']}% progress")
    return True

def update_sql50_readme(progress_data: Dict) -> bool:
    """Update the SQL50/README.md with category breakdown."""
    readme_path = Path("SQL50/README.md")
    if not readme_path.exists():
        print("❌ SQL50/README.md not found!")
        return False
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Build the new table
    table_rows = []
    for i, (category_dir, data) in enumerate(progress_data.items(), 1):
        if category_dir == "_totals":
            continue
        
        category_link = f"[{data['name']}](./{category_dir}/)"
        status = f"{data['completed']}/{data['total']}"
        table_rows.append(f"| {i} | {category_link} | {data['total']} | {status} |")
    
    new_table = "\n".join(table_rows)
    
    # Replace the categories table
    table_pattern = r'(\| # \| Category \| Problems \| Status \|\n\|---|----------|----------|--------\|\n).*?(?=\n\n## Progress:)'
    replacement = f'\\g<1>{new_table}'
    content = re.sub(table_pattern, replacement, content, flags=re.DOTALL)
    
    # Update progress summary
    totals = progress_data["_totals"]
    progress_color = get_progress_color(totals["percentage"])
    new_progress = f'## Progress: {totals["completed"]}/{totals["total"]} ![Progress](https://img.shields.io/badge/Progress-{totals["percentage"]}%25-{progress_color})'
    
    content = re.sub(
        r'## Progress: \d+/\d+ !\[Progress\]\([^)]+\)',
        new_progress,
        content
    )
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Updated SQL50/README.md - Category breakdown refreshed")
    return True

def main():
    """Main function to update all progress statistics."""
    print("🚀 Auto-updating repository progress...")
    print("=" * 50)
    
    # Scan current progress
    progress_data = scan_problems()
    if not progress_data:
        print("❌ Failed to scan problems")
        return
    
    print("\n📝 Updating README files...")
    
    # Update main README
    main_updated = update_main_readme(progress_data)
    
    # Update SQL50 README
    sql50_updated = update_sql50_readme(progress_data)
    
    # Summary
    print("\n" + "=" * 50)
    if main_updated and sql50_updated:
        totals = progress_data["_totals"]
        print(f"✅ All README files updated successfully!")
        print(f"📈 Current progress: {totals['completed']}/{totals['total']} ({totals['percentage']}%)")
        print(f"🎯 Keep going! You're doing great!")
        
        # Motivational messages based on progress
        if totals["percentage"] >= 80:
            print("🏆 Amazing! You're almost done with SQL50!")
        elif totals["percentage"] >= 50:
            print("💪 Great momentum! You're past the halfway mark!")
        elif totals["percentage"] >= 25:
            print("🔥 Solid progress! Keep building that SQL mastery!")
        else:
            print("🌱 Every expert was once a beginner. You've got this!")
    else:
        print("⚠️  Some updates failed. Check the errors above.")

if __name__ == "__main__":
    main()