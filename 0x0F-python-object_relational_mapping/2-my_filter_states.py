#!/usr/bin/python3
"""
Scribt that lists all states from a database
where name maches the argument
"""

import MySQLdb
import sys

if (len(sys.argv) == 5):
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    data = cur.fetchall()
    for row in data:
        if (row[1] == sys.argv[4]):
            print(row)
    db.close()


if "__name__" == "__main__":
    main()
