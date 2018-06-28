import os
import pickle

if __name__ == '__main__':
    print('aaa')
    print(os.getcwd())

    for i in os.walk(os.getcwd()):
        print(i)

    test_file = open("d:\\Downloads\\问卷反馈111.txt", mode='w')
    test_file.write("aaaa")
    # test_file.tell()
    # print(test_file.read(10))
    # print(test_file.read())
    test_file.close()
    os.system('calc')


    my_list = [123,3.13,'kevin', ['inner list']]
    pickle_file = open('D:\\Downloads\\111.txt','wb')
    pickle._dump(my_list,pickle_file)
    pickle_file.close()

    pickle_file = open('D:\\Downloads\\111.txt','rb')
    list1 = pickle.load(pickle_file)
    print(list1)
    pickle_file.close()
