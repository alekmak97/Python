from comments import Hello as Hi
from actions import action as act
from actions import exit_from_calc as ec
from view import *
from logger import save_data


def Calc():
    Hi() # Приветствие
    while True: # Цикл для непрерывных вычислений
        value_x = get_value('x', get_value_type('x')) # задание типа и значения для переменной
        value_y = get_value('y', get_value_type('y')) # задание типа и значения для переменной
        value_act = get_action()# задание действия над переменными
        result = act(value_act, value_x, value_y) # вычисление результата
        save_data(result, value_act, value_x, value_y) # сохранение данных в заранее преднастроенный файл
        view_data(result, value_act, value_x, value_y) # отображение результата

        # Ниже условия для выхода из приложения / продолжения работы
        status = ec()
        if status: continue
        else: break
