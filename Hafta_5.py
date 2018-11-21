#!/usr/bin/env python
# coding: utf-8

# In[2]:


from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[15]:


def my_product(a, b):
    return a[0]*b[0] +  a[1]*b[1] + a[2]*b[2] 


# In[16]:


def my_length_function(a):
    return my_product(a,a)**.5


# In[17]:


def plane_point(plane,point):
#draw plane
#draw two point
    FQ_line_segment_v=[point[0], point[1], point[2]+plane[3]/plane[2]]
    plane_normal=[plane[0],plane[1], plane[2]]
    d=my_product(plane_normal, FQ_line_segment_v) / my_length_function(plane_normal)
    t=-plane[3]-(my_product(plane_normal,point))
    t=t/my_product(plane_normal,plane_normal)
    p_0=[0,0,0]
    p_0[0]=point[0]+ t* plane[0]
    p_0[1]=point[1]+ t* plane[1]
    p_0[2]=point[2]+ t* plane[2]
    return d,t,p_0


# In[18]:


def plot_plane_line_point(plane, line_with_twopoints, twopoints):
    plane_normal=[plane[0],plane[1], plane[2]]
    d=plane[3]
    xx,yy=np.meshgrid(range(-10,20), range(-10,20))
    z1=(-plane_normal[0]*xx-plane_normal[1]*yy-d)*1./plane_normal[2]
    
    plt3d=plt.figure().gca(projection='3d')
    plt3d.plot_surface(xx,yy,z1)
    point_1=line_with_twopoints[0]
    point_2=line_with_twopoints[1]
    points_x=[point_1[0], point_2[0]]
    points_y=[point_1[1], point_2[1]]
    points_z=[point_1[2], point_2[2]]
    plt3d.plot3D(points_x, points_y, points_z, 'red')
    plt.show()
  
          
    point_1=twopoints[0]
    point_2=twopoints[1]
    points_x=[point_1[0], point_2[0]]
    points_y=[point_1[1], point_2[1]]
    points_z=[point_1[2], point_2[2]]
    plt3d.plot3D(points_x, points_y, points_z, 'red')
    plt.show()
    


# In[19]:


def test():
    plane_1=[3,2,6,-6]
    point_1=[1,1,3]
    (d,t,p)=plane_point(plane_1,point_1)
    plot_plane_line_point(plane_1,[point_1, p], [point_1, p])
    print(d,t,p)


# In[20]:


test()


# In[ ]:




