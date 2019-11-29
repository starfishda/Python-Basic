#!/usr/bin/env python
# coding: utf-8

# In[5]:


a, b, v = map(int, input().split())

day = (v-b) / (a-b)

if day > int(day):
    print(int(day) + 1)
else:
    print(int(day))

'''
time out code
sum = a
day = 1

while(sum < v):
    day += 1
    sum = sum - b + a
    
print(day)
'''


# In[ ]:




