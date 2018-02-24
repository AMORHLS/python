# -*- coding: utf-8 -*-
# @Time    : 2018/2/24
# @Author  : 何立诗
# @Email   : hlsamor@163.com
import os
import time
# 1、The files and directories to be  backed up are speicified in a list .
source = ['F:\\abc','E:\\DB-repository']   # \ 表示转义符  或者加上r   R   或者 将\ 改为 /
# If you are using Linux,use source = ['/home/swaroop/byte','/home/swaroop/bin'] or something like that
# 2、The backup must be stored in a main backup directory
target_dir = 'D:\\Backup\\'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
# 3、The files are backed up into a zip file.
# 4、The name of the zip archive is the current date and time
target = target_dir + time.strftime('%Y%m%d%H%M%S')+'.zip'
print(target)
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















