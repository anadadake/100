#!/usr/bin/python
# -*- coding: UTF-8 -*-

# python version 3.6.5 64bit on windows

# 002
# 题目：企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？

if __name__ == '__main__':

###########method 1:从小到大

# 比例
    rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    # 临界值
    limit_array = [1000000, 600000, 400000, 200000, 100000, 0]
    profit = int(input())
    bonus = 0

    for i in range(0, 5):
        if profit > limit_array[i]:
            bonus = bonus + (profit - limit_array[i])*rate[i]

    print(bonus)

###########method 2:从大到小

# i = int(input('净利润:'))
# arr = [1000000, 600000, 400000, 200000, 100000, 0]
# rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
# r = 0
# for idx in range(0, 6):
#     if i > arr[idx]:
#         r += (i - arr[idx]) * rat[idx]
#         print(i - arr[idx]) * rat[idx]
#         i = arr[idx]
#     print(r)
