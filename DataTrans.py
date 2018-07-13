#!/usr/bin/python
#coding:utf-8
import sys
import MySQLdb
print '当前环境默认编码：',sys.getdefaultencoding
lst = []
f = open('books2333.txt','r')
ff = open('store_book.txt','w+')
book_str =  f.read()
# print book_str
# utf8_str = str(f.read())
lst = book_str.split(',,,')
# print lst
for i in range(len(lst)):
    # print i,lst[i]

    info_lst = lst[i].split('\n')
    book_name = info_lst[0]         #书名
    author = info_lst[1]            #作者   注意len('作者')==6
    price = info_lst[2]             #价格   注意len('价格')==6
    pubilsher = info_lst[3]         #出版社  注意len('出版社')==9
    book_code = info_lst[4]         #索书号  注意len('索书号')==9
    ISBN_code = info_lst[5]         #ISBN  
    class_num = info_lst[6]         #分类号  
    page_num = info_lst[7]          #页数
    publish_date = info_lst[8]      #出版日期  len==12
    pubilsh_loc = info_lst[9]       #出版地 
    print "正写第",i,"本书"
    ff.write(book_name)
    ff.write(';;;')
    ff.write(author[6:])
    ff.write(';;;')
    ff.write(price[6:])
    ff.write(';;;')
    ff.write(pubilsher[9:])
    ff.write(';;;')
    ff.write(book_code[9:])
    ff.write(';;;')
    ff.write(ISBN_code[4:])
    ff.write(';;;')
    ff.write(class_num[9:])
    ff.write(';;;')
    ff.write(page_num[4:])
    ff.write(';;;')
    ff.write(publish_date[12:])
    ff.write(';;;')
    ff.write(pubilsh_loc[9:])
    ff.write('\n')
    #有的作者不止一个，逗号分割，所以企图用单逗号分隔是不合适的
    # print [6:]
    # print info_lst[9]
    # print author[6:]
    # print len('出版日期')
    # print author
    # for j in range(len(info_lst)):
    #     print j
# print (lst[1].split('\n'))