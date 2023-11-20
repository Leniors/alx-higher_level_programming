#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
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
    cur.execute("SELECT * FROM states ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
