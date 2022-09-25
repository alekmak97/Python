from comments import select_type_value as stv
from check import check_value_type as cvt
from comments import example_value as ev
from check import check_value_real as cvr
from check import check_value_complex as cvc
from comments import example_action as ea
from check import check_action as ca


# Отображение данных
def view_data(res, act, x, y):
    print()
    print(f'x = {x}, y = {y}, act = {act}')
    print()
    print(f"result = {x} {act} {y} = {res}")
    print()


# Ввод данных
def get_value(v, value_type):
    ev()
    while True:
        val = input(f"Enter value for {v}: ")
        if value_type == 1:
            value = cvr(val)
        else:
            value = cvc(val)
        if value == False:
            continue
        else:
            break
    return value


# Ввод типа переменной
def get_value_type(v):
    stv()
    while True:
        val_type = input(f"Enter value type for {v}: ")
        value = cvt(val_type)
        if 1 <= value <= 2:
            break
        else:
            continue
    return value


# Ввод действия
def get_action():
    ea()
    while True:
        val = input("Enter action: ")
        act = ca(val)
        if act == False:
            continue
        else:
            break
    return act