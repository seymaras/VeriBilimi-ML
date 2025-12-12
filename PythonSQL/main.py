import sqlite3
import os

def create_database():
    if os.path.exists("students.db"):
        os.remove("students.db")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    return conn, cursor

def create_tables(cursor):
    cursor.execute('''
    CREATE TABLE Students (
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL,
        age INTEGER,
        email VARCHAR UNIQUE,
        city VARCHAR)
        
        
    ''')

    cursor.execute('''
    CREATE TABLE COURSES (
        id    INTEGER PRIMARY KEY,
        course_name  VARCHAR NOT NULL,
        instructor   TEXT,
        credits INTEGER)
 ''')



def insert_sample_data(cursor):
    students = [
        (1, 'Alice Johnson', 21, 'alice@gmail.com','New York'),
        (2, 'Bob Smith', 19, 'bob@gmail.com', 'Chigago'),
        (3, 'Carol Whitr', 21, 'alice@gmail.com', 'Boston'),
        (4, 'David Brown', 20, 'alice@gmail.com', 'New York'),
        (5, 'Emma Davis', 22, 'alice@gmail.com', 'SEattle'),
    ]

def main():
    conn, cursor = create_database()

    try:
        create_tables(cursor)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()

if __name__== "__main__":
    main()