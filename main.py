import pandas as pd
from jb import *
from download import download
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#下载
download(input("请输入cid："))
data = pd.read_csv('./result/Barrage.csv')
#读取
b = ""
for i in data.itertuples():
    b += getattr(i,"弹幕内容")
#分词
n = jb(b)
#成图
wc = WordCloud(
    background_color='white',
    font_path='./res/微软雅黑.ttf',
    max_words=2000,
    max_font_size=100,
    min_font_size=5,
    color_func=r_color,
    random_state=50
)
word_cloud = wc.generate(n)
# 保存到本地
word_cloud.to_file('./result/barrage.jpg')
