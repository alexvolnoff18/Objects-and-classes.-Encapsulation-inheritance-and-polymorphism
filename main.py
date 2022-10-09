class Student:
    def __init__(self, name, surname, gender):
        """Конструирует класс студентов ('Student') с атрибутами: имя(name), 
        фамилия(surname), пол(gender), оконченные курсы(finished_courses)
        изучаемые курсы(courses_in_progress), оценки за домашние задания (grades)
        и средний балл за домашние задания(grade_point_average)
        """
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grade_point_average = float()

    def rate_lect(self, lecturer, course, grade):
        """Реализует возможность выставления оценок по десятибалльной шкале лекторам
        (Lecturer) у класса Student, если лектор ведет курс у студента
        """
        if grade > 10 or grade < 0:
            print("Ошибка. Оценки выставляются по десятибалльной шкале")
        else:
            if isinstance(lecturer,
                          Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return "Ошибка"

    def __str__(self):
        """Рассчитывает средний балл за домашнее задание и выводит
        информацию о экземпляре класса 'Student': имя, фамилия, средняя оценка
        за домашнее задание, курсы в процессе изучения, завершенные курсы
        """
        grades_count = 0
        courses_in_progress_str = ", ".join(self.courses_in_progress)
        finished_courses_str = ", ".join(self.finished_courses)
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.grade_point_average = sum(map(sum, self.grades.values())) / grades_count
        output = f"Имя: {self.name}\n" \
                 f"Фамилия: {self.surname}\n" \
                 f"Средняя оценка за домашние задания: {self.grade_point_average}\n" \
                 f"Курсы в процессе изучения: {courses_in_progress_str}\n" \
                 f"Завершенные курсы: {finished_courses_str}\n"

        return output

    def __lt__(self, other):
        """Реализует возможность сравнения студентов междусобой 
        (через операторы сравнения <,>) по средней оценке за домашние задания.
        """
        if not isinstance(other, Student):
            print("Некорректное сравнение!")
            return
        return self.grade_point_average < other.grade_point_average


class Mentor:
    def __init__(self, name, surname):
        """Конструирует класс преподавателей ('Mentor') с атрибутами: имя(name), 
        фамилия(surname), преподаваемый курс(courses_attached)
        """
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        """Конструирует наследуемый от класса 'Mentor' класс лекторов ('Lecturer') 
        с атрибутами: имя(name), фамилия(surname), оценки за лекции (grades)
        и средний балл за лекции(grade_point_average)
        """
        super().__init__(name, surname)
        self.grades = {}
        self.grade_point_average = float()

    def __str__(self):
        """Рассчитывает средний балл за домашнее задание и выводит нформацию
        о экземпляре класса 'Lecturer': имя, фамилия, средняя оценка
        за лекции, курсы в процессе изучения, завершенные курсы
        """
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.grade_point_average = sum(map(sum, self.grades.values())) / grades_count
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.grade_point_average}'
        return output

    def __lt__(self, other):
        """Реализует возможность сравнения лекторов междусобой
        (через операторы сравнения <,>) по средней оценке за домашние задания"""
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.grade_point_average < other.grade_point_average


class Reviewer(Mentor):
    """Конструирует наследуемый от класса 'Mentor' класс проверяющих ('Reviewer')"""

    def rate_hw(self, student, course, grade):
        """Реализует возможность выставления оценок за домашние заданияпо десятибалльной шкале студентам
        (Student) у класса Reviewer, если Reviewer ведет курс у студента"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        """Овыводит нформацию о экземпляре класса 'Reviewer': имя, фамилия"""
        output = f"Имя: {self.name}\n" \
                 f"Фамилия: {self.surname}\n"
        return output


# Создаем лекторов
course_lecturer_1 = Lecturer('Иоан', 'Ивашкин')
course_lecturer_1.courses_attached += ['Python']

course_lecturer_2 = Lecturer('Джон', 'Голопупкин')
course_lecturer_2.courses_attached += ['C++']

course_lecturer_3 = Lecturer('Алибек', 'Суходрищев')
course_lecturer_3.courses_attached += ['Java']

# Создаем проверяющих
cool_reviewer_1 = Reviewer('Александр', 'Бородач')
cool_reviewer_1.courses_attached += ['Python', 'C++']

cool_reviewer_2 = Reviewer('Федор', 'Емельяненко')
cool_reviewer_2.courses_attached += ['C++']

cool_reviewer_3 = Reviewer('Тайсон', 'Фьюри')
cool_reviewer_3.courses_attached += ['Java']

# Создаем студентов
student_1 = Student('Дэни', 'Филт', "Муж.")
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Промышленное зельеварение']

student_2 = Student('Мерлин', 'Менсон', "Муж.")
student_2.courses_in_progress += ['C++']
student_2.finished_courses += ['Колыбельные от А до Я']

student_3 = Student('Володя', 'Бектяшкин', "Мальчик")
student_3.courses_in_progress += ['Java']
student_3.finished_courses += ['АК74 с нуля']

# Выставляем оценки лекторам
student_1.rate_lect(course_lecturer_1, 'Python', 10)
student_1.rate_lect(course_lecturer_1, 'Python', 7)
student_1.rate_lect(course_lecturer_1, 'Python', 8)

student_2.rate_lect(course_lecturer_2, 'C++', 9)
student_2.rate_lect(course_lecturer_2, 'C++', 10)
student_2.rate_lect(course_lecturer_2, 'C++', 6)

student_3.rate_lect(course_lecturer_3, 'Java', 10)
student_3.rate_lect(course_lecturer_3, 'Java', 10)
student_3.rate_lect(course_lecturer_3, 'Java', 10)

# Выставляем оценки студентам
cool_reviewer_1.rate_hw(student_1, 'Python', 5)
cool_reviewer_1.rate_hw(student_1, 'Python', 7)
cool_reviewer_1.rate_hw(student_1, 'Python', 7)

cool_reviewer_2.rate_hw(student_2, 'C++', 9)
cool_reviewer_2.rate_hw(student_2, 'C++', 9)
cool_reviewer_2.rate_hw(student_2, 'C++', 9)

cool_reviewer_3.rate_hw(student_3, 'Java', 10)
cool_reviewer_3.rate_hw(student_3, 'Java', 9)
cool_reviewer_3.rate_hw(student_3, 'Java', 9)

# Выводим список студентов:
print(f'Список студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}')

# Выводим список лекторов:
print(f'Список лекторов:\n\n{course_lecturer_1}\n\n{course_lecturer_2}\n\n{course_lecturer_3}')

# Выводим список проверяющих:
print(f'Список проверяющих:\n\n{cool_reviewer_1}\n\n{cool_reviewer_2}\n\n{cool_reviewer_3}')

# Выводим результат сравнения студентов по средним оценкам за домашние задания
print(f'Результат сравнения студентов: '
      f'{student_1.name} {student_1.surname} > {student_2.name} {student_2.surname} = {student_1 < student_2}')

# Выводим результат сравнения лекторов по средним оценкам за лекции
print(f'Результат сравнения лекторов: '
      f'{course_lecturer_1.name} {course_lecturer_1.surname} < {course_lecturer_3.name} {course_lecturer_3.surname}\
      = {course_lecturer_1 > course_lecturer_3}')

# Создаем список студентов
student_list = [student_1, student_2, student_3]

# Создаем список лекторов
lecturer_list = [course_lecturer_1, course_lecturer_2, course_lecturer_3]


def student_rating(student_list, course_name):
    """Функция для подсчета средней оценки за домашние задания по всем студентам
    в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса
    """
    sum_all = 0
    count_all = 0
    for stud in student_list:
        if stud.courses_in_progress == [course_name]:
            sum_all += stud.grade_point_average
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")


def lecturer_rating(lecturer_list, course_name):
    """Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
    (в качестве аргумента принимаем список лекторов и название курса)
    """
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.grade_point_average
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")

