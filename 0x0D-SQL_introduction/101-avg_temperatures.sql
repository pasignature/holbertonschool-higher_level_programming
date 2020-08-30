-- fetch the average temperature according to city field and order by avg_temp with the largest first followed by the smallest
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
