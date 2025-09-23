# [550. Game Play Analysis IV](https://leetcode.com/problems/game-play-analysis-iv/)

**Difficulty:** Medium  
**Category:** Basic Aggregate Functions

## Problem

Write a SQL query to find the **fraction** of players who logged in again on the day after their first login day, rounded to **2 decimal places**.

**Table: Activity**
```
+-----------+-----------+------------+--------------+
| Column Name   | Type    |
+-----------+-----------+------------+--------------+
| player_id     | int     |
| device_id     | int     |
| event_date    | date    |
| games_played  | int     |
+-----------+-----------+------------+--------------+
```

**Example:**

**Input:**
```
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2016-03-02 | 1            |
| 3         | 1         | 2016-03-01 | 0            |
| 3         | 4         | 2016-07-03 | 5            |
+-----------+-----------+------------+--------------+
```

**Output:**
```
+----------+
| fraction |
+----------+
| 0.33     |
+----------+
```

**Explanation:**
- Player 1: First login `2016-03-01`, **did** login on `2016-03-02` (consecutive)
- Player 2: First login `2016-03-02`, **no** login on `2016-03-03` (not consecutive)  
- Player 3: First login `2016-03-01`, **no** login on `2016-03-02` (not consecutive)

**Result:** 1 out of 3 players logged consecutively = 1/3 = 0.33

## Solution Approach

Use **subquery with IN clause** to find players who logged in exactly one day after their first login. **Key insight**: Need to identify first login date per player, then check if (player_id, first_login_date + 1) exists in the activity table.

**Why subquery approach?** We need to compare each player's first login date with all their subsequent activities to find the specific "day after first login" pattern.

**Critical pattern**: This is a **retention analysis** - measuring player engagement after initial signup, common in gaming/app analytics.

**Key concepts:**
- MIN() with GROUP BY to find first login per player
- Date arithmetic with INTERVAL or DATE_ADD  
- Self-referential logic using IN clause or EXISTS
- Fraction calculation with ROUND for precision
- COUNT(DISTINCT) to avoid duplicate counting

**Files:**
- `solution.sql` - Subquery approach with IN clause
- `solution_cte.sql` - CTE version for step-by-step clarity
- `solution.py` - Pandas implementation with date operations and set logic