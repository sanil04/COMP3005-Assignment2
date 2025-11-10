import psycopg2



def connect():
    
    # Connect to DB
    
    return psycopg2.connect(
        dbname="postgres", user="postgres", password="$Iforgot7", host="localhost", port="5432"
    )



def getAllStudents():

    #getAllStudents(): Retrieves and displays all records from the students table.

    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("SELECT * FROM students;")

        rows = cur.fetchall()
        print("All Students:")
        for row in rows:
            print(row)

        cur.close()
        conn.close()


    except Exception as e:
        print(f"Error retrieving students: {e}")






def addStudent(first_name, last_name, email, enrollment_date):

    #addStudent(first_name, last_name, email, enrollment_date): Inserts a new student record into the students table.

    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
            (first_name, last_name, email, enrollment_date))
        
        conn.commit()
        print("Student added successfully.")

        cur.close()
        conn.close()


    except Exception as e:
        print(f"Error adding student: {e}")






def updateStudentEmail(student_id, new_email):

    #updateStudentEmail(student_id, new_email): Updates the email address for a student with the specified student_id.

    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute(
            "UPDATE students SET email = %s WHERE student_id = %s;",
            (new_email, student_id))
        
        conn.commit()
        print("Student email updated successfully.")

        cur.close()
        conn.close()


    except Exception as e:
        print(f"Error updating student email: {e}")



def deleteStudent(student_id):

    #deleteStudent(student_id): Deletes the record of the student with the specified student_id.

    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute(
            "DELETE FROM students WHERE student_id = %s;",
            (student_id,))
        
        conn.commit()
        print("Student deleted successfully.")

        cur.close()
        conn.close()


    except Exception as e:
        print(f"Error deleting student: {e}")


def menu():

    #prints out menu
    
    print("CRUD Application Menu:")
    print("1. View All Students")
    print("2. Add New Student")
    print("3. Update Student Email")
    print("4. Delete Student")
    print("5. Exit")


if __name__ == "__main__":


    print("Welcome to the CRUD Application!")
    print("Here is a list of all students in the database:")
    print("---------------------------------------------------")
    getAllStudents()

    stayInLoop = 0

    while (stayInLoop == 0):

        print(" ")

        menu()
        input_choice = input("Please enter your choice (1-5): ")

        print(" ")

        if input_choice == '1':
            getAllStudents()
        

        elif input_choice == '2':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)

        elif input_choice == '3':
            student_id = input("Enter student ID to update: ")
            new_email = input("Enter new email: ")
            updateStudentEmail(student_id, new_email)

        elif input_choice == '4':
            student_id = input("Enter student ID to delete: ")
            deleteStudent(student_id)

        elif input_choice == '5':
            print("Exiting the application. Goodbye!")
            stayInLoop = 1

        else:
            print("Invalid choice. Please try again.")
        
        print(" ")



    
