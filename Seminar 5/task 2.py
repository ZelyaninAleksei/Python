# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def simplicity_check(num, i):

    while i < num:
        if num % i == 0:
            break
        i=+1
       


num = int(input("Ввелите число:"))
i=2
simplicity_check(num, i)