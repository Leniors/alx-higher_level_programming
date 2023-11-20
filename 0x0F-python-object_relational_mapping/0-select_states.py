#!/usr/bin/python3
import MySQLdb
import sys

if len(sys.argv) != 4:
    sys.exit()
username = argv[1]
password = argv[2]
name = argv[3]
db = MySQLdb.connect(user=username, passwd=password, db=name)
cur = db.cursor()
cur.execute("SELECT * FROM hbtn_0e_0_usa.states ORDER BY id")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()
