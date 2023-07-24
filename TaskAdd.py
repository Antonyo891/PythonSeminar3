'''дан некоторый список чисел, задача - найти сколько раз встречается введенная пользователем цифра
например был список [1,15,55,7.58,0,99]
и пользователь ввел 5
ответ будет 4'''
import os, random,decimal
os.system('cls')
list = [1,15,55,7.58,0,99]
print(list)
k=5
i=0
count=0
while i<len(list):
    while list[i]%1>0:
        list[i]=list[i]*10
    while list[i]>0:
        if list[i]%10==k:
            count+=1
        list[i]//=10
    i+=1
print(count)