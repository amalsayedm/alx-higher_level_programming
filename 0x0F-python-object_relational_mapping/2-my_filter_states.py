#!/usr/bin/python3
""" Select states with names matching arguments """


if __name__ == '__main__':

    from sys import argv
    import MySQLdb

    user = argv[1]
    passwd = argv[2]
    name = argv[3]
    state_name = argv[4]

    database = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=user,
                               passwd=passwd,
                               db=name)

    cursor = database.cursor()

    cursor.execute('SELECT id, name FROM states\
                   WHERE states.name = \'{}\'\
                   ORDER BY states.id ASC'.format(state_name))

    for row in cursor.fetchall():
        print(row)
