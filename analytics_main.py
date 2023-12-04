import numpy as np # библиотека для работы с массивами
import matplotlib.pyplot as plt # библиотека для работы с графиками

# ФУНКЦИЯ преобразования 2 списков -> в 2 массива
def get_data(chat_id, period, points):
    x_array = np.array(period) # создаем массив значений по X
    y_array = np.array(points) # создаем массив значений по Y
    photo = create_plot(chat_id, x_array, y_array) # передаем номер чата и 2 массива в следующую функцию
    return photo

# ФУНКЦИЯ построения графика (Баллы по Y, Время по X)
def create_plot(chat_id, x_array, y_array): 
    plt.subplots() # создаем оси
    plt.title(f"Прогресс ученика {chat_id}") # подписываем название графика вверху
    plt.xlabel("Время") # подписываем ось X
    plt.ylabel("Баллы") # подписываем ось Y
    plt.plot(x_array, y_array) # строим график в виде кривой, соединяющей точки
    plt.grid(True) # включаем сетку для удобства


    photo = f'./analytics/plots/plt_{chat_id}.png'
    plt.savefig(photo) # сохраняем график как файл-картинку
    return photo