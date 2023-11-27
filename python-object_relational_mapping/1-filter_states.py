#!/usr/bin/python3
"""lists all states with a name starting with N"""
import MySQLdb
import sys

if __name__ == "__main__":
    # connects to database (host, user, pw, db)
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    # create cursor to exec query
    cursor = db.cursor()
    # execute query
    cursor.execute("SELECT * FROM states"
                   "WHERE BINARY name LIKE 'N%' ORDER BY id;")
    # fetch rows returned by query
    rows = cursor.fetchall()
    # iterate and print rows
    for row in rows:
        print(row)
    # close cursor and database connection
    cursor.close()
    db.close()
