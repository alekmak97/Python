'''
Вычислить число c заданной точностью d
Пример:
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
'''
a1 = float(input('a = '))
b1 = float(input('b = '))
d1 = float(input('d = '))
c1 = ((a1/b1)//d1)*d1
print(c1)


'''
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
'''
def EnterCheckNumber():
    while True:
        try:
            n = int(input())
            break
        except:
            continue
    return n
def SimpleNumbers(N):
    if N == 1:
        nums = [1]
    if N == 2:
        nums = [1,2]
    if N >= 3:
        nums = [1,2,3]
        for i in range(4,N+1):
            trigger = True
            for j in range(1,i+1):
                if (i % j == 0) and (j<i) and j>1:
                    trigger = False
                    break
            if trigger:
                nums.append(i)
    return nums
print('N = ')
N2 = EnterCheckNumber()
SimpleNums2 = SimpleNumbers(N2)
SimpleDiv = []
for i in SimpleNums2:
    if (N2 % i == 0):
        SimpleDiv.append(i)
print(f"Простые делители для N = {N2}: {SimpleDiv}")




'''
Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
'''
import random
print('Ввведите число элементов последовательности: ')
N3 = EnterCheckNumber()
nums3 = []
for i in range(0,N3):
    nums3.append(random.randint(1,4))
print("List: ", nums3)
nums3new = []
for i in nums3:
    if i not in nums3new:
        nums3new.append(i)
print("Result: ", nums3new)




'''
Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''
print("k = ")
k4 = EnterCheckNumber()
for i in range(k4, -1, -1):
    file = open('text.txt', 'a', encoding='utf-8')
    if i == k4:
        k = random.randint(1,100)
        file.write(f'{k} * x^{i} ')
    if k4 > i > 1:
        k = random.randint(0, 100)
        if k != 0:
            file.write(f'+ {k} * x^{i} ')
    if i == 1:
        if k != 0:
            file.write(f'+ {k} * x ')
    if i == 0:
        k = random.randint(0, 100)
        if k != 0:
            file.write(f'+ {k} = 0')
        if k == 0:
            file.write(f'= 0')
    file.close()




'''
Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
'''



'''
В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
Нужно перезаписать файл.
Пример:
Ангела Меркель 5
Андрей Валетов 5
Фредди Меркури 3
Анастасия Пономарева 4

Программа выдаст:
АНГЕЛА МЕРКЕЛЬ 5
АНДРЕЙ ВАЛЕТОВ 5
Фредди Меркури 3
Анастасия Пономарева 4
'''
import re
with open('text.txt', 'w', encoding='utf-8') as file:
    file.write('Ангела Меркель 5\nАндрей Валетов 5\nФредди Меркури 3\nАнастасия Пономарева 4\n')
with open('text.txt', 'r', encoding='utf-8') as file:
    data = file.read().split('\n')
if len(data[-1]) == 0:
    data.pop(-1)
for i in range(0,len(data)):
    res = re.findall(r'5', data[i])
    if '5' in res:
        data[i] = str(data[i]).upper()
with open('text.txt', 'w', encoding='utf-8') as file:
    for i in data:
        file.write(i)
        file.write('\n')

'''
Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. 
При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. 
"вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
Сдвиг часто называют ключом шифрования.
Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, 
которая спрашивает ключ, считывает текст и дешифровывает его.
'''

# без файла, просто переменная
s = "АББА"
k = 1
def en(st, key):
    temp = []
    for i in st:
        temp.append(chr(ord(i)+key))
    new_st = ''.join(temp)
    return new_st
en_s = en(s,k)
print(en_s)
def de(st,key):
    temp = []
    for i in st:
        temp.append(chr(ord(i)-key))
    new_st = ''.join(temp)
    return new_st
de_s = de(en_s, k)
print(de_s)

'''
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
файл первый:
AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
файл второй:
сжатый текст.
'''

# без файлов
q = "AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool"

def rle_en(st):
    res = []
    count = 0
    if len(st) == 1:
        res.append((1, st[0]))
        return res
    for i in range(len(st)):
        count += 1
        if (i + 1) == len(st) or st[i] != st[i + 1]:
            res.append((count, st[i]))
            count = 0
    return res

en_q = rle_en(q)
print(en_q)

def rle_de(l):
    res = ''
    for i in l:
        res += i[0]*i[1]
    return res

de_q = rle_de(en_q)
print(de_q)



