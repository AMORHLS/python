# -*- coding: utf-8 -*-
# @Time    : 2018/2/24
# @Author  : 何立诗
# @Email   : hlsamor@163.com
# 使用 时间 作为文件名，而当前的 日期 作为目录名，存放在主备份目录中。
# 备份会以等级结构存储，容易管理。文件名的长度变短。采用各自独立的文件夹可以帮助你方便地检验你是否在每一天创建了备份，
# 因为只有在你创建了备份，才会出现那天的目录。
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
today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created diectory',today)
target = today + os.sep + now + '.zip'  # os.sep 跨平台的分隔符 /  \
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















