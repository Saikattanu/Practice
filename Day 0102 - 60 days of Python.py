#!/usr/bin/env python
# coding: utf-8

# In[5]:


'data science' #shift+inter


# In[11]:


print('Hello world' , 'Welcome to 60 days of Python', sep= ' & ', end=" * ") #shift+tab


# In[12]:


var = 'Hello World'
print(var)


# In[17]:


var = 'Hello World'
print(var)

print('My Sentence is ' + var)


# In[18]:


id(var)


# In[19]:


import sys
sys.getsizeof(var)


# In[20]:


x = 100


# In[21]:


x


# In[22]:


y = 100


# In[23]:


y


# In[24]:


id(x)


# In[25]:


id(y)


# In[26]:


x = 1000
y = 1000
id(x)


# In[27]:


id(y)


# In[29]:


name = 'Saikat'
x = 'Saikat'
x


# In[30]:


saikat = 100


# In[31]:


var-2 = 100


# In[32]:


10-2


# In[33]:


var_2 =100
var_2


# In[34]:


x,y,z = 10,100,1000


# In[35]:


z


# In[36]:


y


# In[37]:


x


# In[40]:


x,y,z = 10,100,0


# In[41]:


x,y,z = 10,100,'Saikat'


# In[42]:


z


# In[43]:


X = 1
x = 2


# In[44]:


x


# In[45]:


X


# In[49]:


VARSITYID = 20231092
varsity_id = 20231092 #snakecase


# In[50]:


VARSITYID


# In[52]:


varsity_id


# # local vs global

# In[56]:


x = 1000

def func1():
    x = 500 #local
    print('My num is : ',x)
    
func1()


# In[63]:


x = 1000 #global

def func1():
    x = 500 #local
    print('My num is : ',x)
func1()
print('My num is : ',x)


# In[64]:


def func1():
    global x
    x = 500 #local
    print('My num is : ',x)
func1()
print('My num is : ',x)


# In[ ]:




