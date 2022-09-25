from datetime import datetime as dt

# сохранение данных
def save_data(res, act, x, y):
    time = dt.now().strftime("%Y/%m/%d, %H:%M:%S")
    with open('log.csv', 'a') as file:
        file.write(f"{time};{x};{act};{y};{res};\n")