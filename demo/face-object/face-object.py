# -*- coding: utf-8 -*-
# @Time    : 2018/3/2
# @Author  : 何立诗
# @Email   : hlsamor@163.com
# 创建一个类
class Person:
    pass # 具体的逻辑代码（空白块）
p = Person()
print(p)

# 对象   类与对象可以拥有函数一样的方法  区别是比函数多了一个self变量   相当于this
class Person:
    def sayHi(self):
        print("Hello,how are you ?")
p = Person()
p.sayHi();

print("-------------------------------__init__方法----------------------------------")
class Person:
    def __init__(self,name):
        self.name = name
    def sayHi(self):
        print("Hello,my name is",self.name)
p = Person('AMOR')
p.sayHi();

