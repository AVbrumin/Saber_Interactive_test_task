/* SQL 1 */
SELECT 
    SUBSTR(issue_key, 1, 1) as "groups of tasks ",
    round(AVG(minutes_in_status)/60, 2) as "mean value (hours)"
FROM 
    history 
WHERE 
    lower(status) = 'open'
GROUP BY SUBSTR(issue_key, 1, 1);



/* SQL 2  */
/* Для настройки запроса измените дату в строке 9. Аргумент 'now' соответствует текущей дате */
SELECT 
	issue_key,
    status,
	datetime(max(started_at) / 1000, 'unixepoch') as "time of last status" -- перевод времени в текстовое представление  
FROM 
	history 
WHERE 
    started_at <= (strftime('%s', '2022-09-15 09:17:04') * 1000)

GROUP BY issue_key
HAVING lower(status) not in ('closed', 'resolved');