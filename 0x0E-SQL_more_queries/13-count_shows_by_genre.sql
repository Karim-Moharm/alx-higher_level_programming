-- list all genre from hbtn_0d_tvshows and displays the number of shows linked to each

SELECT tv_genres.name AS `genre`, count(*) AS `number_of_shows`
FROM genre INNER JOIN number_of_shows
