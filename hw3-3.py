def exe_3(a, b, c):
    z = [a, b, c]
    z.remove(min(a, b, c))
    return sum(z)


def exe_3_use():
    print(exe_3(4, 1, 9))