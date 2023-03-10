'''
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).

*Пример:*
3 2 4 -> yes
3 2 1 -> no
'''


def Enter_user_num(msg):
    x = input(f"Введите количество долек {msg} ")
    while True:
        if x.isdigit() == False:
            print("Введённое значение не является цифрой. Даже если написано 'много' )")
        elif x == 0:
            print(
                "Значение не может быть равно нулю. Если нет шоколадки то и не чего делить. К сожалению)")
        else:
            return x


def Checking_division(number_of_slices_horizontally, number_of_slices_vertical, desired_number_of_slices):
    if int(number_of_slices_horizontally)*int(number_of_slices_vertical) < int(desired_number_of_slices):
        print("Шоколадка меньше того, что Вы хотите. Ломать шоколадку не над3о.")
    elif int(number_of_slices_horizontally)*int(number_of_slices_vertical) == int(desired_number_of_slices):
        print(
            "Шоколадка ровно содержит столько долек сколько Вы и хотите. Забирайте её всю.")
    else:
        if (int(desired_number_of_slices) % int(number_of_slices_horizontally) == 0) or (int (desired_number_of_slices) % int(number_of_slices_vertical) == 0):
            print(
                f"От шоколадки размером {number_of_slices_horizontally} на {number_of_slices_vertical} МОЖНО отломить {desired_number_of_slices} долек одним разломом")
        else:
            print(
                f"От шоколадки размером {number_of_slices_horizontally} на {number_of_slices_vertical} НЕЛЬЗЯ отломить {desired_number_of_slices} долек одним разломом")


number_of_slices_horizontally = Enter_user_num("по горизонтали")
number_of_slices_vertical = Enter_user_num("по вертикали")
desired_number_of_slices = Enter_user_num(", которое хотите взять")
Checking_division(number_of_slices_horizontally,number_of_slices_vertical, desired_number_of_slices)
