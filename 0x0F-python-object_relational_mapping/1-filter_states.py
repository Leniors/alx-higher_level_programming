#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    """only execute when specified"""
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
        sec_argv = row[1]
        if sec_argv[0] == 'N':
            print(row)
    cur.close()
    db.close()
