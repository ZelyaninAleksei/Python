# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# id, lastname, firstname, secondname, phone


def menu(filename):

    while True:

        user_num = int(input(
            " \n    Меню: \n\n 1. Просмотреть телефонную книгу \n 2. Найти запись \n 3. Внести запись \n 4. Для выхода \n \n Введите номер пункта: "))

        if user_num == 1 or user_num == 2 or user_num == 3:

            if user_num == 1:
                viewing_the_phonebook(filename)
            elif user_num == 2:
                request = input("\n Введите Фамилию или Имя: ")
                search_person(request, filename)
            elif user_num == 3:
                record(filename)

        elif user_num == 4:
            quit()
        else:
            print("Некорректный ввод. Повторите ввод")


def viewing_the_phonebook(filename):
        
        print("")
        
        with open(filename, 'r') as f:
            print(f.read())
            return_to_the_menu()

# def viewing_the_phonebook(filename):
#     with open(filename, 'r') as f:
#         for line in f:
#             print(line)
#     return_to_the_menu()

def return_to_the_menu():

    while True:
        temp_val = int(
            input("Вернуться в меню? \n 1 - да, вернуться \n 2 - нет, выйти из программы: \n"))
        if temp_val == 1:
            menu(filename)
        elif temp_val == 2:
            quit()
        else:
            print("Повторите ввод.")


def search_person(request, filename):
    
    flag = True
    print("")
    with open(filename, 'r') as f:
        
        for line in f:
            
            if request in line:
                print(line)
                flag = False
                
        if flag:    
                print("\033[31mЗапись не найдена\033[0m \n")
                
    return_to_the_menu()
    

def record(filename):
    with open(filename, 'a') as f:
        x = input("Внесите ФИО и телефон:")
        f.writelines(x + "\n")
    return_to_the_menu()

# 1 Выбор пункта меню (есть)
filename = r'C:\Users\super\Desktop\Учёба\GB\Python\Seminar 8\phonebook.txt'
enter_user = menu(filename)
