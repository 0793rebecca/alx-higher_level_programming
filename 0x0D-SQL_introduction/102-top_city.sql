-- the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, temperature
FROM weather
WHERE month IN ('July', 'August')
ORDER BY temperature DESC
LIMIT 3;
