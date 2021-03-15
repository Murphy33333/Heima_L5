#coding by Murphy

import pandas as pd
#
# import nltk
# nltk.download('punkt')
from nltk.tokenize import word_tokenize

#数据加载
data=pd.read_csv(r'D:\黑马课程\第五课\Market_Basket_Optimisation.csv',header=None)
print(data)
print(data.shape)
#将数据放到transactions中
transactions=[]
#存储字典key：value
item_count={}
for i in range(data.shape[0]):
    temp=[]
    for j in range(data.shape[1]):
        item=str(data.values[i,j])
        if item !='nan':
            temp.append(item)
            if item not in item_count:
                item_count[item]=1
            else:
                item_count[item]+= 1

    transactions.append(temp)
print(transactions)
from wordcloud import WordCloud
#去掉停用词，即比较经常使用的词（虚词，您好，我的）
def remove_stop_words(f):
    stop_words=[]
    for stop_word in stop_words:
        f=f.replace(stop_word,'')
    return f
def create_word_cloud(f):
	f = remove_stop_words(f)
	cut_text = word_tokenize(f)
	cut_text = " ".join(cut_text)
	wc = WordCloud(
		max_words=100,
		width=2000,
		height=1200,
    )
	wordcloud = wc.generate(cut_text)
	wordcloud.to_file("wordcloud.jpg")
#生成慈云
all_word=' '.join('%s'%item for item in transactions)
#print(all_word)
#create_word_cloud(all_word)

#有问题，词云包安装后运行报如下错误，需要downloa （‘punkt")试了很多方法都解决不了
#
# import nltk
# nltk.download('punkt')

#Top10的商品有哪些
print(item_count)
print(item_count.items())
print('Top10的商品有哪些')
Top10=sorted(item_count.items(),key=lambda x:x[1],reverse=True)[:10]
print(Top10)
