#安装过程中，有的包名字，bs4其实就是一个更大的包
#现在from 从....里面，import 导入其中的一部分内容
from bs4 import BeautifulSoup
'''
BeautifulSoup 是一个第三方包，用来解析html代码，
下载命令：
pip install beautifulsoup4

下载失败请参考：
pip使用教程(包括打开cmd、库是什么/分类、pip下载库、换镜像源、pip不是内部或外部命令、导入库失败解决方法)
https://blog.csdn.net/weixin_43698776/article/details/135575203
'''
#这里是老师提前准备好的网页内容，如果是想访问正常网址
#直接通过requests.get获取就可以了。
html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <div id="container">
        <span>这些明星</span>
        <div class="item1">
            <a href="https://www.baidu.com/">周杰伦</a>
        </div>
        <div class="item2">
            <a href="https://news.baidu.com/">林俊杰</a>
        </div>
        <div class="item3">
            <a href="https://tieba.baidu.com/">张杰</a>
        </div>
    </div>
</body>
</html>
'''
#1.创建soup对象 第一个参数：html代码
soup = BeautifulSoup(html,'html.parser')
#2.soup对象.某一个标签，可以找到对应标签
# 对应标签.text 可以找到对应的文本内容
# print(soup.span.text)
#find更常用
# print(soup.find('span').text)
#3.查找具体的某一个标签的时候，要知道对应的标签名字
#class是关键词，所以函数里使用的是class_
# print(soup.find('div',class_='item2').text)
#4.如果我想批量获取，某一个网站上的所有链接，要去找该网站上的所有a标签（超链接）
#find只会找到对应的第一条符合的数据，就不继续寻找了
#find_all可以找到所有的对应标签
print(soup.find_all('a'))
for url in soup.find_all('a'):
    # print(url.text)
    print(url['href'])

# soup1 = BeautifulSoup(html1,'html.parser')
# print(soup1.select('#content'))
#print(soup1.select('ul>li>a'))#没有跨层级，逐步寻找
# print(soup1.select('ul a'))#可以跨层级找到所有的内容
