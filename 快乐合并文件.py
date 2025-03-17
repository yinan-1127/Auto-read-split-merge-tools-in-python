#!/usr/bin/env python
# coding: utf-8

# # 快乐合并！

# ## 完成这个脚本我们需要以下几个条件
# 
# 1. 请把要合并的东西放在和该代码同一个文件夹里
# 2. 请固定他的文件格式
# 3. 然后就可以快乐运行啦！

# In[ ]:


import pandas as pd
import os


# In[ ]:


files = [ i for i in os.listdir() if i.endswith('csv')]
files


# In[ ]:


data = pd.DataFrame()
for f in files:
    df = pd.read_csv(f)
    print(f"LOADING...... \n {f} ")
    df['filename'] =f.split(".")[0]
    df['index'] = df.index
    data = pd.concat([data,df],axis = 0)
    print(f"SUCCESS! The Merge result is...... \n {data.shape}")


# In[ ]:


data.iloc[0]['filename']


# In[ ]:


###实践开始!
# import numpy as np
# data['score'] = np.nan
# data['score'] = data['score'].apply(lambda x:np.random.randn())
# data['score'] = data['score'].apply(lambda x: ((x+4)/8)*100)

# ###查看分布
# import matplotlib.pyplot as plt
# data['score'].hist()
# plt.show()


# In[ ]:


#把打好分的data总文件导入进来
data.head()


# In[ ]:


samples = list(data['filename'].unique())
samples


# In[ ]:


grouped_df ={}
grouped = data.groupby("filename")
print(grouped.count())


# In[ ]:


for i,(name,group) in enumerate(grouped):
    grouped_df[f'df_{i+1}'] =group.reset_index(drop=True)


# In[ ]:


grouped_df


# In[ ]:


for key, value in grouped_df.items():
    print(key)
    filnm = value.iloc[0]['filename']
    print(filnm)
    key = pd.DataFrame(value)
    print(key.shape)
    key.to_csv(f"{filnm}_score.csv")
    print(f"{filnm}_score has been saved")


# In[ ]:




