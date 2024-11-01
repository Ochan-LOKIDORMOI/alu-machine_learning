-- This script is used to get the number of fans per origin
SELECT origin, SUM(fans) nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;