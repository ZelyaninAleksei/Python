# Найдите сумму цифр трехзначного числа. Вариант 2 (с использованием функции)
def Summing_Digits(user_num):
    sum = 0
    while user_num != 0:
        sum += user_num % 10
        user_num = user_num//10
    return sum


while True:
    user_num = input('Введите трёхзначное число: ')
    if user_num.isdigit() == False:
        print("Введите цифры, а не буквы, пожалуйста")
    elif len(user_num) != 3:
        print("Просили же 'Введите трёхзначное число' ")
    else:
        break

print('Введённое Вами число =', user_num, 
      ', сумма цифр числа составляет ->', Summing_Digits(int(user_num)))
