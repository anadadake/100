def fab_iter(n):
    a1 = 1
    a2 = 1
    a3 = 1
    if n == 1 or n == 2:
        return 1
    else:
        while n > 2:
            a3 = a1 + a2
            a1 = a2
            a2 = a3
            n = n - 1
    return a3


def fab_recur(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fab_recur(n - 1) + fab_recur(n - 2)


if __name__ == '__main__':
    print(fab_iter(10))
    print('-----')
    print(fab_recur(10))