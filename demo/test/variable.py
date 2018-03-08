# -*- coding: utf-8 -*-
# @Time    : 2018/2/5
# @Author  : HLS
# @Email   : hlsamor@163.com
# @Site    : 
# @File    : variable.py
# @Software: PyCharm
from pip._vendor.distlib.compat import raw_input

i = 5
print(i)
i = i + 1
print(i)

s = ''' This is a multi-line string. 
    This is the second line. '''
print(s)
print("---------------------------------------------------------")

print(4//3.0) #返回商的整数部分
print("-------------------------if控制语句--------------------------------")
# number = 23
# guess = int(raw_input('请输入一个整数：'))
#
# if guess == number:
#     print('Congratulations, you guessed it.')
#     print("(but you do not win any prizes!)")
# elif guess < number:
#     print('No, it is a little higher than that')
# else:
#     print('No, it is a little lower than that')
#
# print('Done!')

print("-------------------------while控制语句--------------------------------")

number = 23
running = True

# while running:
#     guess = int(raw_input('请输入一个整数：'))
#
#     if guess == number:
#         print('Congratulations, you guessed it.')
#         running = False
#     elif guess < number:
#         print('No, it is a little higher than that')
#         print('请继续猜测。。。')
#     else:
#         print('No, it is a little lower than that')
#         print('请继续猜测。。。')
# print('Done!')

# print("-------------------------for循环--------------------------------")
# for i in range(1,5):  #左闭右开
#     print(i)
# else:
#     print('over!!!')

print("-------------------------break语句--------------------------------")

# var = 10
# while var > 0:
#     print('当前变量值 :', var)
#
#     var = var - 1
#     if var == 5:  # 当变量 var 等于 5 时退出循环
#         break
#
# print("Good bye!")

# for letter in 'Python':
#    if letter == 'h':
#       break
#    print ('当前字母 :', letter)
#第一次下载2.4版本，不知道是因为版本原因还是什么原因 当时的break退不出循环（记录）
while True:
    s = raw_input('Enter something : ')
    if s == 'quit':
        break
    print( 'Length of the string is', len(s))
print ('Done')

















