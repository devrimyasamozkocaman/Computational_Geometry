#!/usr/bin/env python
# coding: utf-8

# In[2]:


from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig=plt.figure()
ax=Axes3D(fig)
X=np.arange(-10,10,0.5)
Y=np.arange(-10,10,0.5)
X,Y=np.meshgrid(X,Y)
#R=np.sqrt(X2+Y2)
R=(X2+Y2)
Z=np.sin(R)

X_plane=np.arange(-2,7,25)
Y_plane=np.arange(-3,7,0.5)
X_plane, Y_plane=np.meshgrid(X_plane, Y_plane)
Z_plane=5-2X_plane+4Y_plane

ax.plot_surface(X,Y,R, rstride=1, cstride=1, cmap='hot')
ax.plot_surface(X_plane,Y_plane,Z_plane, rstride=1, cstride=1, cmap='hot')
plt.show()


# In[ ]:




