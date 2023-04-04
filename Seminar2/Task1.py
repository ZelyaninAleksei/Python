'''
По данному целому неотрицательному n вычислите 
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех 
чисел от 1 до N) 0! = 1 Решить задачу используя цикл 
while

Input: 5
Output: 120
'''
def Enter_user_num(msg):
    while True:
        x = input(msg)
        if x.isdigit() == False:
            print("Некорректный ввод значения.")
        elif int(x) == 0:
            x = 1
            return x
        else:
            return x
        
def Calculating_Factorial(user_num):
    i = 1
    factorial = 1
    while int(i) <= int(user_num):
        factorial *= i
        i += 1
    return factorial

user_num = Enter_user_num("Введите целое неотрицательное число: ")
factorial_user_num = Calculating_Factorial(user_num)
print(f'Факториал числа {user_num} составляет {factorial_user_num}')

