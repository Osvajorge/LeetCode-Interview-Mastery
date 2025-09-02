#!/usr/bin/env python3
"""
Simplified progress tracking script for LeetCode Interview Mastery repository
Updates both main README.md and SQL50/README.md with current progress
Usage: python update_progress.py
"""

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
        
        # 🎯 CORRECCIÓN 1: Ajustado el total de problemas
        self.categories = {
            "01-Select": {"name": "Select", "total": 5},
            "02-Basic-Joins": {"name": "Basic Joins", "total": 9},
            "03-Basic-Aggregate-Functions": {"name": "Basic Aggregate Functions", "total": 8},
            "04-Sorting-and-Grouping": {"name": "Sorting and Grouping", "total": 7},
            "05-Advanced-Select-and-Joins": {"name": "Advanced Select and Joins", "total": 7},
            "06-Subqueries": {"name": "Subqueries", "total": 7},
            "07-Advanced-String-Functions": {"name": "Advanced String Functions", "total": 7} # Cambiado de 8 a 7
        }

    def scan_directory_for_problems(self) -> Dict[str, List[str]]:
        """Scan SQL50 directory structure to find completed problems"""
        completed_problems = {}
        
        for category_folder in self.sql50_path.glob("*"):
            if category_folder.is_dir() and category_folder.name in self.categories:
                completed_problems[category_folder.name] = []
                
                for problem_folder in category_folder.glob("*"):
                    if problem_folder.is_dir():
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
        
        total_problems = sum(stat.total_problems for stat in stats)
        total_completed = sum(stat.completed_problems for stat in stats)
        progress_percentage = self.get_progress_percentage(total_completed, total_problems)

        with open(sql50_readme_path, 'r', encoding='utf-8') as f:
            content = f.read()

        progress_section = f"""## 📊 Progress Overview

**Total Progress: {total_completed}/{total_problems} problems ({progress_percentage}%)**

## 🗂️ Categories

| # | Category | Problems | Status | Progress |
|:---:|:---|:---:|:---:|:---:|"""
        
        for i, stat in enumerate(stats, 1):
            status_emoji = self.get_status_emoji(stat.completed_problems, stat.total_problems)
            status_text = f"{status_emoji} {stat.completed_problems}/{stat.total_problems}"
            progress_percent = self.get_progress_percentage(stat.completed_problems, stat.total_problems)
            
            category_anchor = stat.name.lower().replace(' ', '-').replace('&', 'and')
            category_id = list(self.categories.keys())[i-1].split('-')[0]
            progress_section += f"\n| {i} | [{stat.name}](#{category_id}-{category_anchor}) | {stat.total_problems} | {status_text} | {progress_percent}% |"

        pattern = re.compile(r"## 📊 Progress Overview.*?(?=## 📚 Solution Structure)", re.DOTALL)
        
        if pattern.search(content):
            new_content = pattern.sub(progress_section, content)
        else:
            print("Warning: Progress section not found in SQL50/README.md. Could not update.")
            new_content = content

        with open(sql50_readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"✅ Updated {sql50_readme_path}")

    def update_main_readme(self, stats: List[CategoryStats]):
        """Update main README.md with SQL50 progress"""
        main_readme_path = self.root_path / "README.md"
        
        if not main_readme_path.exists():
            print(f"Warning: {main_readme_path} not found")
            return

        sql50_total = sum(stat.total_problems for stat in stats)
        sql50_completed = sum(stat.completed_problems for stat in stats)
        sql50_progress = self.get_progress_percentage(sql50_completed, sql50_total)

        with open(main_readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 🎯 CORRECCIÓN 3: Expresión regular más robusta para la tabla principal
        # Esta expresión busca la fila que contiene el enlace a SQL50 y captura las partes que necesitamos
        sql50_pattern = re.compile(
            r"(\|\s*\[\*\*SQL50\*\*\]\(./SQL50/\)\s*\|)([^|]*\|[^|]*\|)(.*?)(\s*\|.*\|)",
            re.DOTALL
        )
        
        color = "green" if sql50_progress >= 50 else "yellow" if sql50_progress >= 25 else "red"
        
        # Construimos el reemplazo usando los grupos capturados por la expresión regular
        # \g<1> es la primera columna, \g<2> son las dos siguientes, y \g<4> es la última
        sql50_replacement = (
            f"\\g<1>"
            f" {sql50_total} | Easy-Hard |" # Actualizamos el total y mantenemos el texto
            f" ![Progress](https://img.shields.io/badge/Progress-{sql50_progress}%25-{color})"
            f"\\g<4>"
        )
        
        content, count = sql50_pattern.subn(sql50_replacement, content)
        if count == 0:
            print("Warning: SQL50 progress line not found in main README.md. Could not update table.")

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
                print(f"   {self.categories[category]['name']}: {len(problems)} problems")
            else:
                print(f"   {self.categories[category]['name']}: No completed problems")

        stats = self.calculate_category_stats(completed_problems)
        
        print("\n📝 Updating README files...")
        self.update_sql50_readme(stats)
        self.update_main_readme(stats)
        
        total_completed = sum(stat.completed_problems for stat in stats)
        total_problems = sum(stat.total_problems for stat in stats)
        progress_percentage = self.get_progress_percentage(total_completed, total_problems)
        
        print(f"\n🎯 Summary:")
        print(f"   Total progress: {total_completed}/{total_problems} ({progress_percentage}%)")

if __name__ == "__main__":
    try:
        tracker = ProgressTracker()
        tracker.run()
        print("\n✅ Progress update completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Error updating progress: {str(e)}")
        import traceback
        traceback.print_exc()