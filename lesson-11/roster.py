import sqlite3
create="CREATE TABLE Roster(Name TEXT, Species TEXT, Age int );"
values=(
    ("Benjamin Sisko",	"Human",	40),
    ("Jadzia Dax",	"Trill",	300),
    ("Kira Nerys",	"Bajoran",	29)
)

with sqlite3.connect("roster.db") as con:
    cursor=con.cursor()
    cursor.execute("DROP TABLE IF EXISTS Roster")
    cursor.execute(create)
    cursor.executemany("INSERT INTO Roster VALUES(?, ?, ?);", values)
    