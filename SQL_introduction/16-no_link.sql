-- Lists all records in second_table in descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;