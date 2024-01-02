'''

Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions
'''
from fractions import Fraction

first_fraction = input("Введите дробь в формате a/b: ")
second_fraction = input("Введите дробь в формате c/d: ")


def add_fraction(a, b, c, d):
    numerator, denominator = a * d + b * c, b * d
    return f"{numerator}/{denominator}"


def mult_fraction(a, b, c, d):
    numerator, denominator = a * c, b * d
    return f"{numerator}/{denominator}"


print(mult_fraction(int(first_fraction[0]), int(first_fraction[2]), int(second_fraction[0]), int(second_fraction[2])))
a = Fraction(3, 4)
b = Fraction(5, 7)
print(a * b)
