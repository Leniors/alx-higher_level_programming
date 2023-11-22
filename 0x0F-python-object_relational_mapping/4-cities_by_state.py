#!/usr/bin/python3
"""list all cities in the hbtn_0e_4_usa database"""
import MySQLdb
import sys

if __name__ == "__main__":
    """executes only if the fie is called"""
    if len(sys.argv) != 4:
        sys.exit()
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=name,
        host='localhost',
        port=3306)
    cur = db.cursor()
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    ORDER BY cities.id
    """
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
