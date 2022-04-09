import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import seaborn as sns

sns.set()
#f = pd.read_csv('德国发电量预测4.6.csv')
#f.head()
f=open("co2_fore 4.8.csv","r",encoding="utf-8")
f_reader = csv.reader(f)

year=[]
co2=[]
id=[]
dic_data={}

#flag=0
for item in f_reader:
    # if flag==0:
    #     flag=1
    #     continue
    #else:
        #id.append(eval(item[0]))
        # year.append(eval(item[1]))
    if item[3]!='':
        co2.append(eval(item[3]))
        # dic_data[eval(item[1])]=eval(item[2])
#s = f.pivot(index='id',columns='year',values='co2')

for i in range(len(co2)):
    id.append(i+1)

# 柱状图
sns.barplot(x=id,y=co2,palette='PuBu')
#"Greens_d"palette='OrRd_r'"summer"'YlGnBu'

#显示数据
# for x1, yy in zip(id, co2):
#     plt.text(x1, yy + 1, str(yy), ha='center', va='bottom', fontsize=5, rotation=0)
#plt.legend()

#折线
plt.plot(id, co2, "r", ms=10, color='goldenrod',label="碳排放量")
#'darkorange''slategrey'

#sns.countplot(data=dic_data, palette="Greens_d")
plt.show()

