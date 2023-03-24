"""
3. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def print_info(name, surname, year_of_birth, address, email, telephone_number):
    print(f"{name} {surname} {year_of_birth} года рождения, проживает в городе {address},"
          f" email: {email}, телефон: {telephone_number}")


print_info(name="Иван", surname="Иванов", year_of_birth="1846",
           address="Москва", email="jackie@gmail.com", telephone_number="01005321456")

