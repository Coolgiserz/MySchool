#!/usr/bin/python
#coding:utf-8
import time
from UrlManager import *
from HtmlParser import *
import types
import urlparse
import re
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
f = open('books_.txt','a+')

info_lst = []
sub_lst = []

def Controller():
    count = 0
    # id = 48552
    id = 48553  #id上限544229
    while(id<544229): 
        lst = []
   
        url = urlmaker(id)
        html = urllib2.urlopen(url)
        text =  html.read()
        # print text
        soup = BeautifulSoup(text,'lxml')
        soup_ul = soup.find('ul')
        soup_h1 = soup.find('h1')
        # print soup_ul
        #因为存在有的页面不包含信息，此时soup_ul类型为NoneType，故做个判断
        if(type(soup_ul) is types.NoneType):
            id += 1
            print '空类型，继续id自增后循环'
        else:
            # print soup_ul.get_text()
            h1_a = soup_h1.find('a')
            h1 = h1_a.get_text().encode('utf-8')
            
            store_str = soup.ul.get_text()
            store_str = store_str.encode('utf-8')
            f.write(h1)
            f.write(store_str)
            f.write(',,,')
            print '已写入第',id,'本书'
            count += 1
            
            if(count>40):
                time.sleep(30)
                print '休息30秒'
                count = 0
            # info_lst.append(store_str)
            # print type(store_str.encode('utf-8'))   #此时store_str为包含每本书所有所需信息的文本字符串
            # sub_li = soup_ul.find_all('li') #使用find_all函数返回的列表中汉字被表示成如\u51fa\u7248\u5730的字符串，如何将此类字符串转换成汉字？
            # sub_li = soup_ul.children
            # print sub_li
            # for child in sub_li:
            #     for sub_span in child:
                    # sub_span =  sub_span.encode('utf-8')
                    # print type(sub_span)        #此时sub_span是Tag和unicode混合的各子序列

            #     span_text = i.find('span').get_text()
                # print (i)
                # if(span_text=='作者'):
                # print i.get_text()

            id += 1
            # print type(sub_li)
            # print u'\u5317\u4eac'
            # ul_str = soup_ul
            # count=0
            # for i in sub_li:
            #     lst = i.strings
            #     # print(lst)
            #     for j in (lst):
            #         sub_lst.append(j)
            #         print (j),count
            #         count+=1                        #经计数测试发现，有的书没有录入isbn号，需要注意
                    # j = j.next
                # print dir(lst)
            # info_lst.append(sub_lst)
            # print (info_lst)

            # print (sub_li[2].contents)
            # res = htmlparser(soup,sub_li)
            # print res
        # print soup_ul
           
Controller()
print '写入完成'
# print info_lst