-- Display the max temp according to states
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state;
