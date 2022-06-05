def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def delen(a, b):
    return a / b


def prois(a, b):
    return a * b


def ctep(a, b):
    return a ^ b


while True:
    print('Введите 2 числа: ')
    a = int(input())
    b = int(input())
    c = input('+, -, /, *, ^')
    if c == '+':
        print('Результат:', plus(a, b))
    elif c == '-':
        print('результат: ', minus(a, b))
    elif c == '*':
        print('результат: ', prois(a, b))
    elif c == '^':
        print('результат: ', ctep(a, b))
    elif c == '/' and b != 0:
        print('результат: ', delen(a, b))
    else:
        print('деление на 0 нельзя')
        break
