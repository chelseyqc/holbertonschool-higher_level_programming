#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    # connects to database (host, user, passwd, db)
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    # create cursor to exec queries
    cursor = db.cursor()
    # execute query
    cursor.execute("SELECT * FROM states ORDER BY id;")
    # fetches the rows returned by query
    rows = cursor.fetchall()
    # iterate and prints rows
    for row in rows:
        print(row)
    # close cursor and database connection
    cursor.close()
    db.close()
