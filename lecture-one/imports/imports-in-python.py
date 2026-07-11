"""
- Modules get used all the time throughout programming
- It helps with creating more files, with unique purposes, to help with clean maintainable code
"""

import grade_average_service

home_assignment_grades = {
    'homework_1': 85,
    'homework_2': 100,
    'homework_3': 81,
}

grade_average_service.calculate_homework(home_assignment_grades)

"""Agar biz module dan aynan kerakli bir method yoki 
variable ni import qilmoqchi bolsak from keywordidan foydalanamiz.
syntax: => from grade_average_service import age
! from keywordidan foydalanganda method yoki variable dan foydalanishda module name dan foydalinmaydi
"""

from grade_average_service import age
print(age)
