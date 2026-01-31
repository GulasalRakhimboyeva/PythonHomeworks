import sqlite3
connection=sqlite3.connect("test.db")

connection.close()

connection=sqlite3.connect(":memory:")


type(connection)

s=",".join(['?']* 3)

print(s)