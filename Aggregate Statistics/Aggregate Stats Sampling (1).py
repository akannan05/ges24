#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


ads = pd.read_csv("train_data_ads.csv")


# In[4]:


feeds = pd.read_csv("train_data_feeds.csv")


# In[5]:


ads = ads.drop_duplicates(subset='user_id', keep='first', inplace=False)
feeds = feeds.drop_duplicates(subset='u_userId', keep='first', inplace=False)


# In[6]:


feeds.shape


# In[7]:


ads.shape


# In[8]:


feeds['user_id'] = feeds['u_userId']


# In[9]:


feeds = feeds.drop('u_userId', axis = 1)


# In[10]:


merged = pd.merge(ads, feeds, on = 'user_id', how = 'outer')


# In[11]:


merged.head()


# In[12]:


merged.shape


# In[13]:


76756 + 32278


# In[14]:


merged.columns


# In[15]:


df_cust = merged[merged['label_y'] == 1]


# In[16]:


df_cust.shape


# In[17]:


df_cust


# In[18]:


import matplotlib.pyplot as plt
plt.hist(df_cust['age'])


# In[19]:


plt.hist(df_cust['residence'])


# In[20]:


plt.hist(df_cust['city'])


# In[21]:


plt.hist(df_cust['series_group'])


# In[22]:


plt.hist(df_cust['e_section'])


# In[23]:


import plotly.express as px
fig = px.pie(df_cust, values='age', names='age', title = "Potential Customer Age Distribution")
fig.show()


# In[24]:


fig = px.box(df_cust, x="age", title = "Potential Customer Age Distribution (Boxplot)")
fig.show()


# In[25]:


import plotly.express as px
fig = px.pie(df_cust, values='residence', names='residence', title = "Potential Customer Residence Distribution")
fig.show()


# In[26]:


import plotly.express as px
fig = px.pie(df_cust, values='city', names='city')
fig.show()


# In[27]:


merged['e_section'].value_counts()


# In[28]:


df_cust['e_section'].value_counts()


# In[29]:


value_counts = df_cust['e_section'].value_counts()
count_0 = value_counts.get(0, 0)  
count_1 = value_counts.get(1, 0)

labels = ['0', '1']
values = [count_0, count_1]

fig = px.pie(values=values, names=labels, title='Distribution of content preferences among Potential Customers')
fig.show()


# In[30]:


df_cust.columns


# In[31]:


import plotly.express as px
fig = px.pie(df_cust, values='series_dev', names='series_dev', title = "Potential Customer Device Series Distribution")
fig.show()


# In[32]:


import plotly.express as px
fig = px.pie(df_cust, values='series_group', names='series_group', title = "Potential Customer Device Series Group Distribution")
fig.show()


# In[33]:


import plotly.express as px
fig = px.pie(df_cust, values='emui_dev', names='emui_dev', title = "Potential Customer Device EMUI Distribution")
fig.show()


# In[34]:


import plotly.express as px
fig = px.pie(df_cust, values='device_name', names='device_name', title = "Potential Customer Device Name Distribution")
fig.show()


# In[35]:


import plotly.express as px
fig = px.pie(df_cust, values='device_size', names='device_size', title = "Potential Customer Device Size Distribution")
fig.show()


# In[36]:


df_cust.columns


# In[37]:


df_cust['pt_d'] = pd.to_datetime(df_cust['pt_d'], format='%Y%m%d%H%M')
df_cust['e_et'] = pd.to_datetime(df_cust['e_et'], format='%Y%m%d%H%M')


# In[38]:


df_cust['ads_hour'] = df_cust['pt_d'].dt.hour
df_cust['feeds_hour'] = df_cust['e_et'].dt.hour


# In[39]:


df_cust['ads_day'] = df_cust['pt_d'].dt.dayofweek
df_cust['feeds_day'] = df_cust['e_et'].dt.dayofweek


# In[40]:


df_cust['ads_dayname'] = df_cust['pt_d'].dt.day_name()
df_cust['feeds_dayname'] = df_cust['e_et'].dt.day_name()


# In[41]:


df_cust.columns


# In[42]:


import plotly.express as px
fig = px.pie(df_cust, values='ads_hour', names='ads_hour', title = "Potential Customer Advertisement Hour Viewed Distribution")
fig.show()


# In[92]:


import plotly.express as px
fig = px.pie(df_cust, values= df_cust['feeds_hour'].value_counts().values, names=df_cust['feeds_hour'].value_counts().index, title = "Potential Customer Feeds Hour Viewed Distribution")
fig.show()


# In[44]:


import plotly.express as px
fig = px.pie(df_cust, values= df_cust['ads_day'].value_counts().values, names=df_cust['ads_dayname'].value_counts().index, title = "Potential Customer Advertisement Day Viewed Distribution")
fig.show()


# In[45]:


value_counts = df_cust['e_section'].value_counts()
count_0 = value_counts.get(0, 0)  
count_1 = value_counts.get(1, 0)

labels = ['0', '1']
values = [count_0, count_1]

fig = px.pie(values=values, names=labels, title='Distribution of Content Preferences among Customers')
fig.show()


# In[46]:


df_cust['feeds_day']


# In[47]:


import plotly.express as px
fig = px.pie(df_cust, values= df_cust['feeds_day'].value_counts().values, names=df_cust['feeds_dayname'].value_counts().index, title = "Potential Customer Feeds Day Viewed Distribution")
fig.show()


# In[48]:


df_noncust = merged[merged['label_y'] == -1.0]


# In[49]:


merged.to_csv("merged_dataframe.csv")


# In[50]:


import plotly.express as px
fig = px.pie(df_noncust, values='age', names='age', title = "Non-Potential Customer Age Distribution")
fig.show()


# In[51]:


import plotly.express as px
fig = px.pie(df_noncust, values='residence', names='residence', title = "Non-Potential Customer Residence Distribution")
fig.show()


# In[52]:


value_counts = df_noncust['e_section'].value_counts()
count_0 = value_counts.get(0, 0)  
count_1 = value_counts.get(1, 0)

labels = ['0', '1']
values = [count_0, count_1]

fig = px.pie(values=values, names=labels, title='Distribution of content preferences among Non-Potential Customers')
fig.show()


# In[53]:


import plotly.express as px
fig = px.pie(df_noncust, values='series_group', names='series_group', title = "Non-Potential Customer Device Series Group Distribution")
fig.show()


# In[54]:


import plotly.express as px
fig = px.pie(df_noncust, values='series_dev', names='series_dev', title = "Non-Potential Customer Device Series Distribution")
fig.show()


# In[55]:


import plotly.express as px
fig = px.pie(df_noncust, values='emui_dev', names='emui_dev', title = "Non-Potential Customer Device EMUI Distribution")
fig.show()


# In[56]:


df_noncust['pt_d'] = pd.to_datetime(df_noncust['pt_d'], format='%Y%m%d%H%M')
df_noncust['e_et'] = pd.to_datetime(df_noncust['e_et'], format='%Y%m%d%H%M')


# In[57]:


df_noncust['ads_hour'] = df_noncust['pt_d'].dt.hour
df_noncust['feeds_hour'] = df_noncust['e_et'].dt.hour


# In[58]:


df_noncust['ads_day'] = df_noncust['pt_d'].dt.dayofweek
df_noncust['feeds_day'] = df_noncust['e_et'].dt.dayofweek


# In[59]:


df_noncust['ads_dayname'] = df_noncust['pt_d'].dt.day_name()
df_noncust['feeds_dayname'] = df_noncust['e_et'].dt.day_name()


# In[60]:


import plotly.express as px
fig = px.pie(df_noncust, values='ads_hour', names='ads_hour', title = "Non-Potential Customer Advertisement Hour Viewed Distribution")
fig.show()


# In[93]:


import plotly.express as px
fig = px.pie(df_noncust, values= df_noncust['feeds_hour'].value_counts().values, names=df_noncust['feeds_hour'].value_counts().index, title = "Non-Potential Customer Feeds Hour Viewed Distribution")
fig.show()


# In[62]:


import plotly.express as px
fig = px.pie(df_noncust, values= df_noncust['ads_day'].value_counts().values, names=df_noncust['ads_dayname'].value_counts().index, title = "Non-Potential Customer Advertisement Day Viewed Distribution")
fig.show()


# In[63]:


import plotly.express as px
fig = px.pie(df_noncust, values= df_noncust['feeds_day'].value_counts().values, names=df_noncust['feeds_dayname'].value_counts().index, title = "Non-Potential Customer Feeds Day Viewed Distribution")
fig.show()


# In[64]:


df_cust.to_csv("customer_df.csv")


# In[65]:


df_cust.columns


# In[66]:


df_noncust.to_csv("noncustomer_df.csv")


# In[ ]:





# In[67]:


import plotly.graph_objects as go


fig = go.Figure(data=[
    go.Bar(name='Potential Customers', x=df_cust['age'].value_counts().index, y=df_cust['age'].value_counts().values),
    go.Bar(name='Non Customers', x=df_noncust['age'].value_counts().index, y=df_noncust['age'].value_counts().values)
])
# Change the bar mode
fig.update_layout(barmode='group', title = "Grouped Barchart to Visualize Age Distribution Differences")
fig.show()


# In[68]:


fig = px.pie(merged, values=merged['label_y'].value_counts().values, names=merged['label_y'].value_counts().index, title = "Label Distribution")
fig.show()


# In[69]:


merged.shape


# In[70]:


merged['label_y'].value_counts()


# In[71]:


merged.columns


# In[72]:


ads.columns


# In[73]:


feeds.columns


# In[74]:


feeds.shape


# In[75]:


feeds['cillabel'].value_counts()


# In[76]:


import plotly.express as px
fig = px.pie(df_cust, values='gender', names='gender', title = "Potential Customer Gender Distribution")
fig.show()


# In[77]:


import plotly.express as px
fig = px.pie(df_noncust, values='gender', names='gender', title = "Non Customer Gender Distribution")
fig.show()


# In[78]:


df_cust['gender'].unique()


# In[79]:


import plotly.graph_objects as go


fig = go.Figure(data=[
    go.Bar(name='Potential Customers', x=df_cust['gender'].value_counts().index, y=df_cust['gender'].value_counts().values),
    go.Bar(name='Non Customers', x=df_noncust['gender'].value_counts().index, y=df_noncust['gender'].value_counts().values)
])
# Change the bar mode
fig.update_layout(barmode='group', title = "Grouped Barchart to Visualize Age Distribution Differences")
fig.show()


# In[80]:


import plotly.graph_objects as go


fig = go.Figure(data=[
    go.Bar(name='Potential Customers', x=df_cust['residence'].value_counts().index, y=df_cust['residence'].value_counts().values),
    go.Bar(name='Non Customers', x=df_noncust['residence'].value_counts().index, y=df_noncust['residence'].value_counts().values)
])
# Change the bar mode
fig.update_layout(barmode='group', title = "Grouped Barchart to Visualize Residence Distribution Differences")
fig.show()


# In[81]:


import plotly.graph_objects as go


fig = go.Figure(data=[
    go.Bar(name='Potential Customers', x=df_cust['e_section'].value_counts().index, y=df_cust['e_section'].value_counts().values),
    go.Bar(name='Non Customers', x=df_noncust['e_section'].value_counts().index, y=df_noncust['e_section'].value_counts().values)
])
# Change the bar mode
fig.update_layout(barmode='group', title = "Grouped Barchart to Visualize Content Preference Distribution Differences")
fig.show()


# In[82]:


df_cust['e_section'].value_counts()


# In[83]:


df_noncust['e_section'].value_counts()


# In[84]:


df_cust.columns


# In[85]:


import plotly.graph_objects as go


fig = go.Figure(data=[
    go.Bar(name='Potential Customers', x=df_cust['series_dev'].value_counts().index, y=df_cust['series_dev'].value_counts().values),
    go.Bar(name='Non Customers', x=df_noncust['series_dev'].value_counts().index, y=df_noncust['series_dev'].value_counts().values)
])
# Change the bar mode
fig.update_layout(barmode='group', title = "Grouped Barchart to Visualize Device Series Distribution Differences")
fig.show()


# In[86]:


import plotly.graph_objects as go


fig = go.Figure(data=[
    go.Bar(name='Potential Customers', x=df_cust['series_group'].value_counts().index, y=df_cust['series_group'].value_counts().values),
    go.Bar(name='Non Customers', x=df_noncust['series_group'].value_counts().index, y=df_noncust['series_group'].value_counts().values)
])
# Change the bar mode
fig.update_layout(barmode='group', title = "Grouped Barchart to Visualize Device Series Group Distribution Differences")
fig.show()


# In[87]:


import plotly.graph_objects as go


fig = go.Figure(data=[
    go.Bar(name='Potential Customers', x=df_cust['emui_dev'].value_counts().index, y=df_cust['emui_dev'].value_counts().values),
    go.Bar(name='Non Customers', x=df_noncust['emui_dev'].value_counts().index, y=df_noncust['emui_dev'].value_counts().values)
])
# Change the bar mode
fig.update_layout(barmode='group', title = "Grouped Barchart to Visualize Device EMUI Distribution Differences")
fig.show()


# In[88]:


import plotly.graph_objects as go


fig = go.Figure(data=[
    go.Bar(name='Potential Customers', x=df_cust['ads_hour'].value_counts().index, y=df_cust['ads_hour'].value_counts().values),
    go.Bar(name='Non Customers', x=df_noncust['ads_hour'].value_counts().index, y=df_noncust['ads_hour'].value_counts().values)
])
# Change the bar mode
fig.update_layout(barmode='group', title = "Grouped Barchart to Visualize Ad Hour Viewed Distribution Differences")
fig.show()


# In[89]:


import plotly.graph_objects as go


fig = go.Figure(data=[
    go.Bar(name='Potential Customers', x=df_cust['feeds_hour'].value_counts().index, y=df_cust['feeds_hour'].value_counts().values),
    go.Bar(name='Non Customers', x=df_noncust['feeds_hour'].value_counts().index, y=df_noncust['feeds_hour'].value_counts().values)
])
# Change the bar mode
fig.update_layout(barmode='group', title = "Grouped Barchart to Visualize Feed Hour Viewed Distribution Differences")
fig.show()


# In[90]:


import plotly.graph_objects as go


fig = go.Figure(data=[
    go.Bar(name='Potential Customers', x=df_cust['feeds_day'].value_counts().index, y=df_cust['feeds_day'].value_counts().values),
    go.Bar(name='Non Customers', x=df_noncust['feeds_day'].value_counts().index, y=df_noncust['feeds_day'].value_counts().values)
])
# Change the bar mode
fig.update_layout(barmode='group', title = "Grouped Barchart to Visualize Feed Day Viewed Distribution Differences")
fig.show()


# In[91]:


import plotly.graph_objects as go


fig = go.Figure(data=[
    go.Bar(name='Potential Customers', x=df_cust['ads_day'].value_counts().index, y=df_cust['ads_day'].value_counts().values),
    go.Bar(name='Non Customers', x=df_noncust['ads_day'].value_counts().index, y=df_noncust['ads_day'].value_counts().values)
])
# Change the bar mode
fig.update_layout(barmode='group', title = "Grouped Barchart to Visualize Ad Day Viewed Distribution Differences")
fig.show()


# In[94]:


df_cust.columns


# In[95]:


import plotly.express as px
fig = px.pie(df_cust, values= df_cust['i_upTimes'].value_counts().values, names=df_cust['i_upTimes'].value_counts().index, title = "Potential Customer Article Like Distribution")
fig.show()


# In[96]:


import plotly.express as px
fig = px.pie(df_noncust, values= df_noncust['i_upTimes'].value_counts().values, names=df_noncust['i_upTimes'].value_counts().index, title = "Non-Potential Customer Article Like Distribution")
fig.show()


# In[97]:


import plotly.express as px
fig = px.pie(df_cust, values= df_cust['i_dislikeTimes'].value_counts().values, names=df_cust['i_dislikeTimes'].value_counts().index, title = "Potential Customer Article Dislike Distribution")
fig.show()


# In[98]:


import plotly.express as px
fig = px.pie(df_noncust, values= df_noncust['i_dislikeTimes'].value_counts().values, names=df_noncust['i_dislikeTimes'].value_counts().index, title = "Non-Potential Customer Article Dislike Distribution")
fig.show()


# In[99]:


import plotly.express as px
fig = px.pie(df_cust, values= df_cust['pro'].value_counts().values, names=df_cust['pro'].value_counts().index, title = "Potential Customer Article Progress Distribution")
fig.show()


# In[101]:


df_noncust['pro'].value_counts()


# In[100]:


import plotly.express as px
fig = px.pie(df_noncust, values= df_noncust['pro'].value_counts().values, names=df_noncust['pro'].value_counts().index, title = "Non-Potential Customer Article Progress Distribution")
fig.show()


# In[102]:


import plotly.graph_objects as go


fig = go.Figure(data=[
    go.Bar(name='Potential Customers', x=df_cust['i_upTimes'].value_counts().index, y=df_cust['i_upTimes'].value_counts().values),
    go.Bar(name='Non Customers', x=df_noncust['i_upTimes'].value_counts().index, y=df_noncust['i_upTimes'].value_counts().values)
])
# Change the bar mode
fig.update_layout(barmode='group', title = "Grouped Barchart to Visualize Article Liked Distribution Differences")
fig.show()


# In[103]:


import plotly.graph_objects as go


fig = go.Figure(data=[
    go.Bar(name='Potential Customers', x=df_cust['i_dislikeTimes'].value_counts().index, y=df_cust['i_dislikeTimes'].value_counts().values),
    go.Bar(name='Non Customers', x=df_noncust['i_dislikeTimes'].value_counts().index, y=df_noncust['i_dislikeTimes'].value_counts().values)
])
# Change the bar mode
fig.update_layout(barmode='group', title = "Grouped Barchart to Visualize Article Disliked Distribution Differences")
fig.show()


# In[104]:


import plotly.graph_objects as go


fig = go.Figure(data=[
    go.Bar(name='Potential Customers', x=df_cust['pro'].value_counts().index, y=df_cust['pro'].value_counts().values),
    go.Bar(name='Non Customers', x=df_noncust['pro'].value_counts().index, y=df_noncust['pro'].value_counts().values)
])
# Change the bar mode
fig.update_layout(barmode='group', title = "Grouped Barchart to Visualize Article Progress Distribution Differences")
fig.show()


# In[ ]:




