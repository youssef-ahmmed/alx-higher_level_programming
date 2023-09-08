-- lists all genres in the database hbtn_0d_tvshows_rate by their rating

SELECT tg.name, SUM(tsr.rate) AS rating
FROM tv_genres tg
INNER JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
INNER JOIN tv_shows ts ON tsg.show_id = ts.id
INNER JOIN tv_show_ratings tsr ON ts.id = tsr.show_id
GROUP BY tg.name
ORDER BY rating DESC;
