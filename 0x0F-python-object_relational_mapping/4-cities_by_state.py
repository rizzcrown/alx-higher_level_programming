#!/usr/bin/python3
"""script that lists all cities from
the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    """main function"""
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT p2.id, p2.name, p1.name \
            FROM states p1, cities p2 \
            WHERE p1.id = p2.state_id ORDER BY p2.id ASC")
    for state in cur.fetchall():
        print(state)
    cur.close()
    db.close()
