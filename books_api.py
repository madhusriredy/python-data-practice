import sqlite3

# simulated API data
books = [
    {"title": "Clean Code", "author": "Robert Martin", "year": 2008},
    {"title": "Python Crash Course", "author": "Eric Matthes", "year": 2016}
]

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    title TEXT,
    author TEXT,
    year INTEGER
)
""")

for book in books:
    cursor.execute(
        "INSERT INTO books VALUES (?, ?, ?)",
        (book["title"], book["author"], book["year"])
    )

conn.commit()

cursor.execute("SELECT * FROM books")
for row in cursor.fetchall():
    print(row)

conn.close()
