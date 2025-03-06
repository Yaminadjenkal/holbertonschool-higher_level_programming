-- Shows full description of `first_table`, DB passed as script arg.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
