-- a SQL script that lists all genres in the hbtn_0d_tvshows_rate database by their rating sum, sorted in descending order
SELECT tv_genres.name AS name, SUM(rating) AS rating
FROM tv_genres
JOIN tv_shows ON tv_shows.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY rating DESC
