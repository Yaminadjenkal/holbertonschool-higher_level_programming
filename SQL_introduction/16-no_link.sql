-- Shows full description of `first_table`, DB passed as script arg.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
