#!/usr/bin/env python
# coding: utf-8

# In[1]:


# In[1]:


from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


def draw_my_line(normal_vector, point_on_line): # other_point adim 2 de eklendi
    a = normal_vector[0]
    b = normal_vector[1]
    c = normal_vector[2]
    
    x_0 = point_on_line[0]
    y_0 = point_on_line[1]
    z_0 = point_on_line[2]
    
    x = []
    y = []
    z = []
    
   
    
    for t in range(-1,10):
        x.append(x_0+t*a)
        y.append(y_0+t*b) 
        z.append(z_0+t*c) 
  
    return x,y,z
    


# In[3]:


def point_on_line(normal_vector,point_on_line,other_point): #adim 3
    
    a_x = other_point[0] - point_on_line[0]   #otherpoint pointonline ikilisi
    a_y = other_point[1] - point_on_line[1] 
    a_z = other_point[2] - point_on_line[2] 
    
    b = [a_x,a_y,a_z]
    a = normal_vector
    
    c = my_scalar_product(a,b) / my_scalar_product(a,a)
    
    b_x = c*a[0]
    b_y = c*a[1]
    b_z = c*a[2]
    
    nearest_point_on_line = [b_x,b_y,b_z]
    
    return nearest_point_on_line


# In[4]:


def my_scalar_product(a, b ):
    #a = [-1,-2,4]
    #b = [-2,-5,2]
    #a transpoz b 
    a_t_b= a[0]*b[0]+a[1]*b[1]+ a[2]*b[2]
    return a_t_b


# In[5]:


p = (0,0,0)                           #hattı tanımlayan iki pakametre
n = (1,1,1)
other_point = (1,2,7)                 #bekleme kontrası
points = draw_my_line(n,p)
n_p = point_on_line(n,p,other_point)  #hat üzerindeki bize en yaıkın nokta


# In[6]:


get_ipython().run_line_magic('matplotlib', 'notebook')
ax = plt.axes(projection='3d')
ax.plot3D(points[0],points[1],points[2],'red')
ax.scatter(n_p[0],n_p[1],n_p[2],'*')
ax.scatter(other_point[0],other_point[0],other_point[0],'*')
plt.show()


# In[ ]:



# In[2]:


from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


def draw_my_line(normal_vector, point_on_line): # other_point adim 2 de eklendi
    a = normal_vector[0]
    b = normal_vector[1]
    c = normal_vector[2]
    
    x_0 = point_on_line[0]
    y_0 = point_on_line[1]
    z_0 = point_on_line[2]
    
    x = []
    y = []
    z = []
    
   
    
    for t in range(-1,10):
        x.append(x_0+t*a)
        y.append(y_0+t*b) 
        z.append(z_0+t*c) 
  
    return x,y,z


# In[4]:


def point_on_line(normal_vector,point_on_line,other_point): #adim 3
    
    a_x = other_point[0] - point_on_line[0]   #otherpoint pointonline ikilisi
    a_y = other_point[1] - point_on_line[1] 
    a_z = other_point[2] - point_on_line[2] 
    
    b = [a_x,a_y,a_z]
    a = normal_vector
    
    c = my_scalar_product(a,b) / my_scalar_product(a,a)
    
    b_x = c*a[0]
    b_y = c*a[1]
    b_z = c*a[2]
    
    nearest_point_on_line = [b_x,b_y,b_z]
    
    return nearest_point_on_line


# In[5]:


def my_scalar_product(a, b ):
    #a = [-1,-2,4]
    #b = [-2,-5,2]
    #a transpoz b 
    a_t_b= a[0]*b[0]+a[1]*b[1]+ a[2]*b[2]
    return a_t_b


# In[6]:


p = (0,0,0)                           #hattı tanımlayan iki pakametre
n = (1,1,1)
other_point = (1,2,7)                 #bekleme kontrası
points = draw_my_line(n,p)
n_p = point_on_line(n,p,other_point)  #hat üzerindeki bize en yaıkın nokta


# In[13]:


get_ipython().run_line_magic('matplotlib', 'notebook')
ax = plt.axes(projection='3d')
ax.plot3D(points[0],points[1],points[2],'red')
ax.scatter(n_p[0],n_p[1],n_p[2],'*')
ax.scatter(other_point[0],other_point[0],other_point[0],'*')
plt.show()


# In[14]:


points=draw_my_line(n,p)
ax=plt.axes(projection='3d')
ax.plot3D(points[0], points[1], points[2], 'red')
ax.scatter(other_point[0], other_point[1], other_point[2], '*')
ax.scatter(n_p[0], n_p[1], n_p[2], '*')
plt.show()


# In[ ]:




