-- lists all the cities of California

SELECT c.id, c.name
FROM states AS s, cities AS c
WHERE s.id = c.state_id AND s.name = 'California'
ORDER BY c.id;
