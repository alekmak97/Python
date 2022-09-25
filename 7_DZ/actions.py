
# Выполнение действия над числами
def action(act,x,y):
    if act == '+' : return x+y
    elif act == '-' : return x-y
    elif act == '*' : return x*y
    elif act == '/' : return x/y
    elif act == '^' and type(y) != type(3-5j) : return x**y
    else:
        return 'Error'

# Выход из приложения
def exit_from_calc():
    print("Для выхода из калькулятора введите любой символ и нажмите Enter, для продолжения просто нажмите Enter")
    status = input()
    if status == '':
        return True
    else:
        return False