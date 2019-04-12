import matplotlib.pyplot as plt
import numpy as np
 
#Figure：Before drawing, we need a Figire object, 
#which can be understood as we need a drawing board to start drawing.
#Axes:After having Figure objects, we need axes before drawing. Without axes, there is no drawing benchmark,
#so we need to add Axes. 
#It can also be understood as a paper that can really be painted.

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(224)

'''>>> import numpy as np
>>> np.linspace(0,np.pi)
array([0.        , 0.06411414, 0.12822827, 0.19234241, 0.25645654,
       0.32057068, 0.38468481, 0.44879895, 0.51291309, 0.57702722,
       0.64114136, 0.70525549, 0.76936963, 0.83348377, 0.8975979 ,
       0.96171204, 1.02582617, 1.08994031, 1.15405444, 1.21816858,
       1.28228272, 1.34639685, 1.41051099, 1.47462512, 1.53873926,
       1.60285339, 1.66696753, 1.73108167, 1.7951958 , 1.85930994,
       1.92342407, 1.98753821, 2.05165235, 2.11576648, 2.17988062,
       2.24399475, 2.30810889, 2.37222302, 2.43633716, 2.5004513 ,
       2.56456543, 2.62867957, 2.6927937 , 2.75690784, 2.82102197,
       2.88513611, 2.94925025, 3.01336438, 3.07747852, 3.14159265])
>>> np.pi
3.141592653589793'''
x = np.linspace(0,np.pi)
Y_sin = np.sin(x)
Y_cos = np.cos(x)

#The plot () function draws a series of points and connects them with line segments.
ax1.plot(x,Y_sin)
ax2.plot(x,Y_cos,"go--",linewidth = 2,markersize = 12)
ax3.plot(x,Y_cos,color = "red",marker = "+")


plt.show()
