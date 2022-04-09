import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# f = pd.read_csv('一阶灵敏度热力图.csv')
#f = pd.read_csv('一阶灵敏度.csv')
f = pd.read_csv('全局灵敏度.csv')
f.head()

# pivot = f.pivot(index='Function Value',columns='Parameters',values='First-order sobol index')
pivot = f.pivot(index='Function Value',columns='Parameters',values='Total-effect sobol index')

sns.heatmap(pivot,annot= True,fmt= "f",linewidths= 1.6,cmap="RdPu")
#sns.heatmap(pivot,cmap= )
#"RdPu""RdBu_r"
plt.show()