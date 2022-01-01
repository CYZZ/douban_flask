import jieba
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from wordcloud import WordCloud  # 词云
import sqlite3


con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = 'select instroduction from movie250'
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
# print(text)
cur.close()
con.close()

cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))

img = Image.open(r'static/image/tree.jpeg')
img_array = np.array(img)  # 将图片转换为数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="STHeiti Light.ttc"
)
wc.generate_from_text(string)

# 绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')  # 是否显示坐标轴

# plt.show()  # 显示

plt.savefig(r'static/image/word.png')


