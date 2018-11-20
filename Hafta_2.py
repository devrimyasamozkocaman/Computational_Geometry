#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


x=[4,0]
y=[0,3]
plt.plot(x,y)                   #verilen iki noktadan geçen doğruyu çizer


# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')
x=[0,4,10]
y=[0,3,3]
plt.xlim=(-10,25)
plt.ylim=(-20,25)
plt.plot(x,y)


# In[7]:


def my_draw_a_vector_from_origin(v):            #orijinden başlayan ve verilen noktadan geçen vektörü çizdiren fonksiyon
    
    plt.axes().set_aspect('equal')
    x=[0,v[0]]
    y=[0,v[1]]
    plt.xlim=(-10,15)
    plt.ylim=(-10,15)
    plt.plot(x,y)
my_draw_a_vector_from_origin([5,13])


# In[8]:


def my_draw_a_vector_from_v_to_w(v,w):   #parametre olarak verilen iki noktanın birinden diğerine giden vektörü çizen fonksiyon 
    
    plt.axes().set_aspect('equal')
    x=[v[0],w[0]]
    y=[v[1],w[1]]
    plt.xlim=(-10,15)
    plt.ylim=(-10,15)
    plt.plot(x,y)
my_draw_a_vector_from_v_to_w([5,6],[20,16])


# In[10]:


def my_scalar_product(a,b):
    
    return (a[0]*b[0]+a[1]*b[1])
v=[3,4]
w=[4,7]
my_scalar_product(v,w)


# In[11]:


def distance(v,w):
    return [(((v[0]-w[0])**2)+((v[1]-w[1])**2))**.5]
def my_vector_add(v,w):
    return [v[0]+w[0],v[1]+w[1]]
def my_vector_sub(v,w):
    return [v[0]-w[0],v[1]-w[1]]
def my_vector_mult_with_scalar(c,v):
    return [c*v[0],c*v[1]]


# In[12]:


a=[3,0]
b=[0,4]
print("Vekrötlerin toplamı: ", my_vector_add(a,b))
print("Vektörlerin farkı: ", my_vector_sub(a,b))
print("Vektörün skaler sayıyla çarpımı: ", my_vector_mult_with_scalar(5,b))
print("Vektörler arası mesafe: ", distance(a,b))


# In[ ]:




