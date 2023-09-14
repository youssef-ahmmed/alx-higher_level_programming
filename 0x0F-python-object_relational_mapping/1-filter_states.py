#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(
        host='localhost', user=username,
        passwd=password, db=database, port=3306
    )

    cur = db.cursor()

    query = "SELECT * FROM states WHERE states.name LIKE 'N%'"
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
