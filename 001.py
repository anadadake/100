#!/usr/bin/python
# -*- coding: UTF-8 -*-

# if __name__ == '__main__':
#     for i in range(1, 5):
#         for j in range(1, 5):
#             for k in range(1, 5):
#                 if (i != k) and (i != j) and (j != k):
#                     print(i, j, k)


if __name__ == '__main__':
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if (i != k) and (i != j) and (j != k):
                    print(str(i) + str(j) + str(k))
