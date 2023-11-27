#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities of
that state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    # connect database
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    # create cursor
    cursor = db.cursor()
    # injection free query
    query = """SELECT cities.name FROM states\
        JOIN cities ON states.id = cities.state_id WHERE states.name = %s\
            ORDER BY cities.id ASC;"""
    param_tuple = (sys.argv[4],)
    # execute query
    cursor.execute(query, param_tuple)
    # fetch cities returned by query
    rows = cursor.fetchall()
    # empty tuple to hold row values
    cities_list = ()
    # iterate through rows and print
    for row in rows:
        cities_list = cities_list + row
    # join row values into comma separated string
    cities_string = ', '.join(cities_list)
    # print string of row values
    print(cities_string)
    # close cursor and database connection
    cursor.close()
    db.close()
