import random

# Генерация фейковых ФИО
def generate_name():
    first_names = ['Иван', 'Петр', 'Сергей', 'Андрей', 'Максим', 'Дмитрий', 'Александр', 'Алексей']
    last_names = ['Иванов', 'Петров', 'Сергеев', 'Андреев', 'Максимов', 'Дмитриев', 'Александров', 'Алексеев']
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Генерация фейкового телефона
def generate_phone():
    phone = '+7'
    for i in range(10):
        phone += str(random.randint(0, 9))
    return phone

# Создание файла с 1000 записей
with open('phonebook.txt', 'w') as f:
    for i in range(10):
        name = generate_name()
        phone = generate_phone()
        f.write(f"{name},{phone}\n")