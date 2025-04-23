# В коді є помилка. Логічна помилка (BUG). Код працює не коректно.
# https://gitlab.com/mykhailo_lazoryk/lms_2024
# lms_2024 / src / students / models.py

import datetime


# def age(self):
#     if self.birth_date:
#         return datetime.datetime.now().year - self.birth_date.year


class Student:
    def __init__(self, birth_date):
        self.birth_date = birth_date

    def age(self):
        if not self.birth_date:
            return None

        today = datetime.date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )


student = Student(birth_date=datetime.date(2000, 10, 10))
print(student.age())
