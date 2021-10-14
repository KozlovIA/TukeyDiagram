# Программа компании Igorexy Dev, ураденная с GitHub https://github.com/KozlovIA
# Качайте приложение https://play.google.com/store/apps/details?id=com.DefaultCompany.RollBall - рекламная интеграция за 15 рублей, поддержите начинающего разработчика
                                                                                                # я 25$ отдал за аккаунт разработчика((((
# переменная x везде означает выборку, это не тупое имя, а логичное, т.к. в тетради тоже самое
from os import read
# А может import pandas? или import хотя бы Statistics ?    #include <iostream> //  using System.Math;

class TukeyDiagram():
    def __init__(self) -> None:
        pass

    def Bubble_Sort(self, x):  # За использование этой гениальной сортировки я уже не прошел интервью. Хотя какой sort(), это ж в C++;
        # Стоп это что python???? Что я делаю??? Зачем???!!!    Остановите меня, пожалуйста!!!!!!!;;;;
        checker = True
        while checker:
            checker = False
            for i in range(len(x)-1):
                if x[i] > x[i+1]:
                    temp = x[i]
                    x[i] = x[i+1]; x[i+1] = temp
                    checker = True
        return x    # А можно было одной строкой x.sort()
        
    #Error: Logic is not found; uninstall python
    def readFile(self, file = "data.txt"):  # считывание из файла
        x = []
        file = open(file)
        #Считывание из файла
        for line in file:
            values = list(map(float, line.split()))    # map вместо for дает возможность применить функцию к каждому элементу объекта
            # вся эта фигня тут потому что я копировал из прошлого проекта, можно сделать легче, но оптимизация явно не конек МЭИ и тем более этого кода, посмотрите на сортировку)))
            # изначально эта штука читала несколько выборок(столбцов в файле)
            x.append(values[0])
        #Считывание из файла завершено
        return x

    def median(self, x):    # from pandas import median
        if len(x) % 2 == 0:
            med = (x[len(x)//2 - 1] + x[len(x)//2]) / 2
        else:
            med = x[len(x)//2]
        return med

    def scatter(self, x, sort = False): # Разброс
        if sort:
            x = self.Bubble_Sort(x)
        return x[-1] - x[0]

    def Tukey(self, x):
        x = self.Bubble_Sort(x)
        
        print(x)

test = TukeyDiagram()
x = test.readFile()
x = test.Tukey(x)