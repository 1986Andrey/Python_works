class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        return sum(all_grades) / len(all_grades)


    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.average_grade()}\n' \
              f'Курсы в процессе изучения: {self.courses_in_progress}\n' \
              f'Завершенные курсы: {self.finished_courses}'
        return res



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        return sum(all_grades) / len(all_grades)

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.average_grade()}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}'
        return res



def get_average_students_grades(students, course):
    all_grades = []
    for student in students:
        if course in student.courses_attached:
            all_grades.extend(student.grades[course])
    return sum(all_grades) / len(all_grades)



def get_average_lecturers_grades(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            all_grades.extend(lecturer.grades[course])
    return sum(all_grades) / len(all_grades)



students = [Student('Ruoy', 'Eman', 'your_gender'), Student('Hue', 'Ueu', 'your_gender')]
students[0].courses_in_progress += ['Python']
students[0].finished_courses += ['Введение в программирование']
students[1].courses_in_progress += ['Git']
students[1].finished_courses += ['Введение в программирование']


lecturers = [Lecturer('Some', 'Buddy'), Lecturer('Another', 'Buddy')]
lecturers[0].courses_attached += ['Python']
lecturers[1].courses_attached += ['Git']


reviewers = [Reviewer('Reviewer', 'Buddy'), Reviewer('This', 'Buddy')]
reviewers[0].courses_attached += ['Python']
reviewers[1].courses_attached += ['Git']


reviewers[0].rate_hw(students[0], 'Python', 10)
reviewers[0].rate_hw(students[0], 'Python', 3)
reviewers[1].rate_hw(students[1], 'Git', 10)
reviewers[1].rate_hw(students[1], 'Git', 4)


students[0].rate_lecture(lecturers[0], 'Python', 9)
students[0].rate_lecture(lecturers[0], 'Python', 5)
students[1].rate_lecture(lecturers[1], 'Git', 3)
students[1].rate_lecture(lecturers[1], 'Git', 10)


print('Студенты, по возрастанию средней оценки:\n')
for student in sorted(students):
    print(f'{student}\n')
print('\nЛекторы, по возрастанию средней оценки:\n')
for lecturer in sorted(lecturers):
    print(f'{lecturer}\n')
print('\nРевьюверы:\n')
for reviewer in reviewers:
    print(f'{reviewer}\n')