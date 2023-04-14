#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


sales_data = r'C:\Users\himan\Downloads\sales_data_sample.csv'


# In[5]:


df = pd.read_csv(sales_data)

#I received a UnicodeDecodeError. It occurs when decoding an str string from a certain coding. As the codings are mapped only 
#a to limited number of str strings to unicode characters, a formation of illegal sequence of str characters is going to 
#cause the coding-specific decode() to fail.


# In[9]:


import chardet
with open(sales_data, 'rb') as rawdata:
    result = chardet.detect(rawdata.read(100000))
    print(result)
    
    #we manually determined the character encoding and use it alongside the while reading the csv


# In[10]:


df = pd.read_csv(sales_data, encoding ='Windows-1252')


# In[11]:


df.head()
#this now works


# In[12]:


df.isnull().sum()


# In[13]:


df.describe()


# In[14]:


df.info()


# In[15]:


df.tail()


# In[16]:


df.shape


# In[17]:


df.columns


# In[18]:


#our data's date is imported as string. So we will first covert it in datetime format

df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])


# In[19]:


df.info()
#cross check if it's done


# In[20]:


#EXPLORATORY DATA ANALYSIS
#What is the overall sales trend

#Extracting month and year from date

df['month_year'] = df['ORDERDATE'].apply(lambda x: x.strftime('%Y-%m'))


# In[21]:


df['month_year']

#we have data for almost more than a year


# In[24]:


#We can see all the order numbers by each month of the year

df.groupby('month_year').sum()


# In[33]:


df.groupby('month_year').sum()['SALES']


# In[35]:


sales_trend = df.groupby('month_year').sum()['SALES'].reset_index()


# In[36]:


print(sales_trend)


# In[38]:


plt.plot(sales_trend['month_year'], sales_trend['SALES'])


# In[44]:


plt.figure(figsize=(15, 6))
plt.plot(sales_trend['month_year'], sales_trend['SALES'])
plt.xticks(rotation = 'vertical', size = 8)
plt.show


# In[ ]:


#sales were quite low from the 2003-01 till 2003-08. From 2003-08 to 2003-09, a gradual increase can be seen, thereafter a sharp rise in sales is observed in 2003-11.


# In[45]:


#TOP SELLING PRODUCTS BY SALES

df.groupby('PRODUCTCODE').sum()['SALES']


# In[66]:


top_selling_products = pd.DataFrame(df.groupby('PRODUCTLINE').sum()['SALES'])


# In[67]:


print(top_selling_products)


# In[68]:


top_selling_products.sort_values('SALES', ascending= False)
# We sorted in descending order


# In[69]:


#first 10 top selling. Maximum sales was done by Classic Cars.
top_selling_products[:10]


# In[70]:


lk = df.groupby(['PRODUCTCODE', 'PRODUCTLINE']).sum()['SALES']


# In[71]:


lk


# In[87]:


deal_size = pd.DataFrame(df.groupby('COUNTRY').sum()['SALES'])


# In[88]:


deal_size


# In[89]:


#top consumer countries

deal_size.sort_values('SALES', ascending= False)


# In[90]:


deal_size[:10]


# In[102]:


plt.figure(figsize=(10,8))

sns.countplot(df['PRODUCTLINE'])

plt.show()


# In[103]:


deal_size = pd.DataFrame(df.groupby(['PRODUCTLINE', 'DEALSIZE']).sum()['SALES'])


# In[104]:


deal_size


# In[107]:


country_size = pd.DataFrame(df.groupby(['COUNTRY','PRODUCTLINE']).sum()['SALES'])


# In[108]:


country_size


# In[114]:


country_size.sort_values('SALES', ascending = False)


# In[ ]:




