#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Has to take 3 arguments:
    argv[1]: username
    argv[2]: password
    argv[3] database name.
    Results must be sorted in ascending order by states.id."""
    temp = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = temp.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    temp.close()
