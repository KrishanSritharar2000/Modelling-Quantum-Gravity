import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import *
import math

#These are the results for 500 walks
####stepNum = [10,20,30,40,50,60,70,80,90,100]
####meanDistance = [3.27242,3.70334,4.05579,5.96872,6.65222,7.12515,6.20092,8.22213,9.94033,10.13806]
####standardDev = [1.359895808,1.735877107,1.915848634,2.578057187,3.316289883,4.238415552,3.389789607,4.156239907,5.477409234,3.961011767]

#These are the results for 1000 walks
####stepNum = [10,20,30,40,50,60,70,80,90,100]
####meanDistance = [0.80302,0.94107,1.31155,1.67848,1.24387,1.58073,2.03179,2.20642,2.32223,2.40536]
####standardDev = [0.293313869,0.501749428,0.534525115,0.804550324,0.78840761,0.605084783,0.915285406,0.913287142,0.938088804,1.075322424]

#These are the results for 10000 walks
stepNum = [10,20,30,40,50,60,70,80,90,100]
meanDistance = [0.32254,0.28542,0.62648,0.67557,0.59155,0.62207,0.89099,0.68,0.79872,0.77736]
standardDev = [0.19044372,0.115930391,0.207755504,0.292243662,0.231435357,0.355796906,0.422583015,0.295360671,0.377449188,0.441284711]




def meanDistAgainstStepNum(x,y):
    
    plt.scatter(x,y,color='k', marker = 'x', s =25)#this draws the scatter diagram
    plt.plot(x, np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color='k')#this draws the straight line of best fit

    #p1 = np.polyfit(x,y,1)                     These lines also plot the line of best fit
    #plt.plot(x,np.polyval(p1,x), color='k')


    plt.xlabel('Step Number')#labels the axes
    plt.ylabel('Mean Distance')

    plt.title('Mean Distance against Step Number')#title for the graph
    
    plt.show()

def standardDevAgainstStepNum(x,y):
    
    plt.scatter(x,y,color='k', marker = 'x', s =25)#this draws the scatter diagram

    p1 = np.polyfit(x,y,2)#these 3 lines draw the smooth curve
    xp = np.linspace(0,100,100)#this makes the curve smooth
    plt.plot(xp,np.polyval(p1,xp), color='k')

    plt.xlabel('Step Number')#labels the axes
    plt.ylabel('Standard Deviation')

    plt.title('Standard Deviation against Step Number')#title for the graph

    plt.show()

def logStandardDevAgainstLogStepNum(x,y):

    logStepNum = []
    logStandardDev = []

    for i in range(len(x)):
        logStepNum.append(round(math.log(x[i],10),8))
        logStandardDev.append(round(math.log(y[i],10),8))


    plt.scatter(logStepNum,logStandardDev,color='k', marker = 'x', s =25)#this draws the scatter diagram

    p1 = np.polyfit(logStepNum,logStandardDev,1)#this draws the line of best fit
    plt.plot(logStepNum,np.polyval(p1,logStepNum), color='k')

    gradient, intercept = np.polyfit(logStepNum, logStandardDev, 1)#this finds the gradient and intercept of the line

##    print("Gradient: ", round(gradient,4))
##    print("Intercept: ", round(intercept,4))

    p = round(gradient, 4)
    b = round(10 ** math.log(abs(intercept),10),4)#calculates the realtionship

    print("The relationship between the Standard Deviation(o) and Step Number (N) is: ")
    print(" \n  o(d) = " + str(b) + " N^" + str(p))
          

    plt.xlabel('log(Step Number)')#labels the axes
    plt.ylabel('log(Standard Deviation)')

    plt.figtext(0.85, 0.025," \n  o(d) = " + str(b) + " N^" + str(p), wrap=True,
            horizontalalignment='center', fontsize=10)

    plt.title('log(Standard Deviation) against log(Step Number)')#title for the graph

    plt.show()




##meanDistAgainstStepNum(stepNum,meanDistance)
##standardDevAgainstStepNum(stepNum,standardDev)
logStandardDevAgainstLogStepNum(stepNum,standardDev)
