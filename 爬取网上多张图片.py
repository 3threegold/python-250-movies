from bs4 import BeautifulSoup
import requests
import time

#获取一页图片的方法，进行复用
def get_img(url):
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}
    response = requests.get(url=url,headers=headers)
    response.encoding='gbk'
    text = response.text
    soup = BeautifulSoup(text,'html.parser')
    #开始解析内容
    img_list = soup.select('.slist img')
    print(img_list)
    #遍历图片对象，拿到链接地址
    for img in img_list:
        img_src = 'https://pic.netbian.com/'+img['src']
        #发送请求
        response = requests.get(url=img_src)
        #要保存图片，要有对应的文件名,replace是替换的意思，因为照片名称中不能包含*
        img_name = img['alt'].replace('*','_')
        #保存图片
        with open(f"动漫图集/{img_name}.png",'wb') as f:
            f.write(response.content)
        time.sleep(1)

# 定义一个函数（也叫方法），用来获取所有页的链接地址
def get_url(n):
    # 创建一个列表，用来存放所有页的链接地址
    url_list = []
    # 将第一页的链接地址添加到列表中
    url_list.append('https://pic.netbian.com/4kdongman/index.html')
    # 遍历2到n-1页的链接地址，并添加到列表中。range()是左闭右开，(2,n)表示从2到n-1
    for i in range(2,n):
        url_list.append(f'https://pic.netbian.com/4kdongman/index_{i}.html')
    # 返回这个列表
    return url_list

# 调用get_url函数，传入页数
url_list = get_url(4)
# 打印这个列表看看，确定一下每页的网址是否正确
# print(url_list)

# 定义一个n，用来显示进度
n = 0
# 遍历url_list。再次强调：url_list里面存放的是每一页的链接地址
for u in url_list:
    # 每循环一次，n就加1
    n=n+1
    #会遍历列表，直到所有的链接（3页）获取完毕
    #如果链接地址不存在，很容易出现错误。因此加上try-except。当try里面的代码报错时，就会执行except里面的代码
    try:
        print(f'正在获取第{n}页图片')
        # 调用get_img函数，传入每一页的链接地址
        get_img(u)
        # 每获取完一页的图片，就打印一下，不仅是方便查看进度，也是代表get_img函数没有报错顺利执行
        print(f'第{n}页图片获取完毕')
    except:
        # 当except里面的代码执行时，极大概率代表get_img函数报错了，因为try里面的代码就三行，print报错的几率非常小，除非你太粗心写错了。
        # 这时可以暂时取消掉try-except，让报错显示出来，这样便于查错。取消掉try-except之后要注意缩进是否正确
        print(f'获取第{n}页图片失败')