#!/usr/bin/env python3
"""
Enhanced progress tracking script for LeetCode Interview Mastery repository
Updates both main README.md and SQL50/README.md with current progress
Usage: python update_progress.py
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple, NamedTuple

class CategoryStats(NamedTuple):
    name: str
    total_problems: int
    completed_problems: int
    easy_total: int
    medium_total: int
    hard_total: int
    easy_completed: int
    medium_completed: int
    hard_completed: int

class ProgressTracker:
    def __init__(self):
        self.root_path = Path.cwd()
        self.sql50_path = self.root_path / "SQL50"
        
        # Category definitions with correct problem counts from your structure
        self.categories = {
            "01-Select": {"name": "Select", "total": 5, "easy": 5, "medium": 0, "hard": 0},
            "02-Basic-Joins": {"name": "Basic Joins", "total": 9, "easy": 7, "medium": 2, "hard": 0},
            "03-Basic-Aggregate-Functions": {"name": "Basic Aggregate Functions", "total": 8, "easy": 5, "medium": 3, "hard": 0},
            "04-Sorting-and-Grouping": {"name": "Sorting and Grouping", "total": 7, "easy": 5, "medium": 2, "hard": 0},
            "05-Advanced-Select-and-Joins": {"name": "Advanced Select and Joins", "total": 7, "easy": 3, "medium": 4, "hard": 0},
            "06-Subqueries": {"name": "Subqueries", "total": 7, "easy": 1, "medium": 5, "hard": 1},
            "07-Advanced-String-Functions": {"name": "Advanced String Functions", "total": 8, "easy": 6, "medium": 1, "hard": 0}
        }

    def scan_directory_for_problems(self) -> Dict[str, List[str]]:
        """Scan SQL50 directory structure to find completed problems"""
        completed_problems = {}
        
        for category_folder in self.sql50_path.glob("*"):
            if category_folder.is_dir() and category_folder.name in self.categories:
                completed_problems[category_folder.name] = []
                
                # Look for problem folders (contains solution files)
                for problem_folder in category_folder.glob("*"):
                    if problem_folder.is_dir():
                        # Check if problem has at least one solution file
                        has_sql = (problem_folder / "solution.sql").exists()
                        has_py = (problem_folder / "solution.py").exists()
                        has_readme = (problem_folder / "README.md").exists()
                        
                        if has_sql or has_py or has_readme:
                            completed_problems[category_folder.name].append(problem_folder.name)
        
        return completed_problems

    def calculate_category_stats(self, completed_problems: Dict[str, List[str]]) -> List[CategoryStats]:
        """Calculate statistics for each category"""
        stats = []
        
        for category_key, category_info in self.categories.items():
            completed_count = len(completed_problems.get(category_key, []))
            
            # For simplicity, assume completed problems are distributed proportionally across difficulties
            # In a real implementation, you'd want to track difficulty per problem
            total = category_info["total"]
            easy_total = category_info["easy"]
            medium_total = category_info["medium"] 
            hard_total = category_info["hard"]
            
            # Proportional completion calculation
            completion_rate = completed_count / total if total > 0 else 0
            easy_completed = int(easy_total * completion_rate)
            medium_completed = int(medium_total * completion_rate)
            hard_completed = int(hard_total * completion_rate)
            
            stats.append(CategoryStats(
                name=category_info["name"],
                total_problems=total,
                completed_problems=completed_count,
                easy_total=easy_total,
                medium_total=medium_total,
                hard_total=hard_total,
                easy_completed=easy_completed,
                medium_completed=medium_completed,
                hard_completed=hard_completed
            ))
        
        return stats

    def get_status_emoji(self, completed: int, total: int) -> str:
        """Get status emoji based on completion percentage"""
        if completed == 0:
            return "⏳"
        elif completed == total:
            return "✅"
        else:
            return "🚧"

    def update_sql50_readme(self, stats: List[CategoryStats]):
        """Update SQL50/README.md with current progress"""
        sql50_readme_path = self.sql50_path / "README.md"
        
        if not sql50_readme_path.exists():
            print(f"Warning: {sql50_readme_path} not found")
            return
        
        # Calculate totals
        total_problems = sum(stat.total_problems for stat in stats)
        total_completed = sum(stat.completed_problems for stat in stats)
        total_easy = sum(stat.easy_total for stat in stats)
        total_medium = sum(stat.medium_total for stat in stats) 
        total_hard = sum(stat.hard_total for stat in stats)
        total_easy_completed = sum(stat.easy_completed for stat in stats)
        total_medium_completed = sum(stat.medium_completed for stat in stats)
        total_hard_completed = sum(stat.hard_completed for stat in stats)
        
        progress_percentage = int((total_completed / total_problems) * 100) if total_problems > 0 else 0
        easy_progress = int((total_easy_completed / total_easy) * 100) if total_easy > 0 else 0
        medium_progress = int((total_medium_completed / total_medium) * 100) if total_medium > 0 else 0
        hard_progress = int((total_hard_completed / total_hard) * 100) if total_hard > 0 else 0

        # Read current content
        with open(sql50_readme_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update Progress Overview section
        progress_section = f"""## 📊 Progress Overview

**Total Progress: {total_completed}/{total_problems} problems ({progress_percentage}%)**

| Difficulty | Count | Completed | Progress |
|-----------|-------|-----------|----------|
| Easy | {total_easy} | {total_easy_completed} | {easy_progress}% |
| Medium | {total_medium} | {total_medium_completed} | {medium_progress}% |
| Hard | {total_hard} | {total_hard_completed} | {hard_progress}% |"""

        # Update Categories section
        categories_section = "## 🗂️ Categories\n\n| # | Category | Problems | Status | Difficulty Split |\n|---|----------|----------|--------|------------------|\n"
        
        for i, stat in enumerate(stats, 1):
            status_emoji = self.get_status_emoji(stat.completed_problems, stat.total_problems)
            status_text = f"{status_emoji} {stat.completed_problems}/{stat.total_problems}"
            
            difficulty_parts = []
            if stat.easy_total > 0:
                difficulty_parts.append(f"{stat.easy_total} Easy")
            if stat.medium_total > 0:
                difficulty_parts.append(f"{stat.medium_total} Medium")
            if stat.hard_total > 0:
                difficulty_parts.append(f"{stat.hard_total} Hard")
            
            difficulty_split = ", ".join(difficulty_parts)
            
            categories_section += f"| {i} | [{stat.name}](#{str(i).zfill(2)}-{stat.name.lower().replace(' ', '-')}) | {stat.total_problems} | {status_text} | {difficulty_split} |\n"

        # Replace sections in content
        content = re.sub(
            r'## 📊 Progress Overview.*?(?=## 🗂️ Categories)',
            progress_section + '\n\n',
            content,
            flags=re.DOTALL
        )
        
        content = re.sub(
            r'## 🗂️ Categories.*?(?=---|\n## |\Z)',
            categories_section + '\n---\n\n',
            content,
            flags=re.DOTALL
        )

        # Write updated content
        with open(sql50_readme_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ Updated {sql50_readme_path}")

    def update_main_readme(self, stats: List[CategoryStats]):
        """Update main README.md with SQL50 progress"""
        main_readme_path = self.root_path / "README.md"
        
        if not main_readme_path.exists():
            print(f"Warning: {main_readme_path} not found")
            return

        # Calculate SQL50 totals
        sql50_total = sum(stat.total_problems for stat in stats)
        sql50_completed = sum(stat.completed_problems for stat in stats)
        sql50_progress = int((sql50_completed / sql50_total) * 100) if sql50_total > 0 else 0

        # Read current content
        with open(main_readme_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update SQL50 progress in the table
        pattern = r'(\|\s*\[\*\*SQL50\*\*\]\(\.\/SQL50\/\)\s*\|\s*)\d+(\s*\|\s*[^|]*\s*\|\s*)![Progress](https://img\.shields\.io/badge/Progress-\d+%25-[^)]+)(\s*\|[^|]*\|)'
        replacement = rf'\g<1>{sql50_total}\g<2>![Progress](https://img.shields.io/badge/Progress-{sql50_progress}%25-{"green" if sql50_progress >= 50 else "yellow" if sql50_progress >= 25 else "red"})\g<3>'
        
        content = re.sub(pattern, replacement, content)

        # Update total progress line
        total_pattern = r'\*\*Total Progress: \d+/\d+ problems \(\d+%\)'
        total_replacement = f'**Total Progress: {sql50_completed}/{sql50_total} problems ({sql50_progress}%)'
        content = re.sub(total_pattern, total_replacement, content)

        # Write updated content
        with open(main_readme_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ Updated {main_readme_path}")

    def run(self):
        """Main execution function"""
        print("🔍 Scanning repository for completed problems...")
        
        completed_problems = self.scan_directory_for_problems()
        
        print("\n📊 Found completed problems:")
        for category, problems in completed_problems.items():
            if problems:
                print(f"  {self.categories[category]['name']}: {len(problems)} problems")
                for problem in problems:
                    print(f"    - {problem}")
            else:
                print(f"  {self.categories[category]['name']}: No completed problems")

        stats = self.calculate_category_stats(completed_problems)
        
        print("\n📝 Updating README files...")
        self.update_sql50_readme(stats)
        self.update_main_readme(stats)
        
        # Summary
        total_completed = sum(stat.completed_problems for stat in stats)
        total_problems = sum(stat.total_problems for stat in stats)
        progress_percentage = int((total_completed / total_problems) * 100) if total_problems > 0 else 0
        
        print(f"\n🎯 Summary:")
        print(f"   Total progress: {total_completed}/{total_problems} ({progress_percentage}%)")
        print(f"   Categories with progress: {len([s for s in stats if s.completed_problems > 0])}/7")
        print(f"   Completed categories: {len([s for s in stats if s.completed_problems == s.total_problems])}/7")

if __name__ == "__main__":
    try:
        tracker = ProgressTracker()
        tracker.run()
        print("\n✅ Progress update completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Error updating progress: {str(e)}")
        import traceback
        traceback.print_exc()