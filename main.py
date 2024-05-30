from db_func.students import *
from db_func.courses import *
from db_func.course_group import *

student_db = Student()
courses_db = Courses()
course_groups_db = Course_groups()

while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Вийти")

    choice = input("Оберіть опцію (1-7): ")

    if choice == "1":
        student_name = input("\nВведіть ім'я студента ")
        student_age = int(input("Введіть вік студента "))

        student_db.add_student(student_name, student_age)
        print("Доданно")
    # Додавання нового студента

    elif choice == "2":
        course_name = input("\nНазва курса ")
        course_instructor = input("Ім'я вчителя ")

        courses_db.add_course(course_name, course_instructor)
        print("Доданно")
    # Додавання нового курсу

    elif choice == "3":
        print()
        print(student_db.get_all_students())
    # Показати список студентів

    elif choice == "4":
        print()
        print(courses_db.get_all_course())
    # Показати список курсів

    elif choice == "5":
        student_id = int(input("\nID Студента "))
        course_id = int(input("ID Курса "))

        course_groups_db.add_course_groups(course_id, student_id)
        print("Доданно")

    # Зареєструвати студента на курс

    elif choice == "6":
        course_id = int(input("\nВведіть ID курса "))
        print()

        for i in course_groups_db.get_course_groups(course_id):
            print(student_db.get_students(i[2]))

    # Показати студентів на конкретному курсі

    elif choice == "7":
        break

    else:
        print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")