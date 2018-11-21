#!/usr/bin/env python
# coding: utf-8

# In[32]:


from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[33]:


from mpl_toolkits.mplot3d import Axes3D
sint,cost=1,1
t=10

def draw_my_curve():
    n=1000
    theta_max=8*np.pi
    theta=np.linspace(0,theta_max,n)
    z=theta
    x=np.sin(theta)
    y=np.cos(theta)

    theta_current=3*np.pi/2
    x_1=np.cos(theta_current)
    y_1=np.sin(theta_current)
    z_1=1

    x_2=np.sin(theta_current)
    y_2=np.cos(theta_current)
    z_2=theta_current

    x_3 = x_1+x_2
    y_3 = y_1+y_2
    z_3 = z_1+z_2

    x_s=[x_3,x_2]
    y_s=[y_3,y_2]
    z_s=[z_3,z_2]
    ax = plt.axes(projection="3d")

    ax.plot(x, y, z, 'g', lw=2)
    ax.plot(x_s,y_s,z_s,'b',lw=2)
    plt.show()
draw_my_curve()


# In[ ]:




