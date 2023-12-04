#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install matplotlib


# In[2]:


import matplotlib.pyplot as plt


# In[3]:


import numpy as np


# In[4]:


x=np.array([2,23,56])
y=np.array([5,56,78])


# In[5]:


x


# In[6]:


y


# In[7]:


plt.plot(x,y)
plt.show()


# In[8]:


plt.plot(x,y,'o')
plt.show()


# In[10]:


plt.plot(x,marker='*')
plt.show()


# In[11]:


plt.plot(x,'o:y')
plt.show()


# In[12]:


plt.plot(x,'o:b',ms=13,mec="blue")
plt.show()


# In[13]:


plt.plot(x,'o:b',ms=15,mec="black",mfc="y")
plt.show()


# In[14]:


plt.plot(x,y,'o:b',ms=15,mec="black",linestyle="dashed")
plt.show()


# In[15]:


plt.plot(x,'o:b',ms=15,mec="black",linewidth="4.5")
plt.show()


# In[16]:


plt.plot(x)
plt.plot(y)

plt.show()


# In[17]:


plt.plot(x,y)

plt.xlabel("marks")
plt.ylabel("rollno")
plt.title("Demo Data",loc="left")

plt.show()


# In[18]:


plt.plot(x,y)

plt.xlabel("marks")
plt.ylabel("rollno")
plt.title("Demo Data",loc="left")

plt.grid()
plt.show()


# In[ ]:




