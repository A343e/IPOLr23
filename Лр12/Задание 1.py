class Student:
    def __init__(self, name, group_number, grades):
        self.name = name
        self.group_number = group_number
        self.grades = grades


def main():
    # Создаем массив из десяти структур типа Student
    students = []
    for i in range(10):
        name = input(f"Введите фамилию и инициалы студента {i + 1}: ")
        group_number = input(f"Введите номер группы студента {i + 1}: ")
        grades = [int(input(f"Введите оценку {j + 1} для студента {i + 1}: ")) for j in range(5)]

        student = Student(name, group_number, grades)
        students.append(student)

    # Выводим на дисплей фамилии и номера групп студентов с неудовлетворительными отметками
    print("\nСтуденты с неудовлетворительными отметками:")
    for student in students:
        if any(grade < 4 for grade in student.grades):
            print(f"Фамилия и инициалы: {student.name}, Номер группы: {student.group_number}")

if __name__ == "__main__":
    main()
