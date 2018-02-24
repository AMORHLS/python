# -*- coding: utf-8 -*-
# @Time    : 2018/2/23
# @Author  : 何立诗
# @Email   : hlsamor@163.com
print('----------------------------列表[]--------------------------')
shoplist = ['apple','mango','carrot','banana']
print('I have',len(shoplist),'items to purchase.')
print('These items are:')
for item in shoplist:
    print(item)
print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now',shoplist)
print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is ',shoplist)
print('The first item I will buy is',shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the',olditem)
print('My shopping list is now',shoplist)

# help(list)

print('---------------------------------------元祖()----------------------------------')
zoo = ('wolf','elephant','penguin')
print('Number of animals in the zoo is',len(zoo))
new_zoo = ('monkey','dolphin',zoo)
print('Number of animals in the new zoo is',len(new_zoo))
print('All animals in the new zoo are',new_zoo)
print('Animals brought from old zoo are',new_zoo[2])
print('Last animal brought from old zoo is',new_zoo[2][2])

# 用元祖来打印信息
age = 22
name = 'AMOR'
print('Why is %s playing with that python?' % name)
print('%s is %d years old' % (name,age))

print('---------------------------------------字典{}----------------------------------')
ab = {       'Swaroop'   : 'swaroopch@byteofpython.info',
             'Larry'     : 'larry@wall.org',
             'Matsumoto' : 'matz@ruby-lang.org',
             'Spammer'   : 'spammer@hotmail.com'
     }

print("Swaroop's address is %s" % ab['Swaroop'])
ab['Guido'] = 'guido@python.org'
del ab['Spammer']
print('\nThere are %d contacts in the address-book\n' %len(ab))
for name,address in ab.items():
    print('Contact %s at %s' % (name,address))
if 'Guido' in ab:
    print("\nGuido's address is %s" % ab['Guido'])

print('---------------------------------------序列[] 列表和元祖都是序列----------------------------------')
list = ['apple','mango','carrot','banana']
print('Item 0 is',list[0])
print('Item 1 is',list[1])
print('Item 2 is',list[2])
print('Item 3 is',list[3])
print('Item -1 is',list[-1])
print('Item -2 is',list[-2])
# 切片操作符
print('Item 1 to 3 is',list[1:3]) # 左闭右开区间  右边不取值
print('Item 2 to end is',list[2:])
print('Item 1 to -1 is',list[1:-1]) # 左闭右开区间  右边不取值
print('Item start to end is',list[:])

print("-----------字符串也是序列-------------")
name = 'swaroop'
print('characters 1 to 3 is',name[1:3])
print('characters 2 to end is',name[2:])
print('characters 1 to -1 is',name[1:-1])
print('characters start to end is',name[:])

print('---------------参考-------------------')
print('Simple Assignment')
shopping = ['apple','mango','carrot','banana']   # 这个变量仅仅参考那个对象
mylist = shopping

del shopping[0]
print('shopping is ',shopping)
print('mylist is ',mylist)

print('Copy by making a full slice')
mylist = shopping[:]  # 通过切片操作符来复制列表或者序列 ，之后操作 不再具有参考性
del mylist[0]

print('shopping is ',shopping)
print('mylist is ',mylist)

print('---------------------------------字符串的一些方法---------------------------------')
name = 'Swaroop'
if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')
if 'a' in name:
    print('Yes, it contains the string "a"')
if name.find('war') != -1:
    print('Yes, it contains the string "war"')
delimiter = '_*_'
mylist2 = ['AMOR','LOVE','YOU']
print(delimiter.join(mylist2))

# help(str)





























