
def plus():
    return a + b
def minus():
    return a - b
def delen():
    return a / b
def prois():
    return a * b
def ctep():
    return a ^ b

while True:
    print('Введите 2 числа: ')
    a = int(input())
    b = int(input())
    c = input('+, -, /, *, ^')
    if c == '+':
        print('Результат:', plus())
    elif c == '-':
        print('результат: ', minus())
    elif c == '*':
        print('результат: ', prois())
    elif c == '^':
        print('результат: ', ctep())
    elif c == '/' and b != 0:
            print('результат: ', delen())
    else:
       print('деление на 0 нельзя')
       break