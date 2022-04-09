# mport matplotlib.pyplot as plt
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

TotalFile = open("total2.csv","r",encoding="utf-8")
Total_reader = csv.reader(TotalFile)

bjy=[]
gjy=[]
rg=[]
rb=[]

for item in Total_reader:
    # if flag==0:
    #     flag=1
    #     continue
    # else:
        bjy.append(eval(item[12]))
        gjy.append(eval(item[13]))
        rg.append(eval(item[5]))
        rb.append(eval(item[8]))

# print(bjy)
#sns.kdeplot(x=rg,y=gjy,shade=True)
#sns.kdeplot(x=rb,y=bjy,shade=True,colors=sns.color_palette('Paired'),cbar=True)
sns.kdeplot(x=rg,y=gjy,shade=True,colors=sns.color_palette('Paired'),cbar=True)
plt.show()