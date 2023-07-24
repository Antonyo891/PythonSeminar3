'''адача №21. Решение в группах Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
Примечание: Список словарей задан изначально.
Пользователь его не вводит'''
import os, random
os.system('cls')
list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
#list1=str.lstrip([''])
set = set()
for i in list:
    for key,value in i.items():
        print(key.strip(),value.strip())
        if value.strip  not in set:
            set.add(value.strip())
print(set)