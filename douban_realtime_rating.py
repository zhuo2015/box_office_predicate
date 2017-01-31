# coding:utf-8
# get the rating of movies of Douban

import re
from bs4 import BeautifulSoup
import pandas as pd
import requests

# realtime box office
url_box = 'http://www.cbooo.cn/'
box_re = requests.get(url_box).content
box_df = pd.read_html(box_re)[0]
del box_df['Unnamed: 7']
del box_df['Unnamed: 0']

url = 'https://movie.douban.com/nowplaying/beijing/'
movie_list = requests.get(url)
soup = BeautifulSoup(movie_list.content, 'lxml')
mmlist = soup.select('#nowplaying > div.mod-bd > ul')

'''
movies_info = re.findall(
    r'\n\n\n\n\n\n\n\n\n\n                                    (.*)\n                                \n\n\n\n(.*)\n\n\n\n',
    mmlist[0].text)
print(movies_info)
[('功夫瑜伽', '5.8'),
 ('西游伏妖篇', '5.6'),
 ('大闹天竺', '3.9'),
 ('乘风破浪', '6.9'),
 ('熊出没·奇幻空...', '6.1'),
 ('太空旅客', '6.9'),
 ('降临', '7.8'),
 ('大卫贝肯之倒霉...', '4.3'),
 ('健忘村', '6.6'),
 ('血战钢锯岭', '8.7'),
 ('情圣', '6.2'),
 ('星球大战外传：...', '7.4'),
 ('冰雪女皇之冬日...', '4.8'),
 ('铁道飞虎', '5.1'),
 ('你的名字。', '8.5')]
'''

titles = re.findall(r'data-title="(.*)"', movie_list.text)[::2]
actors = re.findall(r'data-actors="(.*)"', movie_list.text)
scores = re.findall(r'data-score="(.*)"', movie_list.text)
star = re.findall(r'data-star="(.*)"', movie_list.text)
region = re.findall(r'data-region="(.*)"', movie_list.text)
director = re.findall(r'data-director="(.*)"', movie_list.text)
votecount = re.findall(r'data-votecount="(.*)"', movie_list.text)

movies_dict = []
for item in zip(titles, actors, director, scores, star, votecount, region):
    movies_dict.append(item)

df1 = pd.DataFrame(list(movies_dict), columns=["title", "actors", "director", "scores", "star", "votecount", "region"])


box_office_data = df1.merge(box_df, left_on="title", right_on='影片名称', how='outer')
print(box_office_data)
