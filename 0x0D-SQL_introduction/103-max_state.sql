-- import
USE hbtn_0c_0
SOURCE /path/to/your/table_dump_file.sql
SELECT state, MAX(temperature) AS max_temperature
FROM table_name
GROUP BY State
ORDER BY State
