def exe_6(text):
    ls = []
    for i in range(len(text)):
        ls.append(text[i][0:1].title() + text[i][1:])
    return ' '.join(ls)


def exe_6_use():
    print(exe_6(input('Input text: ').split()))


def sep():
    print('+' * 30)


def refresh():
    print('Выберите задание и его решение')
    sep()
    print('Задание 1. Введите: 1')
    sep()
    print('Задание 2. Введите: 2')
    sep()
    print('Задание 3. Введите: 3')
    sep()
    print('Задание 4. Введите: 4 или 41 (2 решения)')
    sep()
    print('Задание 5. Введите: 5')
    sep()
    print('Задание 6. Введите: 6\n')