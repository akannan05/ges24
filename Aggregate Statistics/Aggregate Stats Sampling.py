#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[7]:


ads = pd.read_csv("train_data_ads.csv")


# In[8]:


feeds = pd.read_csv("train_data_feeds.csv")


# In[9]:


ads = ads.drop_duplicates(subset='user_id', keep='first', inplace=False)
feeds = feeds.drop_duplicates(subset='u_userId', keep='first', inplace=False)


# In[10]:


feeds.shape


# In[11]:


ads.shape


# In[12]:


feeds['user_id'] = feeds['u_userId']


# In[13]:


feeds = feeds.drop('u_userId', axis = 1)


# In[14]:


merged = pd.merge(ads, feeds, on = 'user_id', how = 'outer')


# In[15]:


merged.head()


# In[16]:


merged.shape


# In[17]:


76756 + 32278


# In[18]:


merged.columns


# In[19]:


df_cust = merged[merged['label_y'] == 1]


# In[20]:


df_cust.shape


# In[21]:


df_cust


# In[22]:


import matplotlib.pyplot as plt
plt.hist(df_cust['age'])


# In[23]:


plt.hist(df_cust['residence'])


# In[24]:


plt.hist(df_cust['city'])


# In[25]:


plt.hist(df_cust['series_group'])


# In[26]:


plt.hist(df_cust['e_section'])


# In[27]:


import plotly.express as px
fig = px.pie(df_cust, values='age', names='age', title = "Potential Customer Age Distribution")
fig.show()


# In[28]:


fig = px.box(df_cust, x="age", title = "Potential Customer Age Distribution (Boxplot)")
fig.show()


# In[29]:


import plotly.express as px
fig = px.pie(df_cust, values='residence', names='residence', title = "Potential Customer Residence Distribution")
fig.show()


# In[30]:


import plotly.express as px
fig = px.pie(df_cust, values='city', names='city')
fig.show()


# In[52]:


merged['e_section'].value_counts()


# In[53]:


df_cust['e_section'].value_counts()


# In[61]:


value_counts = df_cust['e_section'].value_counts()
count_0 = value_counts.get(0, 0)  
count_1 = value_counts.get(1, 0)

labels = ['0', '1']
values = [count_0, count_1]

fig = px.pie(values=values, names=labels, title='Distribution of content preferences among Potential Customers')
fig.show()


# In[32]:


df_cust.columns


# In[33]:


import plotly.express as px
fig = px.pie(df_cust, values='series_dev', names='series_dev', title = "Potential Customer Device Series Distribution")
fig.show()


# In[34]:


import plotly.express as px
fig = px.pie(df_cust, values='series_group', names='series_group', title = "Potential Customer Device Series Group Distribution")
fig.show()


# In[35]:


import plotly.express as px
fig = px.pie(df_cust, values='emui_dev', names='emui_dev', title = "Potential Customer Device EMUI Distribution")
fig.show()


# In[36]:


import plotly.express as px
fig = px.pie(df_cust, values='device_name', names='device_name', title = "Potential Customer Device Name Distribution")
fig.show()


# In[37]:


import plotly.express as px
fig = px.pie(df_cust, values='device_size', names='device_size', title = "Potential Customer Device Size Distribution")
fig.show()


# In[38]:


df_cust.columns


# In[39]:


df_cust['pt_d'] = pd.to_datetime(df_cust['pt_d'], format='%Y%m%d%H%M')
df_cust['e_et'] = pd.to_datetime(df_cust['e_et'], format='%Y%m%d%H%M')


# In[40]:


df_cust['ads_hour'] = df_cust['pt_d'].dt.hour
df_cust['feeds_hour'] = df_cust['e_et'].dt.hour


# In[41]:


df_cust['ads_day'] = df_cust['pt_d'].dt.dayofweek
df_cust['feeds_day'] = df_cust['e_et'].dt.dayofweek


# In[42]:


df_cust['ads_dayname'] = df_cust['pt_d'].dt.day_name()
df_cust['feeds_dayname'] = df_cust['e_et'].dt.day_name()


# In[43]:


df_cust.columns


# In[44]:


import plotly.express as px
fig = px.pie(df_cust, values='ads_hour', names='ads_hour', title = "Potential Customer Advertisement Hour Viewed Distribution")
fig.show()


# In[68]:


import plotly.express as px
fig = px.pie(df_cust, values= df_cust['feeds_hour'].value_counts().values, names=df_cust['feeds_hour'].value_counts().values, title = "Potential Customer Feeds Hour Viewed Distribution")
fig.show()


# In[64]:


import plotly.express as px
fig = px.pie(df_cust, values= df_cust['ads_day'].value_counts().values, names=df_cust['ads_dayname'].value_counts().index, title = "Potential Customer Advertisement Day Viewed Distribution")
fig.show()


# In[59]:


value_counts = df_cust['e_section'].value_counts()
count_0 = value_counts.get(0, 0)  
count_1 = value_counts.get(1, 0)

labels = ['0', '1']
values = [count_0, count_1]

fig = px.pie(values=values, names=labels, title='Distribution of 0s and 1s')
fig.show()


# In[47]:


df_cust['feeds_day']


# In[67]:


import plotly.express as px
fig = px.pie(df_cust, values= df_cust['feeds_day'].value_counts().values, names=df_cust['feeds_dayname'].value_counts().index, title = "Potential Customer Feeds Day Viewed Distribution")
fig.show()


# In[50]:


df_noncust = merged[merged['label_y'] == -1.0]


# In[51]:


merged.to_csv("merged_dataframe.csv")


# In[70]:


import plotly.express as px
fig = px.pie(df_noncust, values='age', names='age', title = "Non-Potential Customer Age Distribution")
fig.show()


# In[74]:


import plotly.express as px
fig = px.pie(df_noncust, values='residence', names='residence', title = "Non-Potential Customer Residence Distribution")
fig.show()


# In[73]:


value_counts = df_noncust['e_section'].value_counts()
count_0 = value_counts.get(0, 0)  
count_1 = value_counts.get(1, 0)

labels = ['0', '1']
values = [count_0, count_1]

fig = px.pie(values=values, names=labels, title='Distribution of content preferences among Non-Potential Customers')
fig.show()


# In[75]:


import plotly.express as px
fig = px.pie(df_noncust, values='series_group', names='series_group', title = "Non-Potential Customer Device Series Group Distribution")
fig.show()


# In[76]:


import plotly.express as px
fig = px.pie(df_noncust, values='series_dev', names='series_dev', title = "Non-Potential Customer Device Series Distribution")
fig.show()


# In[77]:


import plotly.express as px
fig = px.pie(df_noncust, values='emui_dev', names='emui_dev', title = "Non-Potential Customer Device EMUI Distribution")
fig.show()


# In[78]:


df_noncust['pt_d'] = pd.to_datetime(df_noncust['pt_d'], format='%Y%m%d%H%M')
df_noncust['e_et'] = pd.to_datetime(df_noncust['e_et'], format='%Y%m%d%H%M')


# In[79]:


df_noncust['ads_hour'] = df_noncust['pt_d'].dt.hour
df_noncust['feeds_hour'] = df_noncust['e_et'].dt.hour


# In[80]:


df_noncust['ads_day'] = df_noncust['pt_d'].dt.dayofweek
df_noncust['feeds_day'] = df_noncust['e_et'].dt.dayofweek


# In[81]:


df_noncust['ads_dayname'] = df_noncust['pt_d'].dt.day_name()
df_noncust['feeds_dayname'] = df_noncust['e_et'].dt.day_name()


# In[82]:


import plotly.express as px
fig = px.pie(df_noncust, values='ads_hour', names='ads_hour', title = "Non-Potential Customer Advertisement Hour Viewed Distribution")
fig.show()


# In[83]:


import plotly.express as px
fig = px.pie(df_noncust, values= df_noncust['feeds_hour'].value_counts().values, names=df_noncust['feeds_hour'].value_counts().values, title = "Potential Customer Feeds Hour Viewed Distribution")
fig.show()


# In[84]:


import plotly.express as px
fig = px.pie(df_noncust, values= df_noncust['ads_day'].value_counts().values, names=df_noncust['ads_dayname'].value_counts().index, title = "Potential Customer Advertisement Day Viewed Distribution")
fig.show()


# In[85]:


import plotly.express as px
fig = px.pie(df_noncust, values= df_noncust['feeds_day'].value_counts().values, names=df_noncust['feeds_dayname'].value_counts().index, title = "Potential Customer Feeds Day Viewed Distribution")
fig.show()


# In[86]:


df_cust.to_csv("customer_df.csv")


# In[87]:


df_noncust.to_csv("noncustomer_df.csv")


# In[ ]:




