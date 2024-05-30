import sqlite3


class Courses():
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT NOT NULL,
        instructor TEXT NOT NULL
        )
        """)

        self.cursor.close()

    def add_course(self, course_name, instructor):
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
            INSERT INTO courses (course_name, instructor) VALUES (?, ?)
        """, (course_name, instructor))

        self.connection.commit()
        self.cursor.close()

    def get_course(self, course_id):
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
        SELECT * FROM courses WHERE course_id = ?
        """, (course_id,))

        fetchall = self.cursor.fetchall()
        self.cursor.close()
        return fetchall

    def get_all_course(self):
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
        SELECT * FROM courses
        """)

        fetchall = self.cursor.fetchall()
        self.cursor.close()
        return fetchall

    def update_student(self, course_id, course_name=None, instructor=None):
        self.cursor = self.connection.cursor()

        if course_name:
            self.cursor.execute("""
            UPDATE students SET course_name = ? WHERE course_id = ?
            """, (course_name, course_id))

        if instructor:
            self.cursor.execute("""
            UPDATE students SET instructor = ? WHERE course_id = ?
            """, (instructor, course_id))

        self.connection.commit()
        self.cursor.close()

    def delete_student(self, course_id):
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
        DELETE FROM courses WHERE course_id = ?
        """, (course_id,))

        self.connection.commit()
        self.cursor.close()