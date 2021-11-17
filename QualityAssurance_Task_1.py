import numpy as np

class Task_1:
    def __init__(self, var):
        self.var = var

    def InitData(self):
        if self.var == 2:  # Аня
            self.sizeFile = 60000
            self.sizeMTU_1 = 1410
            self.sizeMTU_2 = 700
            self.sizeMTU_3 = 1460
        if self.var == 9:  # Андрей
            self.sizeFile = 60000
            self.sizeMTU_1 = 1410
            self.sizeMTU_2 = 700
            self.sizeMTU_3 = 1460

if __name__ == "__main__":
    Work = Task_1(2)
    Work.One()