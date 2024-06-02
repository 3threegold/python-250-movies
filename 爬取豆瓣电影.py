from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) appendpleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
movie_list = []

# for i in range(0,250,25):
#     url = f"https://movie.douban.com/top250?start={i}&filter="
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     for movie in soup.find_all('div',class_='item'):
#         rank = movie.find('em').text
#         title = movie.find('span',class_='title').text
#         rating = movie.find('span',class_='rating_num').text
#         movie_list.append({'名次':rank,'电影名':title,'评分':rating})


# df = pd.DataFrame()
# df.to_excel('douban_top250_movies.xlsx', index=False)

movie_list=[]
for i in range(0,250,25):
    url=f"https://movie.douban.com/top250?start={i}&filter="
    response=requests.get(url=url,headers=headers)
    response.encoding='utf-8'
    soup=BeautifulSoup(response.text,'html.parser')
    #一面有多部电影，需要用for循环
    for movie in soup.select('.item'):
        #电影名
        title=movie.find('span',class_='title').text
        #电影评分
        rating=movie.find('span',class_='rating_num').text
        #电影评分
        rank=movie.find('em').text
        print(f"名次:{rank},电影:{title},评分:{rating}")
        movie_list.append({'名次':rank,'电影名':title,'评分':rating})

#存放到excel中
df=pd.DataFrame(movie_list)
df.to_excel('豆瓣_top250_movies.xlsx',index=False)