if __name__ == '__main__':
    list1= [1,2,3,4,5,6,7,8,9]
    print(len(list1))
    list1.append(10)
    print(list1)
    list1.pop(2)
    print(list1)
    list1.insert(0,'aaa')
    print(list1)
    list1.append('bbb')
    print(list1)

    list2 = ['a','b','c']

    list1.extend(list2)
    print(list1)
    # del list1
    # print(list1)
    print(list1 * 5)

    print(isinstance(list1, str))

    print(type(list1))

    if r"<class 'list'>" == type(list1):
        print("True")
    else:
        print("False")

    if r"<class 'list'>" == str(type(list1)):
        print("True")
    else:
        print("False")


    subList = ['x','y','z']

    print(subList)

    list1.append(subList)
    print(list1)

    if 'x' in list1[14]:
        print("True")
    else:
        print("False")

    print(list1[14][0])
    # print(list1[14][6])