#!/usr/bin/python3
"""takes in an argument and displays all values in the states table
    where name matches the argument"""
import MySQLdb
import sys

if __name__ == "__main__":
    # connects to database (host, user, pw, db)
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    # create cursor to exec query
    cursor = db.cursor()
    # execute query
    cursor.execute("SELECT * FROM states \
                   WHERE BINARY name = '{}' \
                   ORDER BY id;".format(sys.argv[4]))
    # fetch rows returned by query
    rows = cursor.fetchall()
    # iterate and print rows
    for row in rows:
        print(row)
    # close cursor and database connection
    cursor.close()
    db.close()
