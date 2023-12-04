#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
a=[1,2,3]
a


# In[4]:


a=[[1,2,3],[4,5,6],[7,8,9]]
arr=np.array(a)
arr


# In[5]:


a=[[1,2,3],[4,5,6],[7,8,9]]
arr=np.array(a)
print("Dimesion of array=",arr.ndim)


# In[6]:


a=[[1,2,3],[4,5,6],[7,8,9]]
arr=np.array(a)
print("shape of array=",arr.shape)


# In[7]:


arr=np.zeros(4)
arr


# In[8]:


arr=np.ones(4)
arr


# In[9]:


arr=np.ones((2,4))
arr


# In[10]:


arr=np.eye(3,4)
arr


# In[11]:


arr=np.diag[(2,3,4,5)]
arr


# In[12]:


arr=np.diag([2,3,4,5])
arr


# In[13]:


arr=np.random.randint(1,10,3)
arr


# In[14]:


arr=np.random.rand(5)
arr


# In[15]:


R=np.array([1,2,3,4,5] ,ndmin=5)
R

print(R)
print()
print("Array value type",R.dtype)
print()
print("type of Dimention:",type(R))
print()
print("type of Array : ", R.ndim)


# In[16]:


R=np.array([1,2,3,4,5])

print("Indexing : ",R[1])


# In[17]:


R=np.array([1,2,3,4,5])
print("addition of array : ",R[1]+R[2])


# ### 3D Indexing

# In[18]:


import numpy as np

s=np.array([[[1,23,43],[1,45,64]],[[2,65,88],[1,56,76]]])
print(s)
print()
print("Number of Dimention : ",s.ndim)
print()
print("Type of dimention : ",type(s))
print()
print("type of value : ",s.dtype)
print()
print("Indexing in 3D array : ",s[0,1,1])
print()
print("Reshape Array : ")
print(s.reshape(12,1))
print()
print("Array slicing : ")
print()
print(s[1:3])


# # array iterating

# In[19]:


import numpy as np

arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

for x in np.nditer(arr):
    print(x)


# In[21]:


import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])

for x in np.nditer(arr[:, ::2]):
    print(x)


# # array join

# In[22]:


import numpy as np


# In[23]:


arr1 = np.array([1,2,3])

arr2 = np.array([4,5,6])

arr = np.concatenate((arr1,arr2))

print(arr)


# In[26]:


arr1 = np.array([[1,2],[3,4]])

arr2 = np.array([[5,6],[7,8]])

arr = np.concatenate((arr1,arr2), axis=1)

print(arr)


# In[27]:


arr1 = np.array([1,2,3])

arr2 = np.array([4,5,6])

arr = np.vstack((arr1,arr2))

print(arr)


# # array split

# In[28]:


import numpy as np


# In[29]:


arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)


# In[30]:


arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)


# In[31]:


arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])


# In[32]:


arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)


# In[33]:


import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)


# # array sort

# In[34]:


import numpy as np


# In[35]:


arr = np.array([3, 2, 0, 1])

print(np.sort(arr))


# In[36]:


arr = np.array(['banana', 'cherry', 'mango'])

print(np.sort(arr))


# In[37]:


arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))


# # array filter

# In[38]:


import numpy as np


# In[39]:


arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)


# In[40]:


arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)


# In[41]:


arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)


# In[42]:


arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)


# In[ ]:




