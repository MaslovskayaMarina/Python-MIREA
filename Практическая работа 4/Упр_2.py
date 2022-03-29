import math

class MyClass:
    def __init__(self, x, y): # Метод конструктора
        self.x = x
        self.y = y  
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    def example(self):
        return '12345678910'

obj = MyClass(1, 2)
print('Переменные класса MyClass:')
print(vars(obj))
while True:
    print('Введите метод для вызова. Для выхода нажмите 0')
    s = input()
    if s == '0':
        break
    print(getattr(obj, s)())
