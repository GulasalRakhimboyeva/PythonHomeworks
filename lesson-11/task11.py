import sqlite3

# =========================
# TASK 1: roster.db
# =========================

conn1 = sqlite3.connect("roster.db")
cursor1 = conn1.cursor()

# Create table
cursor1.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# Clear table (safe re-run)
cursor1.execute("DELETE FROM Roster")

# Insert data
cursor1.executemany("""
INSERT INTO Roster (Name, Species, Age)
VALUES (?, ?, ?)
""", [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])

# Update name
cursor1.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")

# Query Bajoran characters
print("Bajoran characters:")
cursor1.execute("""
SELECT Name, Age FROM Roster
WHERE Species = 'Bajoran'
""")
print(cursor1.fetchall())

# Delete characters over 100 years old
cursor1.execute("""
DELETE FROM Roster
WHERE Age > 100
""")

# Add Rank column (ignore error if exists)
try:
    cursor1.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")
except sqlite3.OperationalError:
    pass

# Update ranks
cursor1.execute("UPDATE Roster SET Rank = 'Captain' WHERE Name = 'Benjamin Sisko'")
cursor1.execute("UPDATE Roster SET Rank = 'Lieutenant' WHERE Name = 'Ezri Dax'")
cursor1.execute("UPDATE Roster SET Rank = 'Major' WHERE Name = 'Kira Nerys'")

# Advanced query
print("\nRoster sorted by age (DESC):")
cursor1.execute("""
SELECT * FROM Roster
ORDER BY Age DESC
""")
print(cursor1.fetchall())

conn1.commit()
conn1.close()


# =========================
# TASK 2: library.db
# =========================

conn2 = sqlite3.connect("library.db")
cursor2 = conn2.cursor()

# Create table
cursor2.execute("""
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)
""")

# Clear table (safe re-run)
cursor2.execute("DELETE FROM Books")

# Insert data
cursor2.executemany("""
INSERT INTO Books (Title, Author, Year_Published, Genre)
VALUES (?, ?, ?, ?)
""", [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
])

# Update year
cursor2.execute("""
UPDATE Books
SET Year_Published = 1950
WHERE Title = '1984'
""")

# Query dystopian books
print("\nDystopian books:")
cursor2.execute("""
SELECT Title, Author FROM Books
WHERE Genre = 'Dystopian'
""")
print(cursor2.fetchall())

# Delete books before 1950
cursor2.execute("""
DELETE FROM Books
WHERE Year_Published < 1950
""")

# Add Rating column (ignore error if exists)
try:
    cursor2.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
except sqlite3.OperationalError:
    pass

# Update ratings
cursor2.execute("UPDATE Books SET Rating = 4.8 WHERE Title = 'To Kill a Mockingbird'")
cursor2.execute("UPDATE Books SET Rating = 4.7 WHERE Title = '1984'")
cursor2.execute("UPDATE Books SET Rating = 4.5 WHERE Title = 'The Great Gatsby'")

# Advanced query
print("\nBooks sorted by year (ASC):")
cursor2.execute("""
SELECT * FROM Books
ORDER BY Year_Published ASC
""")
print(cursor2.fetchall())

conn2.commit()
conn2.close()
