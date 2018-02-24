# -*- coding: utf-8 -*-
# @Time    : 2018/2/5
# @Author  : 何立诗
# @Email   : hlsamor@163.com
import urllib

from lxml import html
import requests
# -------------------第一种方式爬取网页数据----------------------
# '//td[@class="title"]//a/text()'   这部分是获取数据的重要部分  xpath语法（路径表达式）
#   解释： //td  --> 相当于指定是大目录   [@class="title"]  -->  这个相当于指定的小目录
#          //a  --> 最小的目录            /text()  -->  这个就是获取的数据
url='https://movie.douban.com/' # 需要爬数据的网址
page=requests.Session().get(url)
tree=html.fromstring(page.text)
# print(tree)
str = '//div[@class="review-meta"]//a/text()'
# str = '//td[@class="title"]//a/text()'
result=tree.xpath(str) # 获取需要的数据
# print(result)
print('\n'.join(result))














