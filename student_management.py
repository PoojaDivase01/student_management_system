import sqlite3


class StudentManagement:

    def __init__(self):

        self.conn = sqlite3.connect("students.db")

        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(

            sid INTEGER PRIMARY KEY,

            name TEXT,

            marks INTEGER

        )
        """)

        self.conn.commit()

    # Add Student

    def add_student(self):

        sid = int(input("Enter Student ID: "))

        name = input("Enter Student Name: ")

        marks = int(input("Enter Marks: "))

        try:

            self.cursor.execute(

                "INSERT INTO students VALUES(?,?,?)",

                (sid, name, marks)

            )

            self.conn.commit()

            print("Student Added Successfully")

        except sqlite3.IntegrityError:

            print("Student ID already exists")

    # View Students

    def view_students(self):

        self.cursor.execute(

            "SELECT * FROM students"

        )

        records = self.cursor.fetchall()

        if len(records) == 0:

            print("No Records Found")

        else:

            print("\n{:<10}{:<20}{:<10}".format(

                "ID", "NAME", "MARKS"

            ))

            print("-" * 40)

            for row in records:

                print(

                    "{:<10}{:<20}{:<10}".format(

                        row[0],

                        row[1],

                        row[2]

                    )

                )

    # Search Student

    def search_student(self):

        sid = int(input("Enter Student ID: "))

        self.cursor.execute(

            "SELECT * FROM students WHERE sid=?",

            (sid,)

        )

        record = self.cursor.fetchone()

        if record:

            print("\nStudent Found")

            print("ID :", record[0])

            print("Name :", record[1])

            print("Marks :", record[2])

        else:

            print("Student Not Found")

    # Update Student

    def update_student(self):

        sid = int(input("Enter Student ID: "))

        name = input("Enter New Name: ")

        marks = int(input("Enter New Marks: "))

        self.cursor.execute(

            "UPDATE students SET name=?, marks=? WHERE sid=?",

            (name, marks, sid)

        )

        self.conn.commit()

        if self.cursor.rowcount > 0:

            print("Student Updated Successfully")

        else:

            print("Student Not Found")

    # Delete Student

    def delete_student(self):

        sid = int(input("Enter Student ID to Delete: "))

        self.cursor.execute(

            "DELETE FROM students WHERE sid=?",

            (sid,)

        )

        self.conn.commit()

        if self.cursor.rowcount > 0:

            print("Student Deleted Successfully")

        else:

            print("Student Not Found")

    # Close Database

    def close_connection(self):

        self.conn.close()


# Main Program

obj = StudentManagement()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")

    print("1. Add Student")

    print("2. View Students")

    print("3. Search Student")

    print("4. Update Student")

    print("5. Delete Student")

    print("6. Exit")

    try:

        choice = int(input("Enter Choice: "))

    except ValueError:

        print("Please enter numbers only")

        continue

    if choice == 1:

        obj.add_student()

    elif choice == 2:

        obj.view_students()

    elif choice == 3:

        obj.search_student()

    elif choice == 4:

        obj.update_student()

    elif choice == 5:

        obj.delete_student()

    elif choice == 6:

        obj.close_connection()

        print("Thank You")

        break

    else:

        print("Invalid Choice")