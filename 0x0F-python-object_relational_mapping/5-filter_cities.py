#!/usr/bin/python3
"""list all cities in the hbtn_0e_4_usa database"""
import MySQLdb
import sys

if __name__ == "__main__":
    """executes only if the fie is called"""
    if len(sys.argv) != 5:
        sys.exit()
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=name,
        host='localhost',
        port=3306)
    cur = db.cursor()
    query = """
    SELECT cities.name
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cur.execute(query, (state,))
    rows = cur.fetchall()
    last = len(rows) - 1
    i = 0
    for row in rows:
        if i < last:
            print(row[0], end=", ")
        else:
            print(row[0], end="")
        i += 1
    print()
