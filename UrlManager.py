import os
import urllib
import urllib2
from bs4 import BeautifulSoup
baseurl = 'http://opac.its.csu.edu.cn/NTRdrBookRetrInfo.aspx?BookRecno='
# id = 1


def urlmaker(id):
    url = "%s%d"%(baseurl,id)
    return url


# url = urlmaker(id)
# html = urllib2.urlopen(url)
# text =  html.read()
# # print text
# soup = BeautifulSoup(text,'lxml')
# print soup.ul
