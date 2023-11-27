#!/usr/bin/python3
"""takes in arguments and displays all values in the states table
    where name matches the argument but is safe from MySQL injections"""
import MySQLdb
import sys

if __name__ == "__main__":
    # connects to database
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    # create cursor to exec query
    cursor = db.cursor()
    query = """SELECT * FROM states WHERE BINARY name = %s ORDER BY id;"""
    # tuple for parameters
    param_tuple = (sys.argv[4],)
    # execute query
    cursor.execute(query, param_tuple)
    # fetch rows returned by query
    rows = cursor.fetchall()
    # iterate and print rows
    for row in rows:
        print(row)
    # close cursor and database connection
    cursor.close()
    db.close()
