import math
import random

'''
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
Пример:

- 6 -> да
- 7 -> да
- 1 -> нет
'''
day = int(input('Enter day of week: '))
if 1 <= day <= 5:
    print('Workday')
elif 6 <= day <= 7:
    print('Weekend')
else:
    print("day did not find")


'''
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
'''
print("Проверка утверждения для всех знавчений предикат: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z")
XYZ = 0
X_Y_Z = 2**3
c = 0
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            A = not (x or y or z)
            B = (not x) and (not y) and (not z)
            if A == B:
                XYZ += 1
if XYZ == X_Y_Z:
    print("Утверждение верно")
else:
    print("Утверждение неверно")


'''
Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
в которой находится эта точка (или на какой оси она находится).
Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
'''
x = random.randint(-10, 10)
y = random.randint(-10, 10)
print("x =", x, "y =", y)
if x>0 and y>0: print("Q1")
elif x<0 and y>0: print("Q2")
elif x<0 and y<0: print("Q3")
elif x>0 and y<0: print("Q4")
elif x == 0 and y != 0: print("Y")
elif x != 0 and y == 0: print("X")
else: print("Центр осей координат")


'''
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
'''
Q = random.randint(1,4)
print("Четверть:", Q)
if Q == 1 : print("x(0, +∞), y(0, +∞)")
elif Q == 2 : print("x(-∞, 0), y(0, +∞)")
elif Q == 3 : print("x(-∞, 0), y(-∞, 0)")
elif Q == 4 : print("x(0, +∞), y(-∞, 0)")
else: print("Error")


'''
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
'''

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

def inputXY (XY):
    print("Point", namestr(XY, globals()))
    x = int(input("Введите координату x: "))
    XY.append(x)
    y = int(input("Введите координату y: "))
    XY.append(y)
    return XY

A = []
B = []
inputXY(A)
inputXY(B)
print("A", A)
print("B", B)

res = round(math.sqrt(math.pow(B[0]-A[0], 2) + math.pow(B[1]-A[1], 2)), 2)
print("Расстояние между точками:", res)
