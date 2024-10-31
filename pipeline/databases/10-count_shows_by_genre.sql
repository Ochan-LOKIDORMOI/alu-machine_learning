-- A script to list all genres and the number of shows linked to each genre,ordered by the number of shows in descending order
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM genres
INNER JOIN tv_show_genres
ON genres.id = tv_show_genres.genre_id
GROUP BY genres.name
ORDER BY number_of_shows DESC;