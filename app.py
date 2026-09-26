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


def print_application(application):
    print("\n--------------------------")
    print("ID:", application[0])
    print("Company:", application[1])
    print("Position:", application[2])
    print("Location:", application[3])
    print("Status:", application[4])
    print("Date Applied:", application[5])


def view_applications():
    connection = sqlite3.connect("internships.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM applications")

    applications = cursor.fetchall()

    connection.close()

    if len(applications) == 0:
        print("No applications found.")
        return

    print("\nYour Applications:")

    for application in applications:
        print_application(application)


    print_application(application)

def main():
    while True:
        print("\n=== Internship Tracker ===")
        print("1. Add application")
        print("2. View applications")
        print("3. Delete application")
        print("4. Update application status")
        print("5. Search by company")
        print("6. Filter by status")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_application()

        elif choice == "2":
            view_applications()

        elif choice == "3":
            delete_application()

        elif choice == "4":
            update_status()

        elif choice == "5":
            search_by_company()

        elif choice == "6":
            filter_by_status()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


def delete_application():
    view_applications()

    application_id = input("Enter the ID of the application to delete: ")

    connection = sqlite3.connect("internships.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM applications WHERE id = ?", (application_id,))
    connection.commit()

    print("Application deleted!")



def update_status():
    view_applications()

    application_id = input("\nEnter the ID of the application to update: ")
    new_status = input("Enter the new status: ")

    connection = sqlite3.connect("internships.db")
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE applications SET status = ? WHERE id = ?",
        (new_status, application_id)
    )

    connection.commit()
    connection.close()

    print("Application status updated.")



def search_by_company():
    company = input("Enter company name: ")

    connection = sqlite3.connect("internships.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM applications WHERE company LIKE ?",
        ("%" + company + "%",)
    )

    applications = cursor.fetchall()

    connection.close()

    if len(applications) == 0:
        print("No applications found.")
        return

    print("\nSearch Results:")

    for application in applications:
        print_application(application)


def filter_by_status():
    status = input("Enter the status to filter by: ")

    connection = sqlite3.connect("internships.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM applications WHERE status = ?",
        (status,)
    )

    applications = cursor.fetchall()

    connection.close()

    if len(applications) == 0:
        print("No applications found.")
        return

    print("\nFiltered Results:")

    for application in applications:
        print_application(application)

main()