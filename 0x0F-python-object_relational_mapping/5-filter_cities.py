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
    search = {'search': sys.argv[4]}
    cur = db.cursor()
    cur.execute("SELECT p2.name \
            FROM states p1, cities p2 \
            WHERE p1.id = p2.state_id AND p1.name = %(search)s \
            ORDER BY p2.id ASC", search)
    output = []
    for x in cur.fetchall():
        output.append(x[0])
    print(", ".join(output))
    cur.close()
    db.close()
