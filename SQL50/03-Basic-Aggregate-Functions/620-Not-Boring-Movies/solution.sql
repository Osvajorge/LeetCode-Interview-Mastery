SELECT id,
    movie,
    description,
    rating
FROM Cinema
WHERE description != 'boring' And id % 2 = 1
ORDER BY rating DESC