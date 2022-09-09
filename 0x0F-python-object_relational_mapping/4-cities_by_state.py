#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    argv = sys.argv
    host = "localhost"
    port = 3306
    user = argv[1]
    passwd = argv[2]
    db_name = argv[3]
    db = MySQLdb.connect(
        host=host, port=port, user=user, passwd=passwd, db=db_name
        )
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM
    cities INNER JOIN states ON
    cities.state_id = states.id ORDER BY states.id ASC""")

    rows = cursor.fetchall()
    for row in rows:
        print(row)
