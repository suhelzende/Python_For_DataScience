#!/usr/bin/env python
# coding: utf-8

# # Data Manipulation with Pandas
# 

# In[1]:


#importing required libararies
import pandas as pd
import numpy as np


# In[11]:


#reading csv
data_mart = pd.read_csv("DataSets/bigmart_data.csv")

#removing / dropping null
data_mart = data_mart.dropna(how="any")

#reading top 5 records
data_mart.head()


# In[14]:



#sorting the data and storing in another dta frame
data_mart_sorted = data_mart.sort_values(by="Outlet_Establishment_Year");
data_mart_sorted[:5]


# In[15]:


data_mart[:5]


# In[16]:


#sorting the data in original data frame
#using inplace
data_mart.sort_values(by="Outlet_Establishment_Year",ascending=False, inplace=True)

data_mart[:5]


# In[17]:


#reading csv in another variable
new_data_mart = pd.read_csv("DataSets/bigmart_data.csv")

#removing / dropping null
new_data_mart = data_mart.dropna(how="any")

#reading top 5 records
new_data_mart.head()


# # sorting using more than one column
# 

# #we can pass list of column names to the sort_values method 
# 

# #the first coulmn name passed will be considered for sorting firct then the second and so on
# 

# In[21]:


new_data_mart.sort_values(by=['Outlet_Establishment_Year','Item_Outlet_Sales'],ascending = False,inplace = True)


# In[22]:


new_data_mart[:5]


# In[23]:


new_data_mart.sort_values(by=['Item_Outlet_Sales','Outlet_Establishment_Year'],ascending = False,inplace = True)
new_data_mart[:5]


# # Sort by sort_index to sort using row number

# In[25]:


#sort using row number
new_data_mart.sort_index(inplace = True)


# In[26]:


new_data_mart[:5]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




