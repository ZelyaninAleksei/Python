import random


def menu(filename):

    while True:
        try:
            user_num = int(input(
                " \n    Меню: \n\n 1. Просмотреть телефонную книгу \n 2. Найти запись \n 3. Внести запись \n 4. Изменить запись \n 5. Удалить запись \n 6. Для выхода \n \n Введите номер пункта: "))

            if 1<=user_num<=6:

                if user_num == 1:
                    viewing_the_phonebook(filename)
                elif user_num == 2:
                    request = input("\n Введите Фамилию или Имя: ")
                    search_person(request, filename)
                elif user_num == 3:
                    record(filename)
                elif user_num == 4:
                    change_record(filename)
                elif user_num == 5:
                    delete_record(filename)
                else:
                    quit()
        except ValueError:
            print("\033[31m Вы ввели буквы, необходимо вводить номер пункта меню\033[0m")


def viewing_the_phonebook(filename):

    print("")
    print("ID | Фамилия | Имя | Отчество | № телефона")

    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
        return_to_the_menu()


def return_to_the_menu():

    while True:
        temp_val = int(
            input("\n Вернуться в меню? \n 1 - да, вернуться \n 2 - нет, выйти из программы: \n"))
        if temp_val == 1:
            menu(filename)
        elif temp_val == 2:
            quit()
        else:
            print("Повторите ввод.")


def search_person(request, filename):

    flag = True
    print("")

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if request in line:
                print(line)
                flag = False
        if flag:
            print("\033[31mЗапись не найдена\033[0m")

    return_to_the_menu()


def record(filename):

    with open(filename, 'a', encoding='utf-8') as f:
        uid = generate_id()
        entry = input("Введите ФИО и телефон: ")
        f.write(f"{uid} {entry}\n")
    return_to_the_menu()


def generate_id():

    uid = ''
    for i in range(3):
        uid += str(random.randint(0, 9))
    return uid


def change_record(filename):

    record_id = input("Введите id записи, которую нужно изменить: ")
    new_record = input("Введите новую запись: ")

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    updated = False
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            if line.startswith(record_id):
                f.write(f"{record_id} {new_record}\n")
                updated = True
            else:
                f.write(line)

    if updated:
        print("Запись успешно изменена")
    else:
        print("Запись не найдена")

    return_to_the_menu()


def delete_record(filename):

    record_id = input("Введите id записи, которую нужно удалить: ")

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    removed = False
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            if not line.startswith(record_id):
                f.write(line)
            else:
                removed = True

    if removed:
        print("Запись успешно удалена")
    else:
        print("Запись не найдена")

    return_to_the_menu()


filename = r'Seminar 8\phonebook.txt'
menu(filename)
