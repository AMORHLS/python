# -*- coding: utf-8 -*-
# @Time    : 2018/2/24
# @Author  : 何立诗
# @Email   : hlsamor@163.com
# 物理行  逻辑行
# 分析  设计  编写  测试与调试  使用  优化运维
import os
import time
# 1、The files and directories to be  backed up are speicified in a list .
from pip._vendor.distlib.compat import raw_input
source = ['F:\\abc','E:\\DB-repository']   # \ 表示转义符  或者加上r   R   或者 将\ 改为 /
# If you are using Linux,use source = ['/home/swaroop/byte','/home/swaroop/bin'] or something like that
# 2、The backup must be stored in a main backup directory
target_dir = 'D:\\Backup\\'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
# 3、The files are backed up into a zip file.
# 4、The name of the zip archive is the current date and time
today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
# Take a comment from the user to create the name of the zip file
comment = raw_input('Enter a comment --> ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_'+\
             comment.replace('','_')+'.zip'  # 用 \ 标明这两个物理行是一个逻辑行
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created diectory',today)
# 5、We use the zip command (in Linux)to put the files in a zip archive
# zip_command = "zip -qr %s %s" % (target,' '.join(source))
# zip_command = "7z a {0} {1}".format(target,' '.join(source))  # ok
zip_command = "7z a %s %s" % (target,' '.join(source))          # ok
print('zip_command is: ')
print(zip_command)
# Run the backup
if os.system(zip_command) == 0:
    print('Successful backup to',target)
else:
    print('Backup FAILED!')















