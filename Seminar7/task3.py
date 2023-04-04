# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

# Ввод:                                    Вывод:
# values = [0, 2, 10, 6]                      same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)




def same_by(characteristic, objects):
    if not objects:
        return True
    first_value = characteristic(objects[0])
    for obj in objects[1:]:
        if characteristic(obj) != first_value:
            return False
    return True

values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values):
    print("same")
else:
    print("different")
    
    
values = [0, 3, 10, 6] 

def same_by(func, input_values):
    result = list(map(func, input_values))
    return min(result) == max(result)

print(same_by(lambda x: x % 2, values))

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
    values = [0, 3, 10, 6] 

def same_by(func, input_values):
    result = list(map(func, input_values))
    return min(result) == max(result)

print(same_by(lambda x: x % 2, values))

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')