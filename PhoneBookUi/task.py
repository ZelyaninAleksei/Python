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


# with open('file.json', 'w+') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# def open_file():


# def add_item():


import tkinter as tk
from tkinter import messagebox


def viewing_the_phonebook(filename):
    """Функция для просмотра содержимого телефонной книги."""
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
    messagebox.showinfo("Телефонная книга", data)


def search_person(request, filename):
    """Функция для поиска записи в телефонной книге по запросу."""
    flag = True
    with open(filename, 'r') as f:
        for line in f:
            if request in line:
                messagebox.showinfo("Результат поиска", line)
                flag = False
        if flag:
            messagebox.showerror("Ошибка", "Запись не найдена")


def record(filename):
    """Функция для добавления новой записи в телефонную книгу."""
    x = input_box.get().capitalize()
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(x + "\n")
    input_box.delete(0, tk.END)
    messagebox.showinfo("Успех", "Запись добавлена в телефонную книгу")


def menu():
    """Функция для создания графического интерфейса меню."""
    window = tk.Tk()
    window.title("Телефонная книга")
    window.geometry("420x200")

    # Создание элементов интерфейса
    label = tk.Label(window, text="Меню:")
    label.grid(row=0, column=0)

    button1 = tk.Button(window, text="Просмотреть телефонную книгу", command=lambda: viewing_the_phonebook(filename))
    button1.grid(row=1, column=0)

    label2 = tk.Label(window, text="Введите Фамилию или Имя:")
    label2.grid(row=2, column=0)

    search_box = tk.Entry(window)
    search_box.grid(row=2, column=1)

    button2 = tk.Button(window, text="Найти запись", command=lambda: search_person(search_box.get(), filename))
    button2.grid(row=2, column=2)

    label3 = tk.Label(window, text="Введите ФИО и телефон:")
    label3.grid(row=3, column=0)

    global input_box
    input_box = tk.Entry(window)
    input_box.grid(row=3, column=1)

    button3 = tk.Button(window, text="Внести запись", command=lambda: record(filename))
    button3.grid(row=3, column=2)

    button4 = tk.Button(window, text="Выход", command=window.quit)
    button4.grid(row=4, column=0)

    window.mainloop()


filename = r'PhoneBookUI\phonebook_GUI.txt'
menu()
