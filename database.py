import sqlite3


def create_database():
    connection = sqlite3.connect("internships.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            position TEXT NOT NULL,
            location TEXT,
            status TEXT NOT NULL,
            date_applied TEXT
        )
    """)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_database()
    print("Database created successfully.")