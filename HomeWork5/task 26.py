'''
Напишите программу, которая на вход 
принимает два числа A и B, и возводит 
число А в целую степень B с помощью 
рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 
    '''


def Enter_user_num(msg):

    while True:
        try:
            tmp_num = int(input(f'Введите {msg} -> '))
            return tmp_num

        except ValueError:
            print("Введены некорректные данные. Введите цифры.")


def Exponentiation(number, degree):

    if degree == 1:
        return number

    else:
        return int(number) * Exponentiation(int(number), int(degree) - 1)

number = Enter_user_num("число")
degree = Enter_user_num("степень")
numberindegree = Exponentiation(int(number), int(degree))

print(f"Число {number} в степени {degree} равно {numberindegree}")
