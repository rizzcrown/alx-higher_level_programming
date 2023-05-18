-- lists all shows, and all genres linked to that show
SELECT ts.title, tg.name
FROM tv_show_genres tsg
RIGHT JOIN tv_shows ts ON ts.id = tsg.show_id
LEFT JOIN tv_genres tg ON tg.id = tsg.genre_id
ORDER BY ts.title ASC, tg.name ASC;
