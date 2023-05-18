-- lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT ts.title, SUM(tsr.rate) AS rating
FROM tv_show_ratings tsr
LEFT JOIN tv_shows ts ON ts.id = tsr.show_id
GROUP BY tsr.show_id 
ORDER BY rating DESC;
