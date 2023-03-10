# Найдите сумму цифр трехзначного числа. 
while True:
    user_num = input('Введите трёхзначное число: ')
    if user_num.isdigit() == False:
        print("Введите цифры, а не буквы, пожалуйста")
    elif len(user_num) != 3:
        print("Просили же 'Введите трёхзначное число' ")
    else:
        break
first_num = int(user_num)//100
second_num = int(user_num)%100//10
end_num=int(user_num)%10
sum = first_num+second_num+end_num

print('Введённое Вами число =', user_num, 'сумма цифр числа составляет ->', sum )