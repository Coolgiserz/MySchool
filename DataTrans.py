#!/usr/bin/python
#coding:utf-8
import sys
import MySQLdb
# print '当前环境默认编码：',sys.getdefaultencoding
db = MySQLdb.connect("localhost", "zhuge1", "zhuge1", "tb_school", charset='utf8' )
cursor = db.cursor()# 使用cursor()方法获取操作游标 
cursor.execute("SELECT VERSION()")# 使用execute方法执行SQL语句
data = cursor.fetchone()# 使用 fetchone() 方法获取一条数据
print "Database version : %s " % data

# 关闭数据库连接
seperator = ';'
lst = []
f = open('books_21795.txt','r')
# ff = open('store_book.txt','w+')
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

    publisher = info_lst[3]         #出版社  注意len('出版社')==9

    book_code = info_lst[4]         #索书号  注意len('索书号')==9

    ISBN_code = info_lst[5]         #ISBN  

    class_num = info_lst[6]         #分类号  

    page_num = info_lst[7]          #页数

    publish_date = info_lst[8]      #出版日期  len==12
    publish_date = publish_date[12:]
    if len(publish_date)<8:
        publish_date = str(00000000)
    publish_loc = info_lst[9]       #出版地 
    
    # sql = "INSERT INTO csu_lib(id,book_name,author, price, publisher,book_code,ISBN_code,class_num,page_num,publish_date,pubilsh_loc) VALUES(i,book_name,author[6:], price[6:], pubilsher[9:], book_code[9:],ISBN_code[4:],class_num[9:],page_num[4:-3],publish_date[12:],publish_loc[9:])"
    cursor.execute("INSERT INTO csu_lib(id,book_name,author, price, publisher,book_code,ISBN_code,class_num,publish_date,publish_loc) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(0,book_name,author[6:], price[6:], publisher[9:], book_code[9:],ISBN_code[4:],class_num[9:],publish_date,publish_loc[9:]))
    db.commit()
    print "写第",i,"本书"
    # try:
    # #     #  cursor.execute(sql)
    #      cursor.execute("INSERT INTO csu_lib(id,book_name,author, price,publisher,book_code,ISBN_code,class_num,publish_date,pubilsh_loc) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(0,book_name,author[6:], price[6:], publisher[9:], book_code[9:],ISBN_code[4:],class_num[9:],publish_date[12:],publish_loc[9:]))

    #      db.commit()
    #      print "写第",i,"本书"
    # except:
    #      print "第",i,"本书出了点问题"
        #  db.rollback()
    # ff.write(book_name)
    # ff.write(seperator)
    # ff.write(author[6:])
    # ff.write(seperator)
    # ff.write(price[6:])
    # ff.write(seperator)
    # ff.write(publisher[9:])
    # ff.write(seperator)
    # ff.write(book_code[9:])
    # ff.write(seperator)
    # ff.write(ISBN_code[4:])
    # ff.write(seperator)
    # ff.write(class_num[9:])
    # ff.write(seperator)
    # ff.write(page_num[4:-3])
    # ff.write(seperator)
    # ff.write(publish_date[12:])
    # ff.write(seperator)
    # ff.write(publish_loc[9:])
    # ff.write('\n')


    # 有的作者不止一个，逗号分割，所以企图用单逗号分隔是不合适的
    # print [6:]
    # print info_lst[9]
    # print author[6:]
    # print len('出版日期')
    # print author
#     for j in range(len(info_lst)):
#         print j
# print (lst[1].split('\n'))
db.close()
