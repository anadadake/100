def saysomething(name, words):
    print(name + ' --> ' + words)


def test(*params, extra=8):
    print("收集参数是：" + str(params))
    print("关键字参数是：" + str(extra))
    global old_price
    old_price = 0



old_price = 1
new_price = 2


def func1():
    print('func 1 ')

    def func2():
        print('in func2')

    func2()


def closure_func_test(x):
    def func1(y):
        return x * y

    return func1


if __name__ == '__main__':
    saysomething('kevin ', ' loves cakes.')
    saysomething(words='loves beef.', name='Kevin')

    print('------------------')
    a = [1, 2, 3, 4, 6]
    test(*a, extra='aa')
    test('1', '2', '3', extra='xxx')

    print(old_price)
    print(new_price)
    print('------------------')
    func1()

    # print(closure_func_test(1))

    i = closure_func_test(40)
    print(i(4))

    l_f_1 = lambda x, y: (x + y) * (x + y)
    print(l_f_1(1, 2))
    temp = filter(None, [1, 0, True, False])
    print(temp)
    print(list(temp))


    def odd(x):
        return x % 2


    print(list(filter(odd, range(20))))

    print(list(filter(lambda x: x % 2, range(100))))

    #range(41) * 3
    print(list(map(lambda x:x*3,range(41))))

    def fact(n):
        if n == 1:
            return 1
        else:
            return fact(n-1)*n

    a = fact(10)
    print(a)
