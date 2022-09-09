#!/usr/bin/python3
"""that takes in the name of a state as an argument
and lists all cities of that state"""
import sys
import MySQLdb


if __name__ == "__main__":
    argv = sys.argv
    host = "localhost"
    port = 3306
    user = argv[1]
    passwd = argv[2]
    db_name = argv[3]
    name = argv[4]
    db = MySQLdb.connect(
        host=host, port=port, user=user, passwd=passwd, db=db_name
        )
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM
    cities INNER JOIN states ON
    cities.state_id = states.id WHERE states.name = %s ORDER
    BY states.id ASC""", (name, ))

    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))
