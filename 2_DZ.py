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
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''

N = int(input("Введите число "))
F = []
for i in range(1, N+1):
    if i == 1:
        F = [1]
        continue
    F.append(F[i-2]*i)
print(F)



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
