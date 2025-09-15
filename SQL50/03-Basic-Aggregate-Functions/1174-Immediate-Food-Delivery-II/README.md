# [1174. Immediate Food Delivery II](https://leetcode.com/problems/immediate-food-delivery-ii/)

**Difficulty:** Easy  
**Category:** Basic

## Problem

[Add problem description here]

## Solution Approach

[Add approach explanation here]
# [1174. Immediate Food Delivery II](https://leetcode.com/problems/immediate-food-delivery-ii/)

**Difficulty:** Medium  
**Category:** Advanced Select and Joins

## Problem

Write a solution to find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places.

If the customer's preferred delivery date is the same as the order date, then the order is called **immediate**; otherwise, it is called **scheduled**.

The **first order** of a customer is the order with the earliest order date that the customer made.

**Table: Delivery**
```
+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+
```

**Example:**
```
Input: 
Delivery table:
+-------------+-------------+------------+-----------------------------+
| delivery_id | customer_id | order_date | customer_pref_delivery_date |
+-------------+-------------+------------+-----------------------------+
| 1           | 1           | 2019-08-01 | 2019-08-02                  |
| 2           | 2           | 2019-08-02 | 2019-08-02                  |
| 3           | 1           | 2019-08-11 | 2019-08-12                  |
| 4           | 3           | 2019-08-24 | 2019-08-24                  |
| 5           | 3           | 2019-08-21 | 2019-08-22                  |
| 6           | 2           | 2019-08-11 | 2019-08-13                  |
| 7           | 4           | 2019-08-09 | 2019-08-09                  |
+-------------+-------------+------------+-----------------------------+

Output: 
+----------------------+
| immediate_percentage |
+----------------------+
| 50.00                |
+----------------------+
```

## Solution Approach

Two-step process: identify first orders per customer, then calculate immediate percentage.

**Key concepts:**
- Window functions with `ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date)`
- CTE for clean separation of logic
- Boolean averaging for percentage calculation
- Handling "top N per group" pattern

**Pattern:** This is a classic "first/latest per group" problem requiring window functions or correlated subqueries.

**Files:**
- `solution.sql` - ROW_NUMBER() with CTE approach
- `solution_subquery.sql` - Correlated subquery version  
- `solution.py` - Pandas implementation

