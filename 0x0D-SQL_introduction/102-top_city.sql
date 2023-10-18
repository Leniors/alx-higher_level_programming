-- importing the table
USE hbtn_0c_0
SOURCE /path/to/your/table_dump_file.sql
SELECT city, temperature
FROM table_name
WHERE month IN ('July', 'August')
ORDER BY temperature DESC
LIMIT 3
