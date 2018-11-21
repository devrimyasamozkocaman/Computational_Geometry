#!/usr/bin/env python
# coding: utf-8

# In[2]:


from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[21]:


# x = 6t y = 3t^2 z = t olan eğrinin t = 10 daki teğetini çizdiriniz.
# Plot a helix along the x-axis
get_ipython().run_line_magic('matplotlib', 'notebook')
n = 1000
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot a helix along the x-axis
theta_max = 8 * np.pi
theta = np.linspace(0, theta_max, n)
x = 6*theta
y = 3*(theta**2)
z = theta
ax.plot(x,y,z,'b',lw=2)

theta_current = 10
x_1 = 6 # math.cos(theta_current)
y_1 = 6*theta_current #math.sin(theta_current)
z_1 = 1

x_2 = 0
y_2 = 6
z_2 = 0

x_3 = x_1+x_2
y_3 = y_1+y_2
z_3 = z_1+z_2


x_s = [x_3, x_2]
y_s = [y_3, y_2]
z_s = [z_3, z_2]

ax.plot(x_s,y_s,z_s)
plt.show()


# In[ ]:




