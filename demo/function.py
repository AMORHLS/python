# -*- coding: utf-8 -*-
# @Time    : 2018/2/23
# @Author  : 何立诗
# @Email   : hlsamor@163.com
# ///////////////////////定义一个函数用 def////////////函数形参/////////////////
# def printMax(a,b):
#     if a>b:
#         print(a,"is maximum")
#     else:
#         print(b,"is maximum")
# printMax(3,4)
# x = 5
# y = 7
# printMax(x,y)
#  -------------------------------------局部变量--------------------------------------------
def func(x):
    print('x is ',x)
    x = 2
    print('changed local x to ', x)
x = 50
func(x)
print('x is still',x)

# 使用global指定全局变量
def func2():
    global y
    print('y is ',y)
    y = 2
    print('changed local y to', y)
y = 50
func2()
print('value of x is ',y)

# 使用默认参数值
def say(message,times = 1):
    print(message*times)
say('hello')
say('world',5)

# 使用关键词参数、
print('------------------------------使用关键词参数---------------------------------')
def func3(a,b = 5, c = 10):
    print('a is ',a,'and b is ',b, 'and c is ',c)
func3(3,7)
func3(25,c = 24)
func3(c = 50 , a = 100)

print('return 语句 跳出函数或者返回一个值')
def maximum(x,y):
    if x > y:
        return  x
    else:
        return  y
print(maximum(2,3))

print('文档字符串docstrings')
def  printmax(x,y):
    ''' Prints the maximum of two numbers.
    The two values must be integers.'''
    x = int(x)
    y = int(y)
    if x > y:
        print(x,'is maximum')
    else:
        print(y,'is maximum')
printmax(3,5)
print(printmax.__doc__)