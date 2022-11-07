INSERT INTO weather (`ts`, `lat`, `lon`, `sensor`, `source`, `value`)
SELECT * FROM (
(SELECT DATE_ADD(DATE(ts), INTERVAL 6*floor(HOUR(ts)/6) HOUR) AS 'date', AVG(lat) as lat, AVG(lon) as lon, 'pm25' as sensor, 'aqi' as source, AVG(pm) as value 
FROM `aqi`
GROUP BY date, sensor, source)
UNION
(SELECT DATE_ADD(DATE(ts), INTERVAL 6*floor(HOUR(ts)/6) HOUR) AS 'date', AVG(lat) as lat, AVG(lon) as lon, 'temperature' as sensor, 'kidbright' as source, AVG(temp) as value 
FROM `kidbright`
GROUP BY date, sensor, source)
UNION
(SELECT DATE_ADD(DATE(ts), INTERVAL 6*floor(HOUR(ts)/6) HOUR) AS 'date', AVG(lat) as lat, AVG(lon) as lon, 'light' as sensor, 'kidbright' as source, AVG(light) as value 
FROM `kidbright`
GROUP BY date, sensor, source)
UNION
(SELECT DATE_ADD(DATE(ts), INTERVAL 6*floor(HOUR(ts)/6) HOUR) AS 'date', AVG(lat) as lat, AVG(lon) as lon, 'temperature' as sensor, 'tmd' as source, AVG(temperature) as value 
FROM `tmd`
GROUP BY date, sensor, source)
UNION
(SELECT DATE_ADD(DATE(ts), INTERVAL 6*floor(HOUR(ts)/6) HOUR) AS 'date', AVG(lat) as lat, AVG(lon) as lon, 'humidity' as sensor, 'tmd' as source, AVG(humidity) as value 
FROM `tmd`
GROUP BY date, sensor, source)
UNION
(SELECT DATE_ADD(DATE(ts), INTERVAL 6*floor(HOUR(ts)/6) HOUR) AS 'date', AVG(lat) as lat, AVG(lon) as lon, 'rain' as sensor, 'tmd' as source, SUM(rainfall) as value 
FROM `tmd`
GROUP BY date, sensor, source)
) AS W  
