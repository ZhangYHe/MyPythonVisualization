# -*- coding:utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
import csv
#matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
# 构建数据
f = open("co2_fore 4.8.csv","r",encoding="utf-8")
f_reader = csv.reader(f)

year=[]
co2=[]
id=[]
dic_data={}

flag=0
for item in f_reader:
    # if flag==0:
    #     flag=1
    #     continue
    # else:
        #id.append(eval(item[0]))
        # year.append(eval(item[1]))
        co2.append(eval(item[1]))
        # dic_data[eval(item[1])]=eval(item[2])

for i in range(len(co2)):
    id.append(i+1965)

# 绘图
plt.bar(x=id, height=co2, color='yellowgreen', alpha=0.8)
#'lightgreen'
# 在柱状图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
for x1, yy in zip(id, co2):
    plt.text(x1, yy + 1, str(yy), ha='center', va='bottom', fontsize=5, rotation=0)
# 显示图例
plt.legend()
# 画折线图
plt.plot(id, co2, "r", ms=10, color='darkorange',label="碳排放量")
#'darkorange'
#plt.xticks(rotation=45)
plt.legend(loc="upper left")
plt.show()
