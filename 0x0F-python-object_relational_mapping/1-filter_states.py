#!/usr/bin/python3
""" Select states starting with N from database """

from sys import argv
import MySQLdb

if __name__ == '__main__':

    user = argv[1]
    passwd = argv[2]
    name = argv[3]

    database = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=user,
                               passwd=passwd,
                               db=name)

    cursor = database.cursor()

    cursor.execute('SELECT * FROM states ORDER BY states.id ASC')

    for row in cursor.fetchall():
        if row[1][0] == 'N':
            print(row)
