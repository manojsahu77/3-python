#!/usr/bin/env python
# coding: utf-8

# In[7]:


even=[]
for i in range(20):
        if i%2==0:
            even.append(i)
print(even)        


# In[8]:


num=range(20)
list(filter(lambda x:x%2==0,num))

