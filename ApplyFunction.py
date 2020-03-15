#!/usr/bin/env python
# coding: utf-8

# # Apply Function to access the data
# Apply Function is used to access data 
# 
# instead of accessing the data using for loop iteration one must use apply function for easy and fast access
# 
# Apply funcstion is used for pre-processing

# In[1]:


#imports
import pandas as pd
import numpy as np


# In[24]:


#reading data
data = pd.read_csv("DataSets/bigmart_data.csv");


# In[25]:


#accessing data using apply function
data.apply(lambda x : x)[:5]


# In[26]:


#accessing the first row
data.apply(lambda x : x[0])


# In[27]:


#accessing first column
data.apply(lambda x: x[2],axis=1)


# In[28]:


data.apply(lambda x: x["Item_Fat_Content"],axis=1)


# In[29]:


data["Item_MRP"]


# In[30]:


def Clip_Price(price):
    if price > 200 :
        price = 200
    return price

data["Item_MRP"].apply(lambda x : Clip_Price(x))


# # Encode categories to numbers so that ML Model will work well

# In[31]:


data['Outlet_Location_Type'][:5]


# In[32]:


def Encode_Location(location):
    if location == 'Tier 1':
        label = 1
    elif location == 'Tier 2':
        label = 2
    else:
        label = 3
    return label
data['Outlet_Location_Type'].apply(Encode_Location)


# In[33]:


data


# In[34]:


data.head()


# In[35]:


data = data.dropna(how="any")


# In[ ]:





# In[36]:


data


# # Aggregate  Functions

# In[37]:


#using group by Item type
data_group=data.groupby("Item_Type")


# In[40]:


#Display first few rows
data_group.first()


# In[43]:


data_group.Item_MRP.mean()


# In[44]:


#grouping on multiple columns
data_group_item = data.groupby(["Item_Type","Item_Fat_Content"])


# In[45]:


data_group_item.first()


# In[59]:


data.groupby("Item_Type").Item_MRP.mean().loc["Baking Goods"]


# # Cross tab calculates the frequency of data group

# In[64]:


#cross tab the Outlet_Size and Outlet_Location_Type
pd.crosstab(data["Outlet_Size"],data["Outlet_Location_Type"],margins=True)


# # Pivot_table is used to see the aggregate results by grouping the rows

# parameters of pivot_table function are
# 
#     1 : data frame
#     
#     2 : index : grouping column names
#     
#     3 : values : coulmn name for aggregation
#     
# By default aggregate function returns mean 
# 
# values coumn shoulb be numric
#     

# In[71]:


pd.pivot_table(data, index=['Outlet_Establishment_Year'],values="Item_Outlet_Sales")


# In[72]:


pd.pivot_table(data, index=['Outlet_Establishment_Year','Outlet_Size','Outlet_Location_Type'], values="Item_Outlet_Sales")


# # we can use the numpy aggregate function as follows

# In[76]:


pd.pivot_table(data,index=['Outlet_Establishment_Year','Outlet_Size','Outlet_Location_Type'], values="Item_Outlet_Sales",aggfunc=[sum,np.mean,np.median,min,max,np.std])


# In[ ]:




