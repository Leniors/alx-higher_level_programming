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
    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=name,
        host='localhost',
        port=3306)
    cur = db.cursor()
    query = f"""
    SELECT cities.name
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = '{sys.argv[4]}'
    """
    cur.execute(query)
    rows = cur.fetchall()
    length = len(rows)
    for i in range(length):
        mylist = list(rows[i])
        if i < length - 1:
            print(mylist[0], end=", ")
        else:
            print(mylist[0])
