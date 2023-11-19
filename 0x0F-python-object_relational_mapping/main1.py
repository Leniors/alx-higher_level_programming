#!/usr/bin/python3
import MySQLdb

db = MySQLdb.connect(host='localhost', user='root', passwd='root', db='mydata')
cur = db.cursor()
cur.execute("SELECT id, name FROM mydata.first_table ORDER BY id")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()
