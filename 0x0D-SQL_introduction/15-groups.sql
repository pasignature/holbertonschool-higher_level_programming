-- fetch how many rows for each distinct value of score
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score DESC;
