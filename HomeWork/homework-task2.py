'''
Петя, Катя и Сережа делают из бумаги журавликов. Вместе
они сделали S журавликов. Сколько журавликов сделал каждый
ребенок, если известно, что Петя и Сережа сделали одинаковое
количество журавликов, а Катя сделала в два раза больше журавликов,
чем Петя и Сережа вместе?
'''
number_of_cranes = input('Введите общее количество журавлей -> ')

if number_of_cranes.isdigit() == False:
        print("Введите цифры, а не буквы, пожалуйста")
else:
        if float(number_of_cranes) % 6 != 0:
                print("Кто-то из ребят филонил и не делал журавликов.")
        else:
                x = int(number_of_cranes)/6
                cranes_Kate = x*4
                cranes_male = x
                print(f"Общее количество журавликов {int(number_of_cranes)} из которых: \n Катя сделала {int(cranes_Kate)}, а Петя и Серёжа сделали по {int(cranes_male)} ")
       