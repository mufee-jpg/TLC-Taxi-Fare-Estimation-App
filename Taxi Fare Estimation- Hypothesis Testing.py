#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from scipy import stats


# In[2]:


taxi_data = pd.read_csv("2017_Yellow_Taxi_Trip_Data.csv", index_col = 0)


# In[3]:


taxi_data.describe(include='all')


# In[4]:


taxi_data.groupby(['payment_type'])['fare_amount'].mean()


# In[5]:


credit_card = taxi_data[taxi_data['payment_type']==1]['fare_amount']
cash = taxi_data[taxi_data['payment_type']==2]['fare_amount']
stats.ttest_ind(a=credit_card,b=cash,equal_var=False)


# In[ ]:




