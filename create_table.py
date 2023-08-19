import sqlite3

# Create a connection to the database (creates a new database if it doesn't exist)
conn = sqlite3.connect('database/login_database.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store login information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Insert sample login records
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("user1", "password123"))
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("user2", "securepass"))

# Commit changes and close the connection
conn.commit()
conn.close()
 
