import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,200)
data_obj = {"x":x,"y1":2*x +1,"y2":3*x+1.2,"mean":0.5*x*np.cos(2*x)+2.5*x+1.1}

fig,ax = plt.subplots()

ax.fill_between("x","y1","y2",color = "yellow",data = data_obj)

plt.plot("x","mean",color = "black",data = data_obj)  
plt.show()
