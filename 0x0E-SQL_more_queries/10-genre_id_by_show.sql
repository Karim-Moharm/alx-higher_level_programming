-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked

SELECT tvs.title, tvg.genre_id
FROM tv_shows AS tvs 
INNER JOIN tv_show_genres AS tvg
ON tvs.id = tvg.show_id
ORDER BY tvs.title, tvg.genre_id ASC;
