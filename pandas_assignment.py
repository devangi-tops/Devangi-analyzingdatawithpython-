#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas


# In[2]:


import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)


# In[3]:


import pandas as pd

print(pd.__version__)


# In[4]:


import pandas as pd


# In[5]:


a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)


# # lables

# In[6]:


import pandas as pd


# In[7]:


a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)


# In[8]:


calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)


# In[9]:


calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)


# # dataframe

# In[10]:


import pandas as pd


# In[11]:


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)


# In[13]:


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)

print(df)


# In[14]:


print(df.loc[0])


# In[15]:


print(df.loc[[0, 1]])


# In[16]:


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 


# In[17]:


print(df.loc["day2"])


# # json

# In[19]:


import pandas as pd


# In[20]:


data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df) 


# In[21]:


import numpy as np
import pandas as pd


# In[22]:


dict1 = {
    "name":['harry','subh','skiff','rohan'],
    "marks":[92,34,45,60],
    "city":['rampur','kolkata','america','lilapur']
}


# In[23]:


df = pd.dataframe(dict1)


# In[24]:


df


# In[25]:


df.to_csv('friends.csv')


# In[26]:


df.head(2)


# In[27]:


df.tail(4)


# In[28]:


df.describe()


# In[8]:


pip install pandas


# In[9]:


import pandas as pd


# In[10]:


d = pd.series([1,2,3,5])
print(d.to_string(index=false))
print()
print("Type Check : ",type(d))
print()
print("Indexing : ",d[0])


# In[ ]:




