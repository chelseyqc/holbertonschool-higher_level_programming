#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    # connects to database
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    # create cursor to exec query
    cursor = db.cursor()
    # execute query
    cursor.execute("SELECT cities.id, cities.name, states.name\
                   FROM states JOIN cities ON states.id = cities.state_id \
                   ORDER BY cities.id;")
    # fetch rows returned by query
    rows = cursor.fetchall()
    # iterate and print rows
    for row in rows:
        print(row)
    # close cursor and database connection
    cursor.close()
    db.close()
