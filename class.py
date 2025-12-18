class Rectangle:

    def __init__(self, a, b):
        self.width = a
        self.length = b

    def area(self):

        s = self.width * self.length
        return s

    def perimeter(self):

        p = (self.width + self.length) * 2
        return p

class BankAccount:

    def __init__(self, number = 1, balance = 0.0):
        self.account_number = number
        self.balance = balance

    def add(self, sum):
        print(f'Начальный баланс счета: {self.balance}')
        self.balance = self.balance + float(sum)
        print(f'На баланс зачислено: {sum} ; Текущий баланс счета : {self.balance}')

    def withdraw(self, rashod):
        print(f'Начальный баланс счета: {self.balance}')

        if rashod > self.balance:
            print('На балансе недостаточно средств, операция не выполнена')
            return
        self.balance = self.balance - float(rashod)
        print(f'С баланса списано: {rashod} ; Текущий баланс счета : {self.balance}')


bigrectangle = Rectangle(10,8)
print(f'Площадь большого прямоугольника: {bigrectangle.area()}')
print(f'Периметр большого прямоугольника: {bigrectangle.perimeter()}')

smallrectangle = Rectangle(3,4)
print(f'Площадь маленького прямоугольника: {smallrectangle.area()}')
print(f'Периметр маленького прямоугольника: {smallrectangle.perimeter()}')

acc1 = BankAccount("123456577", 1000)
acc1.add(200)
acc1.withdraw(500)
acc1.withdraw(300)
acc1.withdraw(900)







