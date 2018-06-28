def hanoi_recur(n, x, y, z):
    if n == 1:
        # print("step: " + str(n))
        print(x + ' --> ' + z)
    else:
        # print("step: " + str(n))
        hanoi_recur(n - 1, x, z, y)
        print(x + ' --> ' + z)
        hanoi_recur(n - 1, y, x, z)


if __name__ == '__main__':
    hanoi_recur(3, 'x', 'y', 'z')
