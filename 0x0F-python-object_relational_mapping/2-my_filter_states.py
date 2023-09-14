#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
import sys

if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(
        host='localhost', user=username,
        passwd=password, db=database, port=3306
    )

    cur = db.cursor()

    query = "SELECT * FROM states WHERE states.name=%s"
    cur.execute(query, (sys.argv[4], ))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
