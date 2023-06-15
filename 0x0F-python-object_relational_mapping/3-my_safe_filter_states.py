#!/usr/bin/python3
"""script that lists all states from
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
    data = {'var1': sys.argv[4]}
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE \
            BINARY %(var1)s ORDER BY id ASC""", data)
    for state in cur.fetchall():
        print(state)
    cur.close()
    db.close()
