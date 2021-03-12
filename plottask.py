#Filename:  plottask.py
#Author:    Mark Parry
#Created:   12/03/2021
#Purpose:   Displays a plot of the functions f(x)=x, g(x)=x**2 and h(x)=x**3 in the range [0, 4] on the one set of axes.

#Assumptions: I am assuming that the plot should display the numbers one to four as range[0,4] will only go up to three, hence my array range is [0,5]

#import the matplotlib module
import matplotlib.pyplot as mpl

#import numpy module to set up array for the range
import numpy as np

#Plot f(x)=x
xvalues = np.array(range(0,5))
yvalues = xvalues
mpl.plot(xvalues,yvalues,color="r", label="x = y")


#Plot g(x)=x**2
yvalues = xvalues * xvalues
mpl.plot(xvalues,yvalues,color="g", label="x squared")

#Plot h(x)=x**3
yvalues = xvalues * xvalues * xvalues
mpl.plot(xvalues,yvalues,color="b", label="x cubed")

#Give the plots a title,change the numbering on the x axis,label both axes, display the legend to note which plot is which(rgb)
mpl.title("3 Functions of x") 
mpl.xticks([0,1,2,3,4])
mpl.xlabel("x Axis") 
mpl.ylabel("y Axis") 
mpl.legend() 

#Display the three functions on the plot
mpl.show()



