'''
Напишите программу для печати всех уникальных 
значений в словаре. 
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII 
":" S007 "}] 
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
Примечание: Список словарей задан изначально. 
Пользователь его не вводит
'''

my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
my_set = set()
for item in my_list:
    for val in item.values():
        my_set.add(val.strip())

print(my_set)

print (set(val.strip() for dic in my_list for val in dic.values()))