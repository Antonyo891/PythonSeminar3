'''адача №23. Общее обсуждение
Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
Примечание: Пользователь может вводить значения
списка или список задан изначально.'''
import os, random
os.system('cls')
array = []#[0, -1, 5, 2, 3]
for _ in range(random.randint(5,9)):
    array.append(random.randint(0,9))
i,j = 0,1
while j < len(array):
    if array[j-1]<array[j]:
        i+=1
    j+=1
print(array)
print(f'{i}')

