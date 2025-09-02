#!/usr/bin/env python3
import os
import re
from pathlib import Path
from typing import Dict, List, NamedTuple

class CategoryStats(NamedTuple):
    name: str
    total_problems: int
    completed_problems: int

class ProgressTracker:
    def __init__(self):
        self.root_path = Path.cwd()
        self.sql50_path = self.root_path / "SQL50"
        
        # Category definitions with correct problem counts
        self.categories = {
            "01-Select": {"name": "Select", "total": 5},
            "02-Basic-Joins": {"name": "Basic Joins", "total": 9},
            "03-Basic-Aggregate-Functions": {"name": "Basic Aggregate Functions", "total": 8},
            "04-Sorting-and-Grouping": {"name": "Sorting and Grouping", "total": 7},
            "05-Advanced-Select-and-Joins": {"name": "Advanced Select and Joins", "total": 7},
            "06-Subqueries": {"name": "Subqueries", "total": 7},
            "07-Advanced-String-Functions": {"name": "Advanced String Functions", "total": 8}
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
            
            stats.append(CategoryStats(
                name=category_info["name"],
                total_problems=category_info["total"],
                completed_problems=completed_count
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

    def get_progress_percentage(self, completed: int, total: int) -> int:
        """Calculate completion percentage"""
        return int((completed / total) * 100) if total > 0 else 0

    def update_sql50_readme(self, stats: List[CategoryStats]):
        """Update SQL50/README.md with current progress"""
        sql50_readme_path = self.sql50_path / "README.md"
        
        if not sql50_readme_path.exists():
            print(f"Warning: {sql50_readme_path} not found")
            return
        
        # Calculate totals
        total_problems = sum(stat.total_problems for stat in stats)
        total_completed = sum(stat.completed_problems for stat in stats)
        progress_percentage = self.get_progress_percentage(total_completed, total_problems)

        # Read current content
        with open(sql50_readme_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Create new Progress Overview section
        progress_section = f"""## 📊 Progress Overview

**Total Progress: {total_completed}/{total_problems} problems ({progress_percentage}%)**

## 🗂️ Categories

| # | Category | Problems | Status | Progress |
|---|----------|----------|--------|----------|"""
        
        for i, stat in enumerate(stats, 1):
            status_emoji = self.get_status_emoji(stat.completed_problems, stat.total_problems)
            status_text = f"{status_emoji} {stat.completed_problems}/{stat.total_problems}"
            progress_percent = self.get_progress_percentage(stat.completed_problems, stat.total_problems)
            
            # Create proper anchor links
            category_anchor = stat.name.lower().replace(' ', '-').replace('&', 'and')
            progress_section += f"\n| {i} | [{stat.name}](#{str(i).zfill(2)}-{category_anchor}) | {stat.total_problems} | {status_text} | {progress_percent}% |"

        # Find and replace the entire section from Progress Overview to the --- separator
        pattern = r'## 📊 Progress Overview.*?(?=---|\n## [^🗂]|\Z)'
        replacement = progress_section + '\n\n---\n\n'
        
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

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
        sql50_progress = self.get_progress_percentage(sql50_completed, sql50_total)

        # Read current content
        with open(main_readme_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update the "Database & SQL Engineering" table section
        # Pattern to match the entire table row for SQL50
        sql50_pattern = r'(\|\s*\[?\*?\*?SQL50\*?\*?\]?\([^)]*\)\s*\|\s*)\d+(\s*\|\s*[^|]*\s*\|\s*)![Progress]\([^)]+\)(\s*\|\s*[^|]*\s*\|)'
        sql50_replacement = f'\\g<1>{sql50_total}\\g<2>![Progress](https://img.shields.io/badge/Progress-{sql50_progress}%25-{"green" if sql50_progress >= 50 else "yellow" if sql50_progress >= 25 else "red"})\\g<3>'
        
        content = re.sub(sql50_pattern, sql50_replacement, content)

        # Update "Current Progress" section if it exists
        current_progress_pattern = r'(\*\*Total Progress: )\d+/\d+ problems \(\d+%\)'
        current_progress_replacement = f'\\g<1>{sql50_completed}/{sql50_total} problems ({sql50_progress}%)'
        content = re.sub(current_progress_pattern, current_progress_replacement, content)

        # Also try to update the progress tracking line in the repository
        repo_progress_pattern = r'(\*\*Total Progress: )\d+/50 problems \(\d+%\)'
        repo_progress_replacement = f'\\g<1>{sql50_completed}/{sql50_total} problems ({sql50_progress}%)'
        content = re.sub(repo_progress_pattern, repo_progress_replacement, content)

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
        progress_percentage = self.get_progress_percentage(total_completed, total_problems)
        
        print(f"\n🎯 Summary:")
        print(f"   Total progress: {total_completed}/{total_problems} ({progress_percentage}%)")
        print(f"   Categories with progress: {len([s for s in stats if s.completed_problems > 0])}/7")
        print(f"   Completed categories: {len([s for s in stats if s.completed_problems == s.total_problems])}/7")
        
        # Show detailed breakdown
        print(f"\n📈 Detailed Breakdown:")
        for stat in stats:
            status = "✅" if stat.completed_problems == stat.total_problems else "🚧" if stat.completed_problems > 0 else "⏳"
            percentage = self.get_progress_percentage(stat.completed_problems, stat.total_problems)
            print(f"   {status} {stat.name}: {stat.completed_problems}/{stat.total_problems} ({percentage}%)")

if __name__ == "__main__":
    try:
        tracker = ProgressTracker()
        tracker.run()
        print("\n✅ Progress update completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Error updating progress: {str(e)}")
        import traceback
        traceback.print_exc()