# Программа компании Igorexy Dev, ураденная с GitHub https://github.com/KozlovIA
# Качайте приложение https://play.google.com/store/apps/details?id=com.DefaultCompany.RollBall - рекламная интеграция за 15 рублей, поддержите начинающего разработчика

from os import read
# А может import pandas? или import хотя бы Statistics ?  NO!  //  using System.Math;


# переменная x везде означает выборку, это логичное имя, т.к. на бумаге тоже самое
class TukeyDiagram():   # Ну главное, чтобы не Turkey))
    def __init__(self) -> None:
        #Я решил ничего не инициализировать, и так хорошечно работает
        pass

    def Bubble_Sort(self, x):  # За использование этой гениальной сортировки я уже не прошел интервью. Хотя какой sort(), это ж C++;
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
            values = list(map(float, line.split()))    # map вместо for дает возможность применить функцию к каждому элементу объекта(он тут не нужен на самом деле)
            # всё это тут потому что я копировал из прошлого проекта, можно сделать легче, но оптимизация явно не конек этого кода, посмотрите на сортировку)))
            # изначально эта штука читала несколько выборок(столбцов в файле)
            x.append(values[0])
        #Считывание из файла завершено
        return x

    def mean(self, x):
        #0пять оптимизировать((
        #return sum(x)/len(x)
        sum = 0
        for value in x:
            sum += value
        return sum/len(x)

    def dispersion(self, x):
        mean = self.mean(x)
        dispersion = 0
        for value in x:
            dispersion += (value - mean)**2
        dispersion /= (len(x) - 1)
        return dispersion

    def median(self, x, sort = True):    # from pandas import median
        if sort:
            x = self.Bubble_Sort(x)
        if len(x) % 2 == 0:
            med = (x[len(x)//2 - 1] + x[len(x)//2]) / 2
        else:
            med = x[len(x)//2]
        return med

    def scatter(self, x, sort = False): # Разброс
        if sort:
            x = self.Bubble_Sort(x)
        return x[-1] - x[0]

    def Tukey(self, x, sort = True):
        if sort:
            x = self.Bubble_Sort(x)
        if len(x) % 2 == 0:
            BottomBorderBox = x[len(x)//2 - len(x)//4]  # Нижняя/верхняя границы ящика
            TopBorderBox = x[len(x)//2 + len(x)//4 - 1]
            H = self.scatter([BottomBorderBox, TopBorderBox])  # H тоже обозначется на бумаге как H, поэтому это удобно
        else:
            BottomBorderBox = x[len(x)//2 - len(x)//4]
            TopBorderBox = x[len(x)//2 + len(x)//4]
            H = self.scatter([BottomBorderBox, TopBorderBox]) 
        # Emissions
        #bottom border of the box
        #top border of the box
        emissions = []
        for i in range(len(x)):
            if x[i] < BottomBorderBox - 1.5*H or x[i] > TopBorderBox + 1.5*H:
                emissions.append(x[i])
        return emissions, BottomBorderBox, TopBorderBox, H

# Of one mind of one soul, we unite to write our c0de
def interview():
    Tukey = TukeyDiagram()
    fileName = input("Введите имя файла с выборкой(!!!Десятичные дроби в файле должны быть записаны через точку, а выборка в столбик!!!): ")
    x = Tukey.readFile(fileName)
    x = Tukey.Bubble_Sort(x)
    meanX = Tukey.mean(x)
    dispersionX = Tukey.dispersion(x)
    medianX = Tukey.median(x, False)
    
    emissions, BottomBorderBox, TopBorderBox, H = Tukey.Tukey(x)
    print("Изначальная выборка:\n", x, "\n\nМат ожидание: ", meanX, "\nДисперсия: ", dispersionX, "\nМедиана: ", medianX,
    "\n\n---Диаграмма Тьюки---\nВерхняя граница ящика: ", TopBorderBox, "\nНижняя граница ящика: ", BottomBorderBox,
    "\nГраница верхнего уса: ", TopBorderBox + 1.5*H, "\nГраница нижнего уса: ", BottomBorderBox - 1.5*H,  "\nВыбросы: ", emissions, sep='')

if __name__ == "__main__":
    interview()