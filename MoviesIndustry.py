#!/usr/bin/env python
# coding: utf-8

# In[111]:


#Import libraries


import pandas as pd
import seaborn as sns
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8) 
#Adjust the configuration of the plot we will create
#matplotlib inline will make your plot outputs appear and be stored within the notebook

#Read in the data

df = pd.read_csv(r'C:/Users/rodri/OneDrive/Documentos/PYTHON/DATASETS/movies.csv')



# In[112]:


df.head(10)


# In[113]:


#Let's check the missing value

for col in df.columns:
        pct_missing = np.mean(df[col].isnull())
        print('{}-{}'.format(col, pct_missing))


# In[114]:


for col in df.columns:
        pct_missing = np.sum(df[col].isnull())
        print('{}-{}'.format(col, pct_missing))
        #rating-77 score-3 writer-3 company-17 runtime-4 yearcorrect-2


# In[118]:


df['rating']=df['rating'].fillna("Not Rated")


# In[119]:


print(df.rating)


# In[91]:


df.dtypes


# In[41]:


#Now let's change the format of gross and budget columns so they don't have that .0 that is senseless
df['budget'] = pd.to_numeric(df['budget'], errors='coerce').fillna(0).astype(int)
df['gross'] = pd.to_numeric(df['gross'], errors='coerce').fillna(0).astype(int) 
df['votes'] = pd.to_numeric(df['votes'], errors='coerce').fillna(0).astype(int)


# In[35]:


#As we can see, some of the values in year doesn't match with the years in released, so we have to create a column that has the correct info
#To do that,first we'll change the format of released from object to string
df['released'] = df['released'].astype(str)
#Then we apply extract in which we're looking for 4 adjacent digits in [0,9], which would only correspond to the year value
df['yearcorrect'] = df['released'].str.extract(pat = '([0-9]{4})')


# In[103]:


df.sort_values(by=['gross'], inplace = False, ascending = False)


# In[43]:


pd.set_option('display.max_rows', None)


# In[117]:


df.drop_duplicates()


# In[ ]:




