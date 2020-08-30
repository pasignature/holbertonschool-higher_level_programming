-- fetch all scores and names where name field is NOT empty, then order it by largest to smallest
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
