#!/usr/bin/python3
import MySQLdb

db = MySQLdb.connect(user='root', passwd='root', db='hbtn_0e_0_usa')
cur = db.cursor()
cur.execute("SELECT * FROM hbtn_0e_0_usa.states ORDER BY id")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()
