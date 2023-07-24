'''Задача №17. Решение в группах Дан список чисел. Определите, сколько в нем
встречается различных чисел. Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6 Примечание: Пользователь может вводить значения
списка или список задан изначально.'''
import os,random
os.system('cls')
list_1 = []
set = set()
for i in range(random.randint(3,15)):
    list_1.append(random.randint(0,5))
    set.add(list_1[i])
print (list_1)
print(f'{set} - {len(set)} лементов')
i=0
while i<len(list_1):
    j=i+1
    while j<len(list_1):
        if list_1[j]==list_1[i]:
            list_1.pop(j)
        else:
            j+=1  
    i+=1
print(f'В списке {len(list_1)} различных элементов')