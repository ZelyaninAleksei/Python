# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

# Ввод:                                           Вывод:
# print_operation_table(lambda x, y: x * y)       1 2  3  4  5  6
#                                                 2 4  6  8  10 12
#                                                 3 6  9  12 15 18
#                                                 4 8  12 16 20 24
#                                                 5 10 15 20 25 30
#                                                 6 12 18 24 30 36




# print_operation_table(operation, num_rows=6, num_columns=6),


def enter_user_num(msg):
    while True:
        try:
            local_num = int(input(f"Введите количество {msg}, которое должно быть распечатано: ")) 
            return local_num
        except ValueError:
            print("Внесены некорректные данные. Повторите ввод.")


def print_operation_table(operation, num_rows, num_cols):
    
    table = []
    
    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            value = (i + 1) * (j + 1)
            row.append(value)
        table.append(row)
    
    for row in table:
        print(row)
    

num_rows = enter_user_num("строк")
num_colu = enter_user_num("столбцов")
print_operation_table(print, num_rows, num_colu)