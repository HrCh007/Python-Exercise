import sqlite3

# Exercise 1: Connect to your database server and print its version

def get_connection():
    connection = sqlite3.connect('python_db.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def read_database_version():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("select sqlite_version();")
        db_version = cursor.fetchone()
        print("You are connected to SQLite version: ", db_version)
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print("Error while getting data", error)

print("Question 1: Print Database version")
read_database_version()
print('\n')

# Question 2: Fetch Hospital and Doctor Information using hospital Id and doctor Id

def get_hospital_detail(hospital_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Hospital where Hospital_Id = ?"""
        cursor.execute(select_query, (hospital_id,))
        records = cursor.fetchall()
        print("Printing Hospital record")
        print(records)
        for row in records:
            print("Hospital Id:", row[0], )
            print("Hospital Name:", row[1])
            print("Bed Count:", row[2])
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print("Error while getting data", error)

def get_doctor_detail(doctor_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Doctor where Doctor_Id = ?"""
        cursor.execute(select_query, (doctor_id,))
        records = cursor.fetchall()
        print("Printing Doctor record")
        for row in records:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6])
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print("Error while getting data", error)

print("Question 2: Read given hospital and doctor details \n")
get_hospital_detail(2)
print("\n")
get_doctor_detail(105)
print('\n')

# 