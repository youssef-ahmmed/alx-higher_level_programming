-- lists all cities contained in the database

SELECT c.id, c.name, s.name
FROM states AS s, cities AS c
WHERE s.id = c.state_id
ORDER BY c.id;
