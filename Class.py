# Упражнение 1
# Определите класс Rectangle, который представляет прямоугольник. Через конструктор класс принимает ширину и длину и сохраняет их в атрибутах width и length соответственно.
# Также этом классе определите метод area, который возвращает площадь прямоугольника, и метод perimeter, который возвращает периметра прямоугольника.
# После создания класса определите несколько объектов класса Rectangle и продемонстрируйте работу его методов.

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

# Упражнение 2
# Создайте класс BankAccount, который представляет банковский счет. Определите в этом классе атрибуты account_number и balance, которые представляют номер счета и баланс.
# Через параметры конструктора передайте этим атрибутам начальные значения.
# Также в классе определите метод add, который принимает некоторую сумму и добавляет ее на баланс счета. И определите метод withdraw, который принимает некоторую сумму и снимает ее с баланса.
# При этом с баланса нельзя снять больше, чем имеется. Если на балансе недостаточно средств, то пользователю должно выводиться соответствующее сообщение.

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
