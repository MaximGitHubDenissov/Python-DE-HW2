'''
Напишите программу, которая получает целое число и
возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
'''
HEX = 16

num = int(input("Введите целое число: "))


def num_to_hex(number):
    result = ''
    while number != 0:
        digit = number % HEX
        if digit == 10:
            digit = "A"
        elif digit == 11:
            digit = "B"
        elif digit == 12:
            digit = "C"
        elif digit == 13:
            digit = "D"
        elif digit == 14:
            digit = "E"
        elif digit == 15:
            digit = "F"
        else:
            digit = str(digit)
        result = digit + result
        number //= HEX
    return result


print(num_to_hex(num))
print(hex(num))
