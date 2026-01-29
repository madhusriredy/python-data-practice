import pandas as pd
import sqlite3

df = pd.read_csv("users.csv")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    email TEXT
)
""")

for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO users VALUES (?, ?)",
        (row["name"], row["email"])
    )

conn.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

conn.close()
