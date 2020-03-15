#!/usr/bin/env python
# coding: utf-8

# # Wroking with the Slaes data set
# 

# In[1]:


#imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


#loading the data set
Data = pd.read_csv('Datasets/bigmart_data.csv')

#droping null
Data = Data.dropna(how='any')

#displaying
Data.head()


# # We Will create a line chart to show mean price per item

# In[18]:



#in matplot the line chart is default chart type
price_by_item = Data.groupby('Item_Type').Item_MRP.mean()
price_by_item


# In[19]:


#getting the index on x axis
x = price_by_item.index.tolist()

#getting mean value on y axis
y = price_by_item.values.tolist();

plt.figure(figsize=(16,8))
plt.plot(x,y)
plt.title('Mean Price per Item type')
plt.xlabel('Item Type')
plt.ylabel('Mean Price')


# # We will create Bar Chart to show mean sales for each outlet Size

# In[21]:


sales_by_outlet_size = Data.groupby('Outlet_Size').Item_Outlet_Sales.mean()
sales_by_outlet_size


# In[25]:


#sorting by sales
sales_by_outlet_size.sort_values(inplace=True)
sales_by_outlet_size


# In[38]:


#getting axis valus
x = sales_by_outlet_size.index.tolist()
y = sales_by_outlet_size.values.tolist()

plt.title('Sales by Outlet Size')
plt.bar(x,y,color=['red','green','blue'])
plt.xlabel('Outlet Size')
plt.ylabel('Sales')


# # Drawing Histograms to see the distribution of MRP
# 

# In[42]:


plt.title('Item MRP Distribution')
plt.xlabel('ITEM MRP')
plt.ylabel('Frequency')

#drawing the histogram
#bins is the range of bars
plt.hist(Data['Item_MRP'], bins=40, color='lightblue')


# # Box plots to show the sales distribution
# 

# In[43]:


data_sales = Data[['Item_Outlet_Sales']]

#creating an outlier point shape
red_diamond = dict(markerfacecolor='r',marker='D')

#setting Title
plt.title('Item sales distribution')

plt.boxplot(data_sales.values,labels=['Item sales'], flierprops=red_diamond)


# In[47]:


data_weigth_mrp = Data[['Item_Weight','Item_MRP']]

#creating an outlier point shape
red_diamond = dict(markerfacecolor='r',marker='D')

#setting Title
plt.title('Item sales distribution')

plt.boxplot(data_weigth_mrp.values,labels=['Item weight','Item MRP'], flierprops=red_diamond)


# # Violin plot
# - Density distribution of item_weight and item price

# In[50]:


data = Data[['Item_Weight','Item_MRP']]

plt.xticks(ticks=[1,2], labels=['Item_Weight','Item_MRP'])
plt.violinplot(data.values)


# # Scatter Plots 
# - Relative Distribution of Item weight and it's visibility

# In[54]:


plt.xlabel('Item_Weight')
plt.ylabel('Item_Visibility')
plt.scatter(Data['Item_Weight'][:200],Data['Item_Visibility'][:200])


# # Bubble Plot
# - Relative distribution of sale, item_price and visibility
# - we can show inter dependency of  3  variables

# In[58]:


plt.xlabel('Item_MRP')
plt.ylabel('Item_Outlet_sales')

plt.title('Item Outlet Sales vs Item MRP')

#Here S is the size of bubble higher the visibility bigger the bubble
plt.scatter(Data["Item_MRP"][:100],Data["Item_Outlet_Sales"][:100],s = Data["Item_Visibility"][:100] * 1000,c='red')


# In[ ]:




