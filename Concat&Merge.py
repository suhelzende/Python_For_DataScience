#!/usr/bin/env python
# coding: utf-8

# # Concating and Merging data frames

# In[1]:


#import section

import pandas as pd
import numpy as np


# In[10]:


df1 = pd.DataFrame({
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3']},
    index=[0,1,2,3]
)

df2 = pd.DataFrame({
    'A':['A4','A5','A6','A7'],
    'B':['B4','B5','B6','B7'],
    'C':['C4','C5','C6','C7'],
    'D':['D4','D5','D6','D7']},
    index=[4,5,6,7]
)

df3 = pd.DataFrame({
    'A':['A8','A9','A10','A11'],
    'B':['B8','B9','B10','B11'],
    'C':['C8','C9','C10','C11'],
    'D':['D8','D9','D10','D11']},
    index=[8,9,10,11]
)


# In[9]:


df3


# In[13]:


#CONCATING THE DATAFRAMES
result = pd.concat([df1,df2,df3])
result


# In[14]:


#CONCATING THE DATAFRAMES with key name to identify data from dataframes
result = pd.concat([df1,df2,df3],keys=['df1','df2','df3'])
result


# In[15]:


#getting the specific data frame
result.loc['df2']


# In[ ]:





# In[17]:


#joining at column level
df1


# In[22]:


df4 = pd.DataFrame({
    'B':['B2','B3','B6','B7'],
    'D':['D2','D3','D6','D7'],
    'F':['F2','F3','F6','F7']},
    index=[2,3,6,7]
    )
#outer join which is default if we deos not provide  join property then it is outer by default
result = pd.concat([df1,df4], axis=1, join='outer')
result


# In[24]:


#inner join same as intersection
result = pd.concat([df1,df4], axis = 1 , join="inner")
result


# # Mergin (same as joining in SQL)

# In[25]:


df_a = pd.DataFrame({
    'subject_id':['1','2','3','4'],
    'first_name' :['Suhel','Vikram','Rushi','Dhananjay'],
    'last_name':['Zende','Ghadge','Koli','Bhosale']
})

df_b = pd.DataFrame({
    'subject_id':['5','6','7'],
    'first_name' :['Nilesh','Rahul','Satish'],
    'last_name':['Suradkar','Lokhande','Jaykar']
})

df_c = pd.DataFrame({
    'subject_id':['1','2','3','4','5','6','7'],
    'test_id':[51,15,15,61,16,16,14]
})


# In[26]:


df_c


# In[30]:


#merging the above Dataframes on common column i.e. 'subject_id'
pd.merge(df_a,df_c,on="subject_id")


# In[32]:


#merging with outer join
pd.merge(df_a,df_c,on="subject_id",how="outer")

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




