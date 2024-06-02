from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

'''
pandas是一个数据分析的库，可以用来处理数据，是第三方库，需要下载
下载命令：
pip install pandas

下载失败请参考：
pip使用教程(包括打开cmd、库是什么/分类、pip下载库、换镜像源、pip不是内部或外部命令、导入库失败解决方法)
https://blog.csdn.net/weixin_43698776/article/details/135575203
'''

'''
time库，是Python内置的一个时间处理库，不需要下载。里面有很多函数，用来处理时间
'''

#1.找到指定的链接地址
url = 'https://www.shicimingju.com/book/xiyouji.html'
#2.模拟浏览器，复制以后一直用就行了
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}
#3.请求地址
response = requests.get(url=url,headers=headers)
# 设置编码格式，不然中文会乱码，一般是utf-8。固定语法
response.encoding='utf-8'
#4.检查一下是否可用，能访问到网址，200表示可用，300表示网站有反爬，400表示网址不存在，500表示服务器错误
# print(response)
# 再对比一下网页内容和response.text是否一致，这一步也非常重要，因为如果一致，说明可用，如果不一致，说明网站有反爬
# print(response.text)
#5.解析其中的内容
soup = BeautifulSoup(response.text,'html.parser')
#定义一个列表来保存数据--包括标题和文章内容
xiyouji = []
#定义一个超链接列表来保存所有的链接  #book-mulu是通过id查找的， .book-mulu通过class来寻找的
a_list =soup.select('.book-mulu a')
#现在获取到了所有a标签，需要遍历这个列表，才能获取其中的文本内容
print(a_list)
for a in a_list:
    #每一个超链接中的文本内容 
    #<a href="/book/xiyouji/77.html">第七十七回·群魔欺本性  一体拜真如</a>,
    # 获取其中的文本内容
    title = a.text
    
    #在循环中，要访问每一个章节的超链接https://www.shicimingju.com/book/xiyouji/X.html
    #https://www.shicimingju.com/book/xiyouji/X.html
    # 拼接每一章的网址，注意拼接完成之后仔细核对一下
    detail_url = 'https://www.shicimingju.com/'+a['href']  # 该拼接多了一个斜杠，但是不影响正常访问，因为浏览器和网络服务器在解析URL时具有一定的容错性。这意味着即使URL中包含了一些非标准或不完整的元素，它们仍会尝试找到匹配的资源。多余的斜杠在这种情况下通常会被忽略或视为路径的一部分，而不会导致访问失败。
    detail_url = 'https://www.shicimingju.com'+a['href']  # 该拼接是完全正确的，因为a标签中已经包含了斜杠，所以不需要在最后加斜杠
    # 打印每一章的网址，看看是否正确，一定要细心细心再细心。第一种拼接虽然不影响访问，但我们应该尽量避免这种错误。
    print(detail_url)
    # 6.请求每一章的网址
    detail_text = requests.get(url=detail_url,headers=headers)
    # 设置编码格式，不然中文会乱码，一般是utf-8
    detail_text.encoding='utf-8'
    #再用BeautifulSOUP解析,需要放入的是html代码
    deatil_soup = BeautifulSoup(detail_text.text,'html.parser')
    # 7.查找每一章的内容
    details = deatil_soup.find('div',class_='chapter_content').text
    # 创建一个字典，里面存放章节和内容
    dic={'章节':title,'内容':details}
    # 然后将字典添加到列表中
    xiyouji.append(dic)
    # 每次访问完一个章节，需要等待一下，不然爬太快会被网站检测
    time.sleep(0.3)

# 最后我们获取到了一个列表，列表中存放了所有章节和内容
# print(xiyouji)

#最后，将其保存在excel表格中,把列表中有字典的数据转为df
df = pd.DataFrame(xiyouji)
df.to_excel('西游记.xlsx',index=False)

# vscode只是写代码的软件，不是所有的文件都能显示（目前只能兼容部分图片格式）。
# 不同的文件最好用它对应的软件打开，xlsx文件需要用excel打开，图片、视频、音乐在本地文件夹里打开，pdf文件用浏览器或者专业的pdf软件打开。
