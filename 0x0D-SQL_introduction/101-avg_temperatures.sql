-- import
USE hbtn_0c_0
SOURCE /path/to/your/table_dump_file.sql
SELECT city, AVG(temperature) as average_temperature_Fahrenheit
FROM table_name
GROUP BY city
ORDER BY average_temperature_Fahrenheit DESC
