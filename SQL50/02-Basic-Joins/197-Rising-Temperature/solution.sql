-- w1.date is equal to w2.date - one day
SELECT w1.id
FROM Weather w1
INNER JOIN Weather w2 ON w2.recordDate = DATE_SUB(w1.recordDate, INTERVAL 1 DAY)
WHERE w1.temperature > w2.temperature;

-- w1.date is equal to w2.date + one day, meaning the following date of w2. 
SELECT w1.id
FROM Weather w1
JOIN Weather w2 ON w1.recordDate = w2.recordDate + INTERVAL 1 DAY
WHERE w1.temperature > w2.temperature;