import sys

import numpy as np

class Task_1:
    def __init__(self, var):
        self.var = var

    def InitData(self):
        if self.var == 2:  # Аня
            self.sizeFile = 60 * 10**3  # Размер файла, байт
            self.sizeMTU_1 = 1410  # Значение MTU 1-го сегмента
            self.sizeMTU_2 = 700  # Значение MTU 2-го сегмента
            self.sizeMTU_3 = 1460  # Значение MTU 3-го сегмента
        elif self.var == 9:  # Андрей
            self.sizeFile = 200 * 10**3  # Размер файла, байт
            self.sizeMTU_1 = 1410  # Значение MTU 1-го сегмента
            self.sizeMTU_2 = 1350  # Значение MTU 2-го сегмента
            self.sizeMTU_3 = 1420  # Значение MTU 3-го сегмента
        else:
            print("Неправильно указан номер варианта")
            sys.exit()

    def One(self):
        self.InitData()



if __name__ == "__main__":
    Work = Task_1(10)
    Work.One()

    # Задание:
    # Рассчитать:
    # Обьем данных и количество пакетов информации, которые
    #   Переданы сервером
    #   Приняты оборудованием пользователя
    #       без учета фазы установления и завершения TCP/IP соединения
    # На сколько процентов скорость приема данных на стороне пользователя ...
    #   должна быть выше скорости передачи данных сервером?