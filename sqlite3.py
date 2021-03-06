#Create connection
import sqlite3
from sqlite3 import Error
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

if os.path.exists("mydatabase.sql"):
    os.remove("mydatabase.sql")

def sql_connection():

    try:
        connection = sqlite3.connect('mydatabase.sql')
        return connection

    except Error:
        print(Error)


#Create Table
def sql_table(connection):

    cursorObj = connection.cursor()
    cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
    connection.commit()

connection = sql_connection()
sql_table(connection)


#Insert entities = PUT
def sql_insert(connection, entities):

    cursorObj = connection.cursor()
    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    connection.commit()

entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
sql_insert(connection, entities)


#Update Table
def sql_update(connection):

    cursorObj = connection.cursor()
    cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')
    connection.commit()

sql_update(connection)


#Fetch data
def sql_fetch(connection):

    cursorObj = connection.cursor()
    #cursorObj.execute('SELECT * FROM employees')
    cursorObj.execute('SELECT id, name FROM employees WHERE salary > 100.0')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

sql_fetch(connection)