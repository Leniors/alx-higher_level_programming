#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """only execute when specified"""
    if len(sys.argv) != 5:
        sys.exit()
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    searched = sys.argv[4]
    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=name,
        host='localhost',
        port=3306)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC".format(
        searched)
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
