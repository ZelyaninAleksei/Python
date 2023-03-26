'''
 Напишите рекурсивную функцию sum(a, b), 
 возвращающую сумму двух целых неотрицательных чисел. 
 Из всех арифметических операций допускаются только 
 +1 и -1. Также нельзя использовать циклы.

*Пример:*

2 2
    4
'''


def Enter_user_num(msg):
    while True:
        try:
            t_num = int(input(f"Введите целое неотрицательное число {msg}: "))
            if t_num <= 0:
                print("Введите неотрицательное число.")
                continue
            return t_num
        except ValueError:
            print("Введите цифру")


def Sum(max_number, min_number):
    if min_number == 0:
        return max_number
    else:
        return Sum(max_number+1, min_number-1)


# Ввод данных
first_number = Enter_user_num("а")
second_number = Enter_user_num("b")

if first_number >= second_number:
    result_sum = Sum(first_number, second_number)
else:
    result_sum = Sum(second_number, first_number)

print(f"Результат сложения {first_number} + {second_number} = {result_sum}")
