#!/usr/bin/python3
import MySQLdb

db = MySQLdb.connect(host='localhost', user='root', passwd='root', db='hbtn_0e_4_usa')
cur = db.cursor()
cur.execute("SHOW TABLES FROM hbtn_0e_4_usa")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()
