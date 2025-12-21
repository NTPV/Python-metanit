# Создайте класс Vector, который представляет вектор и определите в нем операторы сложения и вычитания.
#  Для сложения векторо применяется формула a + b = {ax + bx; ay + by}, а для вычитания a - b = {ax - bx; ay - by}

class Vector:
    def __init__(self, Xcoordinate, Ycoordinate):
        self.Xcoordinate = Xcoordinate
        self.Ycoordinate = Ycoordinate

    def __add__(self, other):
        Xresult = self.Xcoordinate + other.Xcoordinate
        Yresult = self.Ycoordinate + other.Ycoordinate

        return Vector(Xresult, Yresult)

    def __sub__(self, other):
        Xresult = self.Xcoordinate - other.Xcoordinate
        Yresult = self.Ycoordinate - other.Ycoordinate

        return Vector(Xresult, Yresult)

    def showCoordinates(self):
       print(f'Координаты вектора X:{self.Xcoordinate} Y:{self.Ycoordinate}')




VectorA = Vector(4, 5)
VectorB = Vector(3,1)

sumVector = VectorA + VectorB
subtractVector = VectorA - VectorB

sumVector.showCoordinates()
subtractVector.showCoordinates()