import requests
import pandas as pd
from lxml import etree

def download(cid):
    url = "https://comment.bilibili.com/"+str(cid)+'.xml'
    response = requests.get(url)
    xml = etree.fromstring(response.content)
    barrage = xml.xpath("/i/d/text()")
    barrage_df = pd.DataFrame(barrage, columns=['弹幕内容'])
    # 保存到本地
    barrage_df.to_csv("./result/Barrage.csv", encoding='utf_8_sig')
