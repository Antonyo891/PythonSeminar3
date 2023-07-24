'''Задача №19. Дана последовательность из N целых чисел и число K. 
Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, 
K – положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
Примечание: Пользователь может вводить значения
списка или список задан изначально.'''
import os,random
os.system('cls')
list_1 = [1,2,3,4,5]
#for i in range(random.randint(3,5)):
#    list_1.append(random.randint(0,5))
print (list_1)
offset =3 #random.randint(1,3)
print(list_1[offset-1:] + list_1[:offset-1])
for i in range(len(list_1)-offset):
    list_1.insert(len(list_1),(list_1.pop(0)))
print (offset,list_1,sep="--")
