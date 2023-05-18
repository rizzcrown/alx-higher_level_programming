-- lists all shows without the genre Comedy
SELECT ts.title
FROM tv_shows ts
WHERE ts.title NOT IN (
	SELECT ts.title
	FROM tv_shows ts
	LEFT JOIN tv_show_genres tsg ON ts.id = tsg.show_id
	LEFT JOIN tv_genres tg ON tsg.genre_id = tg.id
	WHERE tg.name = 'Comedy'
)
ORDER BY ts.title;
