# SQL50 - LeetCode Database Problems

Complete collection of essential SQL problems for interview preparation, organized by LeetCode's official categories.

## 📊 Progress Overview

**Total Progress: 10/50 problems (20%)**

| Difficulty | Count | Completed | Progress |
|-----------|-------|-----------|----------|
| Easy | 33 | 10 | 27% |
| Medium | 16 | 0 | 6% |
| Hard | 1 | 0 | 0% |

## 🗂️ Categories

| # | Category | Problems | Status | Difficulty Split |
|---|----------|----------|--------|------------------|
| 1 | [Select](#01-select) | 5 | ✅ 5/5 | 5 Easy |
| 2 | [Basic Joins](#02-basic-joins) | 8 | 🚧 5/8 | 7 Easy, 1 Medium |
| 3 | [Basic Aggregate Functions](#03-basic-aggregate-functions) | 8 | ⏳ 0/8 | 4 Easy, 4 Medium |
| 4 | [Sorting and Grouping](#04-sorting-and-grouping) | 7 | ⏳ 0/7 | 5 Easy, 2 Medium |
| 5 | [Advanced Select and Joins](#05-advanced-select-and-joins) | 7 | ⏳ 0/7 | 3 Easy, 4 Medium |
| 6 | [Subqueries](#06-subqueries) | 7 | ⏳ 0/7 | 1 Easy, 5 Medium, 1 Hard |
| 7 | [Advanced String Functions](#07-advanced-string-functions) | 8 | ⏳ 0/8 | 6 Easy, 2 Medium |

---

## 01-Select
*Basic filtering and selection operations*

| Problem | Difficulty | Status | Key Concepts |
|---------|------------|---------|--------------|
| [1757. Recyclable and Low Fat Products](./01-Select/1757-Recyclable-and-Low-Fat-Products/) | Easy | ✅ | WHERE, AND logic |
| [584. Find Customer Referee](./01-Select/584-Find-Customer-Referee/) | Easy | ✅ | NULL handling, OR logic |
| [595. Big Countries](./01-Select/595-Big-Countries/) | Easy | ✅ | WHERE, OR conditions |
| [1148. Article Views I](./01-Select/1148-Article-Views-I/) | Easy | ✅ | DISTINCT, self-filtering |
| [1683. Invalid Tweets](./01-Select/1683-Invalid-Tweets/) | Easy | ✅ | String functions, LENGTH |

## 02-Basic-Joins
*Essential JOIN operations and relationships*

| Problem | Difficulty | Status | Key Concepts |
|---------|------------|---------|--------------|
| [1378. Replace Employee ID With The Unique Identifier](./02-Basic-Joins/1378-Replace-Employee-ID-With-The-Unique-Identifier/) | Easy | ✅ | LEFT JOIN, NULL handling |
| [1068. Product Sales Analysis I](./02-Basic-Joins/1068-Product-Sales-Analysis-I/) | Easy | ✅ | INNER JOIN basics |
| [1581. Customer Who Visited but Did Not Make Any Transactions](./02-Basic-Joins/1581-Customer-Who-Visited-but-Did-Not-Make-Any-Transactions/) | Easy | ✅ | LEFT JOIN, NULL filtering |
| [197. Rising Temperature](./02-Basic-Joins/197-Rising-Temperature/) | Easy | ✅ | Self JOIN, date comparison |
| [1661. Average Time of Process per Machine](./02-Basic-Joins/1661-Average-Time-of-Process-per-Machine/) | Easy | ✅ | Self JOIN, aggregation |
| [577. Employee Bonus](./02-Basic-Joins/577-Employee-Bonus/) | Easy | ⏳ | LEFT JOIN, NULL conditions |
| [1280. Students and Examinations](./02-Basic-Joins/1280-Students-and-Examinations/) | Easy | ⏳ | CROSS JOIN, LEFT JOIN |
| [1934. Confirmation Rate](./02-Basic-Joins/1934-Confirmation-Rate/) | Medium | ⏳ | LEFT JOIN, CASE, aggregation |

## 03-Basic-Aggregate-Functions
*GROUP BY, COUNT, SUM, AVG operations*

| Problem | Difficulty | Status | Key Concepts |
|---------|------------|---------|--------------|
| [620. Not Boring Movies](./03-Basic-Aggregate-Functions/620-Not-Boring-Movies/) | Easy | ⏳ | WHERE, modulo operator |
| [1251. Average Selling Price](./03-Basic-Aggregate-Functions/1251-Average-Selling-Price/) | Easy | ⏳ | Weighted average, JOIN |
| [1075. Project Employees I](./03-Basic-Aggregate-Functions/1075-Project-Employees-I/) | Easy | ⏳ | AVG, GROUP BY, ROUND |
| [1633. Percentage of Users Attended a Contest](./03-Basic-Aggregate-Functions/1633-Percentage-of-Users-Attended-a-Contest/) | Easy | ⏳ | Percentage calculation |
| [1211. Queries Quality and Percentage](./03-Basic-Aggregate-Functions/1211-Queries-Quality-and-Percentage/) | Easy | ⏳ | Multiple aggregations |
| [1193. Monthly Transactions I](./03-Basic-Aggregate-Functions/1193-Monthly-Transactions-I/) | Medium | ⏳ | DATE functions, conditional aggregation |
| [1174. Immediate Food Delivery II](./03-Basic-Aggregate-Functions/1174-Immediate-Food-Delivery-II/) | Medium | ⏳ | Window functions, percentage |
| [550. Game Play Analysis IV](./03-Basic-Aggregate-Functions/550-Game-Play-Analysis-IV/) | Medium | ⏳ | Self JOIN, date arithmetic |

## 04-Sorting-and-Grouping
*ORDER BY, GROUP BY, HAVING operations*

| Problem | Difficulty | Status | Key Concepts |
|---------|------------|---------|--------------|
| [2356. Number of Unique Subjects Taught by Each Teacher](./04-Sorting-and-Grouping/2356-Number-of-Unique-Subjects-Taught-by-Each-Teacher/) | Easy | ⏳ | COUNT DISTINCT, GROUP BY |
| [1141. User Activity for the Past 30 Days I](./04-Sorting-and-Grouping/1141-User-Activity-for-the-Past-30-Days-I/) | Easy | ⏳ | Date filtering, COUNT DISTINCT |
| [596. Classes More Than 5 Students](./04-Sorting-and-Grouping/596-Classes-More-Than-5-Students/) | Easy | ⏳ | GROUP BY, HAVING |
| [1729. Find Followers Count](./04-Sorting-and-Grouping/1729-Find-Followers-Count/) | Easy | ⏳ | COUNT, GROUP BY, ORDER BY |
| [619. Biggest Single Number](./04-Sorting-and-Grouping/619-Biggest-Single-Number/) | Easy | ⏳ | GROUP BY, HAVING, MAX |
| [1045. Customers Who Bought All Products](./04-Sorting-and-Grouping/1045-Customers-Who-Bought-All-Products/) | Medium | ⏳ | COUNT DISTINCT, subquery |
| [1070. Product Sales Analysis III](./04-Sorting-and-Grouping/1070-Product-Sales-Analysis-III/) | Medium | ⏳ | Window functions, ranking |

## 05-Advanced-Select-and-Joins
*Complex queries, CTEs, window functions*

| Problem | Difficulty | Status | Key Concepts |
|---------|------------|---------|--------------|
| [1731. The Number of Employees Which Report to Each Employee](./05-Advanced-Select-and-Joins/1731-The-Number-of-Employees-Which-Report-to-Each-Employee/) | Easy | ⏳ | Self JOIN, COUNT |
| [1789. Primary Department for Each Employee](./05-Advanced-Select-and-Joins/1789-Primary-Department-for-Each-Employee/) | Easy | ⏳ | CASE, UNION |
| [610. Triangle Judgement](./05-Advanced-Select-and-Joins/610-Triangle-Judgement/) | Easy | ⏳ | CASE, mathematical logic |
| [180. Consecutive Numbers](./05-Advanced-Select-and-Joins/180-Consecutive-Numbers/) | Medium | ⏳ | Self JOIN, consecutive logic |
| [1204. Last Person to Fit in the Bus](./05-Advanced-Select-and-Joins/1204-Last-Person-to-Fit-in-the-Bus/) | Medium | ⏳ | Window functions, cumulative sum |
| [1164. Product Price at a Given Date](./05-Advanced-Select-and-Joins/1164-Product-Price-at-a-Given-Date/) | Medium | ⏳ | Complex date logic, subqueries |
| [1907. Count Salary Categories](./05-Advanced-Select-and-Joins/1907-Count-Salary-Categories/) | Medium | ⏳ | CASE, UNION, conditional counting |

## 06-Subqueries
*Nested queries, correlated subqueries*

| Problem | Difficulty | Status | Key Concepts |
|---------|------------|---------|--------------|
| [1978. Employees Whose Manager Left the Company](./06-Subqueries/1978-Employees-Whose-Manager-Left-the-Company/) | Easy | ⏳ | NOT EXISTS, subqueries |
| [626. Exchange Seats](./06-Subqueries/626-Exchange-Seats/) | Medium | ⏳ | CASE, MOD, complex logic |
| [1341. Movie Rating](./06-Subqueries/1341-Movie-Rating/) | Medium | ⏳ | Multiple CTEs, UNION |
| [1321. Restaurant Growth](./06-Subqueries/1321-Restaurant-Growth/) | Medium | ⏳ | Window functions, moving average |
| [602. Friend Requests II: Who Has the Most Friends](./06-Subqueries/602-Friend-Requests-II-Who-Has-the-Most-Friends/) | Medium | ⏳ | UNION, subqueries, MAX |
| [585. Investments in 2016](./06-Subqueries/585-Investments-in-2016/) | Medium | ⏳ | Multiple subqueries, conditions |
| [185. Department Top Three Salaries](./06-Subqueries/185-Department-Top-Three-Salaries/) | Hard | ⏳ | Window functions, ranking |

## 07-Advanced-String-Functions
*String manipulation, regex, text processing*

| Problem | Difficulty | Status | Key Concepts |
|---------|------------|---------|--------------|
| [1667. Fix Names in a Table](./07-Advanced-String-Functions/1667-Fix-Names-in-a-Table/) | Easy | ⏳ | UPPER, LOWER, CONCAT |
| [1527. Patients With a Condition](./07-Advanced-String-Functions/1527-Patients-With-a-Condition/) | Easy | ⏳ | LIKE, pattern matching |
| [196. Delete Duplicate Emails](./07-Advanced-String-Functions/196-Delete-Duplicate-Emails/) | Easy | ⏳ | DELETE, self JOIN |
| [176. Second Highest Salary](./07-Advanced-String-Functions/176-Second-Highest-Salary/) | Medium | ⏳ | LIMIT, OFFSET, DISTINCT |
| [1484. Group Sold Products By The Date](./07-Advanced-String-Functions/1484-Group-Sold-Products-By-The-Date/) | Easy | ⏳ | GROUP_CONCAT, GROUP BY |
| [1327. List the Products Ordered in a Period](./07-Advanced-String-Functions/1327-List-the-Products-Ordered-in-a-Period/) | Easy | ⏳ | Date filtering, HAVING |
| [1517. Find Users With Valid E-Mails](./07-Advanced-String-Functions/1517-Find-Users-With-Valid-E-Mails/) | Easy | ⏳ | REGEXP, email validation |
| [1407. Top Travellers](./07-Advanced-String-Functions/1407-Top-Travellers/) | Easy | ⏳ | LEFT JOIN, COALESCE |

---

## 📚 Solution Structure

Each problem contains:
- **`README.md`** - Problem description, examples, approach explanation
- **`solution.sql`** - Standard SQL solution with comments
- **`solution_cte.sql`** - CTE approach for readability (when applicable)
- **`solution.py`** - Pandas implementation for Python transition


## 🚀 Getting Started

```bash
# Clone and navigate to SQL50
cd SQL50

# Study a specific category
cd 01-Select/1757-Recyclable-and-Low-Fat-Products

# Review all approaches
cat solution.sql
cat solution_cte.sql  
cat solution.py
```

## 📈 Progress Tracking

- ✅ **Completed** - Full solution with all approaches
- ⏳ **In Progress** - Problem identified, needs implementation
- 🎯 **Next** - Prioritized for upcoming study session

**Current Focus: Continue with Basic Joins category (5/8 done) - Making good progress!**