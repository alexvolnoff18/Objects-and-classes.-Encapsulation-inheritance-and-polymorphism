class Student:
    def __init__(self, name, surname, gender):
        """Конструирует класс студентов ('Student') с атрибутами: имя(name), 
        фамилия(surname), пол(gender), оконченные курся(finished_courses)
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
        информацию о экземпляре класса "Student": имя, фамилия, средняя оценка
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
        и средний балл за длекции(grade_point_average)
        """
        super().__init__(name, surname)
        self.grades = {}
        self.grade_point_average = float()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if grade > 10 or grade < 0:
            print("Ошибка. Оценки выставляются по десятибалльной шкале")
        else:
            if isinstance(student,
                          Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return "Ошибка"

    def __str__(self):
        output = f"Имя: {self.name}\n" \
                 f"Фамилия: {self.surname}\n"
        return output


course_lecturer = Lecturer('Some', 'Buddy')
course_lecturer.courses_attached += ['Python']

student = Student('Ruoy', 'Eman', 'your_gender')
student.courses_in_progress += ['Python']
student.rate_lect(course_lecturer, 'Python', 12)
student.rate_lect(course_lecturer, 'Python', 10)
student.rate_lect(course_lecturer, 'Python', 7)
print(course_lecturer.grades)

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']

reviewer = Reviewer('Some', 'Buddy')
reviewer.courses_attached += ['Python']

reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'Python', 15)
reviewer.rate_hw(student, 'Python', 8)
print(course_lecturer.grades)
print(student)
print(reviewer)

# print(best_student.grades)
# print(course_reviewer.name)
