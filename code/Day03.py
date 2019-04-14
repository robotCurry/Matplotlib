import numpy as np
import matplotlib.pyplot as plt

#Histogram is used for the frequency or frequency of statistical data.
#There are many parameters that can be adjusted.

np.random.seed(19680801)

n_bins = 10
x = np.random.randn(1000,3)

fig,axes = plt.subplots(nrows = 2,ncols = 2)
ax0,ax1,ax2,ax3 = axes.flatten()

'''Density controls whether the Y-axis is probability or quantity, corresponding to the first variable returned.
 Histtype controls the style of histogram. 
 The default is `bar'. For multiple bars, it appears adjacent to each other in sub-figure 1, 
 and `barstacked'is stacked together, such as sub-figures 2 and 3. 
 Rwidth controls the width so that some gaps can be cleared. 
 Compare Figures 2 and 3. Figures 4 show that when there is only one data.
'''

colors = ['red','tan','lime']
ax0.hist(x,n_bins,density = True,histtype = "bar",
	color = colors,label = colors)
ax0.legend(prop = {'size':10})
ax0.set_title("bars with legend.")

ax1.hist(x,n_bins,density = True,histtype = "barstacked")
ax1.set_title("stacked bar")

ax2.hist(x,histtype = "barstacked",rwidth = 0.9)

ax3.hist(x[:,0],rwidth = 0.9)
ax3.set_title("different sample sizes.")

fig.tight_layout()
plt.show()
