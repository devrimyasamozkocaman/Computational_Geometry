#!/usr/bin/env python
# coding: utf-8

# In[34]:


from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[35]:


#plot the elips
a=5 
b=3
x=np.linspace(-5.0, 5.0, num=1000)
ax = plt.axes(projection='3d')
y=((1-(x**2)/(a**2))*(b**2))**.5
plt.plot(x,y)
plt.plot(x,-y)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




