#!/usr/bin/python3
"""takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."""
import sys
import MySQLdb


if __name__ == "__main__":
    argv = sys.argv
    host = "localhost"
    port = 3306
    user = argv[1]
    passwd = argv[2]
    db_name = argv[3]
    enter = argv[4]
    db = MySQLdb.connect(
        host=host, port=port, user=user, passwd=passwd, db=db_name
        )
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name
                    LIKE BINARY '{}' ORDER BY states.id ASC""".format(enter))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
