#!/usr/bin/python
#coding:utf-8
'''
传入的text为soup.ul,格式为
<ul class="list">
<li style="width:100%"><span>作者</span><a href="NTRdrBookRetr.aspx?strType=author&amp;strKeyValue=%e5%88%98%e7%82%b3%e6%96%87">刘炳文</a> </li>
<li><span>价格</span>CNY24.40</li>
<li><span>出版者</span><a href="NTRdrBookRetr.aspx?strType=text&amp;strKeyValue=%e5%9b%bd%e9%98%b2%e5%b7%a5%e4%b8%9a%e5%87%ba%e7%89%88%e7%a4%be">国防工业出版社</a></li>
<li><span>索书号</span><a href="NTRdrBookRetr.aspx?strType=text&amp;strKeyValue=73.87221%2fLPW">73.87221/LPW</a></li>
<li><span>ISBN</span><a href="NTRdrBookRetr.aspx?strType=text&amp;strKeyValue=7-118-01010-3">7-118-01010-3</a></li>
<li><span>分类号</span><a href="NTRdrBookRetr.aspx?strType=text&amp;strKeyValue=TP312AD">TP312AD</a></li>
<li><span>页数</span>460页</li>
<li><span>出版日期</span>19930101</li>
<li><span>出版地</span>北京</li>
</ul>
'''
import re
pattern_cost = re.compile(r'(?<=(<span>价格<\/span>)).+(?=<\/li>)', re.S)
pattern_chuban = ''
pattern_suoshu = ''
pattern_isbn = ''
pattern_classic = ''
pattern_yeshu = ''
pattern_date = ''
pattern_chubandi = ''
def htmlparser(soup,text):
#      li=soup.find('ul',class_='list').find('li')
#      print soup.ul.attrs
#    data['title']=title.get_text()
#    summary = soup.find('div',class_='lemma-summary')
#    data['summary']=summary.get_text()   
#      pattern_author = '(?<=(<span>价格<\/span>)).+(?=<\/li>)'
    #  print text

    #  print re.search(pattern_cost,text)
     return text