#!/usr/bin/env python3
"""
Script to automatically update progress in SQL50 README.md
Usage: python update_progress.py
"""

import os
import re
from pathlib import Path

# Official SQL50 structure
SQL50_CATEGORIES = {
    "01-Select": 5,
    "02-Basic-Joins": 8, 
    "03-Basic-Aggregate-Functions": 8,
    "04-Sorting-and-Grouping": 7,
    "05-Advanced-Select-and-Joins": 7,
    "06-Subqueries": 7,
    "07-Advanced-String-Functions": 8
}

def count_completed_problems():
    """Count completed problems by checking existing folders with solutions."""
    sql50_path = Path("SQL50")
    if not sql50_path.exists():
        print("❌ SQL50 folder not found!")
        return {}
    
    category_progress = {}
    
    for category, total_problems in SQL50_CATEGORIES.items():
        category_path = sql50_path / category
        completed = 0
        
        if category_path.exists():
            print(f"🔍 Checking {category}...")
            # Count folders that exist (regardless of solution content for now)
            for folder in category_path.iterdir():
                if folder.is_dir():
                    print(f"  📁 Found: {folder.name}")
                    solution_file = folder / "solution.sql"
                    if solution_file.exists():
                        print(f"    ✅ Has solution.sql")
                        completed += 1
                    else:
                        print(f"    ❌ Missing solution.sql")
        else:
            print(f"❌ Category folder {category} not found")
        
        category_progress[category] = (completed, total_problems)
        print(f"📊 {category}: {completed}/{total_problems}")
    
    return category_progress

def determine_status(completed: int, total: int) -> str:
    """Determine status emoji and text based on completion."""
    if completed == total:
        return f"✅ {completed}/{total}"
    elif completed > 0:
        return f"🚧 {completed}/{total}"
    else:
        return f"⏳ {completed}/{total}"

def update_readme_progress(category_progress: dict):
    """Update the SQL50 README.md with current progress."""
    readme_path = Path("SQL50/README.md")
    
    if not readme_path.exists():
        print("❌ SQL50/README.md not found!")
        return
    
    # Read current README
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Calculate totals
    total_completed = sum(completed for completed, _ in category_progress.values())
    total_problems = sum(total for _, total in category_progress.values())
    total_percentage = int((total_completed / total_problems) * 100) if total_problems > 0 else 0
    
    # Update progress overview
    progress_pattern = r"(\*\*Total Progress: )\d+/\d+ problems \(\d+%\)(\*\*)"
    new_progress = f"\\g<1>{total_completed}/{total_problems} problems ({total_percentage}%)\\g<2>"
    content = re.sub(progress_pattern, new_progress, content)
    
    # Count by difficulty (simplified estimation)
    easy_completed = min(total_completed, 33)  # Most problems are easy
    medium_completed = max(0, total_completed - 33)
    
    # Update difficulty breakdown
    easy_pattern = r"(\| Easy \| 33 \| )\d+( \| \d+% \|)"
    content = re.sub(easy_pattern, f"\\g<1>{easy_completed}\\g<2>", content)
    
    medium_pattern = r"(\| Medium \| 16 \| )\d+( \| \d+% \|)"
    content = re.sub(medium_pattern, f"\\g<1>{medium_completed}\\g<2>", content)
    
    # Update category table
    for category, (completed, total) in category_progress.items():
        status = determine_status(completed, total)
        category_number = category.split('-')[0]
        
        # Pattern to match the category row
        pattern = rf"(\| {category_number} \| \[.*?\] \| {total} \| ).*?( \| .*? \|)"
        replacement = f"\\g<1>{status}\\g<2>"
        content = re.sub(pattern, replacement, content)
    
    # Update current focus based on progress
    current_category = None
    for category, (completed, total) in category_progress.items():
        if 0 < completed < total:  # In progress
            current_category = category
            break
    
    if current_category:
        completed, total = category_progress[current_category]
        category_name = current_category.split('-', 1)[1].replace('-', ' ')
        
        # Different messages based on completion percentage
        if completed / total >= 0.8:
            focus_text = f"**Current Focus: Complete {category_name} category ({completed}/{total} done) - Almost there!**"
        elif completed / total >= 0.5:
            focus_text = f"**Current Focus: Continue with {category_name} category ({completed}/{total} done) - Making good progress!**"
        else:
            focus_text = f"**Current Focus: Work on {category_name} category ({completed}/{total} done) - Getting started!**"
        
        focus_pattern = r"\*\*Current Focus:.*?\*\*"
        content = re.sub(focus_pattern, focus_text, content)
    
    # Write updated content
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"✅ Updated SQL50/README.md")
    print(f"📊 Total Progress: {total_completed}/{total_problems} ({total_percentage}%)")
    
    # Show category breakdown
    print("\n📂 Category Progress:")
    for category, (completed, total) in category_progress.items():
        status_emoji = "✅" if completed == total else "🚧" if completed > 0 else "⏳"
        category_name = category.split('-', 1)[1].replace('-', ' ')
        print(f"  {status_emoji} {category_name}: {completed}/{total}")

def main():
    """Main function to update progress."""
    print("🔄 Updating SQL50 progress...")
    
    # Count completed problems
    category_progress = count_completed_problems()
    
    if not category_progress:
        print("❌ No progress data found!")
        return
    
    # Update README
    update_readme_progress(category_progress)
    
    print("\n🎯 Next Steps:")
    for category, (completed, total) in category_progress.items():
        if 0 < completed < total:
            category_name = category.split('-', 1)[1].replace('-', ' ')
            remaining = total - completed
            print(f"  - Complete {remaining} more problems in {category_name}")
            break

if __name__ == "__main__":
    main()