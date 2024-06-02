from bs4 import BeautifulSoup
import requests
import time

url = 'https://pic.netbian.com/4kdongman/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}
response = requests.get(url=url,headers=headers)
# 因为网站是gbk编码，具体怎么看网站编码，请看“网站编码.png”图片，编码在最上面的head标签里，一般跟网站的编码最好保持一致
response.encoding='gbk'
text = response.text
soup = BeautifulSoup(text,'html.parser')
#开始解析内容
img_list = soup.select('.slist img')
print(img_list)
# 遍历图片对象，拿到链接地址
for img in img_list:
    # 拼接完整的图片地址
    img_src = 'https://pic.netbian.com/'+img['src']
    # 发送请求
    response = requests.get(url=img_src)
    response.encoding='jbk'
    # 要保存图片，要有对应的文件名,replace是替换的意思，因为照片名称中不能包含*
    # replace()方法，只能用于字符串，列表、字典不能用。第一个参数是要替换的内容，第二个参数是替换成的内容
    img_name = img['alt'].replace('*','_')
    # 保存图片，“动漫图集”文件夹需要自己手动创建。w是覆盖写，如果不存在这个文件就会创建，但是w不会创建文件夹，所以需要自己手动先创建好文件夹。
    # f是格式化字符串，是个固定语法
    # wb是写入二进制数据，二进制是最原始的数据，不需要编码
    with open(f"动漫图集/{img_name}.png",'wb') as f:
        f.write(response.content)
    # 控制一下速度，不然容易被网站检测
    time.sleep(1)


#自己写的
# for img in img_list:
#     img_url='https://pic.netbian.com'+img['src']
#     #发送请求
#     response=requests.get(url=img_url)
#     #文件名
#     img_name=img['alt'].replace('*','_')
#     with open(f"动漫图集/{img_name}.png",'wb') as f:
#         f.write(response.content)
#     time.sleep(1)