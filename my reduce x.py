#!/usr/bin/env python
# coding: utf-8

# In[9]:


def my_reduce(items):
    my_reduce=0
    for x in items:
        my_reduce +=x
    return my_reduce
print(my_reduce([11,22,33,-44]))


# In[11]:


from functools import reduce
sum=[11,22,33,-44]
reduce(lambda x,y:x+y,sum)


# In[ ]:




