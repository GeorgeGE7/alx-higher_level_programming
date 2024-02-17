#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa:
- Your script should take 3 arguments
"""
import MySQLdb
import sys


if __name__ == "__main__":
    dbHost="localhost"
    dbUser=sys.argv[1]
    dbPasswd=sys.argv[2]
    dbName=sys.argv[3]
    listingPort=3306
    db = MySQLdb.connect(host=dbHost, user=dbUser,
                         passwd=dbPasswd, db=dbName, port=listingPort)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
