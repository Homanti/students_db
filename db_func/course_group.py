import sqlite3


class Course_groups():
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS course_groups (
        course_groups_id INTEGER PRIMARY KEY,
        course_id INTEGER NOT NULL,
        student_id INTEGER NOT NULL
        )
        """)

        self.cursor.close()

    def add_course_groups(self, course_id, student_id):
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
            INSERT INTO course_groups (course_id, student_id) VALUES (?, ?)
        """, (course_id, student_id))

        self.connection.commit()
        self.cursor.close()

    def get_course_groups(self, course_id):
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
        SELECT * FROM course_groups WHERE course_id = ?
        """, (course_id,))

        fetchall = self.cursor.fetchall()
        self.cursor.close()
        return fetchall

    def update_course_groups(self, course_groups_id, course_id=None, student_id=None):
        self.cursor = self.connection.cursor()

        if course_id:
            self.cursor.execute("""
            UPDATE course_groups SET course_id = ? WHERE course_groups_id = ?
            """, (course_id, student_id))

        if student_id:
            self.cursor.execute("""
            UPDATE course_groups SET age = ? WHERE course_groups_id = ?
            """, (student_id, course_groups_id))

        self.connection.commit()
        self.cursor.close()

    def delete_course_groups(self, course_groups_id):
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
        DELETE FROM course_groups WHERE course_groups_id = ?
        """, (course_groups_id,))

        self.connection.commit()
        self.cursor.close()