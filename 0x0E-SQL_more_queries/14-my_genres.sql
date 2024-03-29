-- uses the hbtn_0d_tvshows database to
-- lists all genres of the show Dexter
SELECT tg.name
FROM tv_shows ts
INNER JOIN tv_show_genres tsg ON tsg.show_id = ts.id
INNER JOIN tv_genres tg ON tg.id = tsg.genre_id
WHERE ts.title = 'Dexter'
ORDER BY tg.name ASC;
