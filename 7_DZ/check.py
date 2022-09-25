
# Проверка рационального числа
def check_value_real(val):
    try:
        value = float(val)
        return value
    except:
        print('Некорректные данные')
        return False

# Проверка комплексного числа
def check_value_complex(val):
    try:
        value = complex(val)
        return value
    except:
        print('Некорректные данные')
        return False

# Проверка типа значения
def check_value_type(value_type):
    try:
        val_type = int(value_type)
        if 1 <= val_type <= 2:
            return val_type
        else:
            print('Некорректные данные')
            return False
    except:
        print('Некорректные данные')
        return False


# Проверка действия
def check_action(act):
    if act == '*' or act == '/' or act == '+' or act == '-' or act == '^':
        return act
    else:
        print('Некорректные данные')
        return False
