#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd               
import numpy as np               

df = pd.read_csv('2017_Yellow_Taxi_Trip_Data.csv')
print("done")


# In[ ]:


df.head(10)


# In[ ]:


df.info()


# In[ ]:


df.describe()


# In[ ]:


df_sort = df.sort_values(['trip_distance'],ascending=False)['trip_distance']
df_sort.head(10)


# In[ ]:


total_amount_sorted = df.sort_values(
    ['total_amount'], ascending=False)['total_amount']
total_amount_sorted.head(20)


# In[ ]:


total_amount_sorted.tail(20)


# In[ ]:


df['payment_type'].value_counts()


# In[ ]:


avg_cc_tip = df[df['payment_type']==1]['tip_amount'].mean()
print('Avg. cc tip:', avg_cc_tip)

avg_cash_tip = df[df['payment_type']==2]['tip_amount'].mean()
print('Avg. cash tip:', avg_cash_tip)


# In[ ]:


df['VendorID'].value_counts()


# In[ ]:


df.groupby(['VendorID']).mean(numeric_only=True)[['total_amount']]


# In[ ]:


df.groupby('VendorID')['total_amount'].mean()


# In[ ]:


credit_card = df[df['payment_type']==1]

credit_card['passenger_count'].value_counts()


# In[ ]:


credit_card.groupby(['passenger_count']).mean(numeric_only=True)[['tip_amount']]

