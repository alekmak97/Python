'''
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11
'''

var = input("Введите число ")
sum = 0
var1 = None
for i in var:
    try:
        var1 = int(i)
    except:
        continue
    sum = sum + var1
print("Sum=", sum)



'''
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''

while True:
    print("Enter number!!! ")
    try:
        N = int(input("Введите число "))
        break
    except:
        continue
F = []
for i in range(1, N+1):
    if i == 1:
        F = [1]
        continue
    F.append(F[i-2]*i)
print(F)


'''
3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
Это происходит до тех пор, пока не будет найден палиндром.
Напишите такую программу, которая найдет палиндром введенного пользователем числа.
'''

poli = str(input('Enter number: '))
poli1 = poli
poli2 = None
count = 0
while True:
    count += 1
    poli2 = ''.join(reversed(poli1))
    if poli1 == poli2:
        print("Полиндром:", poli2)
        print(f'Количество итераций: {count}')
        break
    else:
        p = int(poli1) + int(poli2)
        poli1 = str(p)



'''
4 - Реализуйте выдачу случайного числа
не использовать random.randint и вообще библиотеку random
Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
Учтите, что есть диапазон: от(минимальное) и до (максимальное)
'''
import time
import math


def R(x,y):
    r = float((y*2+y+10))
    re = y*2+y
    k = float(math.fabs(x+23) +math.fabs(y+45))

    while True:
        ns = float(time.time_ns())
        result = math.sin(ns/10)*math.cos(ns/100)*k*r
        k = math.sin(result)
        print(result)
        if (x>=0) and (y>=0):
            re = int(math.fabs(result))
        else:
            re = int(result)
        if x <= re <= y:
            break
    return re

v1 = int(input("First value: "))
v2 = int(input("Second value: "))
V = R(v1,v2)
print(V)









'''
Задайте список из n чисел последовательности (1+(1/n))^n и выведите на экран их сумму.
Пример:
- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
'''
n = int(input("Enter n "))
print({i: round((1+(1/i))**i, 1) for i in range(1, n+1)})


'''
Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
'''

N = int(input("Enter N "))
NN = list()
for i in range(-N,N+1):
    NN.append(i)
print(NN)
indexes = []
try:
    with open('file.txt', 'r') as file:
        indexes = file.read().split("\n")
except FileNotFoundError:
    print('Error')
for i in range(len(indexes)):
    indexes[i] = int(indexes[i])
indexes.sort()
res = 1
for i in indexes:
    try:
        res = res * NN[i]
        print(f'res = {res} * {NN[i]}, where i = {i}')
    except:
        print(f'i = {i}, not found')
        continue
print("res =", res)


'''
Реализуйте алгоритм перемешивания списка.
'''

nums = [45, 5, 689, -35, 76, -1]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
