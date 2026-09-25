import sqlite3


def add_application():
    company = input("Company: ")
    position = input("Position: ")
    location = input("Location: ")
    status = input("Status: ")
    date_applied = input("Date applied: ")

    connection = sqlite3.connect("internships.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO applications
        (company, position, location, status, date_applied)
        VALUES (?, ?, ?, ?, ?)
        """,
        (company, position, location, status, date_applied)
    )

    connection.commit()
    connection.close()

    print("Application added!")


add_application()