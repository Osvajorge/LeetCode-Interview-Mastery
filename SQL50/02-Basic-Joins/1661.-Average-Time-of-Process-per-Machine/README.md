# [1661. Average Time of Process per Machine](https://leetcode.com/problems/average-time-of-process-per-machine/)

**Difficulty:** Easy  
**Category:** Basic Joins

## Problem

Write a SQL query to find the **average time** each machine takes to complete a process.

**Table: Activity**
```
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| machine_id     | int     |
| process_id     | int     |
| activity_type  | enum    |
| timestamp      | float   |
+----------------+---------+
```

The table shows the user activities for a factory website.
- `(machine_id, process_id, activity_type)` is the primary key
- `activity_type` is an ENUM of type ('start', 'end')
- A 'start' timestamp must exist for every 'end' timestamp, and they represent the start and end of a process

**Example:**

**Input:**
```
Activity table:
+------------+------------+---------------+-----------+
| machine_id | process_id | activity_type | timestamp |
+------------+------------+---------------+-----------+
| 0          | 0          | start         | 0.712     |
| 0          | 0          | end           | 1.520     |
| 0          | 1          | start         | 3.140     |
| 0          | 1          | end           | 4.120     |
| 1          | 0          | start         | 0.550     |
| 1          | 0          | end           | 1.550     |
| 1          | 1          | start         | 0.430     |
| 1          | 1          | end           | 1.420     |
| 2          | 0          | start         | 4.100     |
| 2          | 0          | end           | 4.512     |
| 2          | 1          | start         | 2.500     |
| 2          | 1          | end           | 5.000     |
+------------+------------+---------------+-----------+
```

**Output:**
```
+------------+-----------------+
| machine_id | processing_time |
+------------+-----------------+
| 0          | 0.894           |
| 1          | 0.995           |
| 2          | 1.456           |
+------------+-----------------+
```

**Explanation:**
- Machine 0: Process 0 = 1.520 - 0.712 = 0.808, Process 1 = 4.120 - 3.140 = 0.980. Average = (0.808 + 0.980) / 2 = 0.894
- Machine 1: Process 0 = 1.550 - 0.550 = 1.000, Process 1 = 1.420 - 0.430 = 0.990. Average = (1.000 + 0.990) / 2 = 0.995
- Machine 2: Process 0 = 4.512 - 4.100 = 0.412, Process 1 = 5.000 - 2.500 = 2.500. Average = (0.412 + 2.500) / 2 = 1.456

## Solution Approach

Use **self-join** to match 'start' and 'end' activities for the same machine and process, then calculate the time difference and average per machine.

**Why self-join?** The data contains start/end pairs in separate rows. We need to combine them to calculate processing time (end - start). Self-join allows us to pair each 'start' record with its corresponding 'end' record.

**Key insight**: Join on both `machine_id` AND `process_id` to ensure we're matching the correct start/end pairs, then filter by activity_type to get start-end combinations.

**Key concepts:**
- Self-join pattern for start/end event pairing
- Multiple JOIN conditions for precise matching
- Aggregation with GROUP BY at machine level (not machine-process level)
- ROUND() function for decimal precision
- Pandas merge with multiple keys and boolean filtering

**Files:**
- `solution.sql` - Self-join approach with direct aggregation
- `solution_cte.sql` - CTE version separating calculation logic from presentation
- `solution.py` - Pandas merge implementation with DataFrame filtering