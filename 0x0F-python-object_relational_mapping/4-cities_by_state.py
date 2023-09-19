#!/usr/bin/python3
"""
Scribt that lists all states from a database
and prevent sql injection
"""
import MySQLdb
import sys

if (len(sys.argv) == 4):
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT c.name, s.name, c.id\
            FROM cities as c\
            INNER JOIN states as s ON s.id = c.state_id ORDER BY c.id ASC")
    data = cur.fetchall()
    for row in data:
        print(row)
    db.close()


if "__name__" == "__main__":
    main()
