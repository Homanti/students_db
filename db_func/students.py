import sqlite3


class Student():
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
        )
        """)

        self.cursor.close()

    def add_student(self, name, age):
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
            INSERT INTO students (name, age) VALUES (?, ?)
        """, (name, age))

        self.connection.commit()
        self.cursor.close()

    def get_students(self, student_id):
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
        SELECT * FROM students WHERE student_id = ?
        """, (student_id,))

        fetchall = self.cursor.fetchall()
        self.cursor.close()
        return fetchall

    def get_all_students(self):
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
        SELECT * FROM students
        """)

        fetchall = self.cursor.fetchall()
        self.cursor.close()
        return fetchall

    def update_student(self, student_id, name=None, age=None):
        self.cursor = self.connection.cursor()

        if name:
            self.cursor.execute("""
            UPDATE students SET name = ? WHERE student_id = ?
            """, (name, student_id))

        if age:
            self.cursor.execute("""
            UPDATE students SET age = ? WHERE student_id = ?
            """, (age, student_id))

        self.connection.commit()
        self.cursor.close()

    def delete_student(self, student_id):
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
        DELETE FROM students WHERE student_id = ?
        """, (student_id,))

        self.connection.commit()
        self.cursor.close()