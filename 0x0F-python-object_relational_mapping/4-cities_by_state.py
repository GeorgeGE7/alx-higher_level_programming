#!/usr/bin/python3
""" a script that lists all cities from the database hbtn_0e_4_usa """
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
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    all_rows = cur.fetchall()
    for row in all_rows:
        print(row)
    cur.close()
    db.close()
