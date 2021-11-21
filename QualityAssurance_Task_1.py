import sys

import numpy as np
import math

class Task_1:
    def __init__(self, var):
        self.var = var

    def InitData(self):
        if self.var == 2:  # Аня
            self.sizeFile = 60 * 10**3  # Размер файла, байт
            self.sizeMTU_1 = 1410  # Значение MTU 1-го сегмента
            self.sizeMTU_2 = 700  # Значение MTU 2-го сегмента
            self.sizeMTU_3 = 1460  # Значение MTU 3-го сегмента
        elif self.var == 8:  # Андрей
            self.sizeFile = 100 * 10**3  # Размер файла, байт
            self.sizeMTU_1 = 1410  # Значение MTU 1-го сегмента
            self.sizeMTU_2 = 500  # Значение MTU 2-го сегмента
            self.sizeMTU_3 = 1400  # Значение MTU 3-го сегмента
        else:
            print("Неправильно указан номер варианта")
            sys.exit()

    def Cycle(self):
        self.InitData()
        self.Ask()


    def Ask(self):
        # Сетевой сегмент 3

        MSS_3 = self.sizeMTU_3 - 40
        print(f"\nВ начале сервер отдает пакеты в 3-й сегмент сети, где MTU = {self.sizeMTU_3} байт. Размер файла {self.sizeFile} байт."
              f"\nСегменты файла инкапсулируются в TCP и IP (20 + 20 байт)."
              f"\nТо есть MSS для 3-го сетевого сегмента составит MSS =  MTU - 40 = {self.sizeMTU_3 - 40} байт")
        count_packeges_after_MTU = math.ceil(self.sizeFile / (self.sizeMTU_3 - 40))
        remainder = self.sizeFile - math.floor(self.sizeFile / (self.sizeMTU_3 - 40)) * (self.sizeMTU_3 - 40)  # остаток
        print(f"Файл, после прохождение через 3-й сетевой сегмент, разделится на {count_packeges_after_MTU} пакетов,"
              f"\n\tиз которых {count_packeges_after_MTU - 1} пакет содержит 40 байт (TCP и IP адреса)"
              f"\n\tи {MSS_3} байт передаваемого сегмента."
              f"\n\tА оконечный пакет содержит 40 байт (TCP и IP) и {remainder} байт."
              f"\nИтог после 3-го сетевого сегмента:"
              f"\n\tКоличество IP пакетов:"
              f"\n\t\t{count_packeges_after_MTU - 1} шт. каждая по {self.sizeMTU_3} байт"
              f"\n\t\t1 шт.(конец) - {remainder} байт")

        # Сетевой сегмент 2

        MSS_2 = self.sizeMTU_2 - 40
        print(f"\n\nДалее пакеты попадают во 2-ой сетевой сегмент."
              f"\nMTU размер которого равен {self.sizeMTU_2}. И соответственно MSS (без учета IP и TCP) равен {MSS_2}."
              f"Размер пакета, поступившего в сегмент сети больше чем MTU, следовательно он будет разбит на две части."
              f"")



if __name__ == "__main__":
    Work = Task_1(8)
    Work.Cycle()

    # Задание:
    # Рассчитать:
    # Обьем данных и количество пакетов информации, которые
    #   Переданы сервером
    #   Приняты оборудованием пользователя
    #       без учета фазы установления и завершения TCP/IP соединения
    # На сколько процентов скорость приема данных на стороне пользователя ...
    #   должна быть выше скорости передачи данных сервером?