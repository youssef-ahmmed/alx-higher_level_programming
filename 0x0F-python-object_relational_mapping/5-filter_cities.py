#!/usr/bin/python3
"""script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(
        host='localhost', user=username,
        passwd=password, db=database, port=3306
    )

    cur = db.cursor()

    query = """
        SELECT c.name
        FROM cities c
        INNER JOIN states s ON c.state_id = s.id
        WHERE s.name=%s
    """
    cur.execute(query, (sys.argv[4], ))

    rows = cur.fetchall()

    formatted_data = ', '.join(item[0] for item in rows)
    print(formatted_data)

    cur.close()
    db.close()
