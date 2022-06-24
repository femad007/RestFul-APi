


import sqlite3


connection = sqlite3.connect('data.db')

cursor = connection.cursor() #### cursor excuete the query and store the result

create_table = 'Create table if Not Exists users (id INTEGER PRIMARY KEY, username text, password text)'

cursor.execute(create_table)

connection.commit()
connection.close()
