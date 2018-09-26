import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import *
import math

#These are the results for 500 walks
stepNum500 = [10,20,30,40,50,60,70,80,90,100]
meanDistance500 = [3.27242,3.70334,4.05579,5.96872,6.65222,7.12515,6.20092,8.22213,9.94033,10.13806]
standardDev500 = [1.359895808,1.735877107,1.915848634,2.578057187,3.316289883,4.238415552,3.389789607,4.156239907,5.477409234,3.961011767]

#These are the results for 1000 walks
stepNum1000 = [10,20,30,40,50,60,70,80,90,100]
meanDistance1000 = [0.80302,0.94107,1.31155,1.67848,1.24387,1.58073,2.03179,2.20642,2.32223,2.40536]
standardDev1000 = [0.293313869,0.501749428,0.534525115,0.804550324,0.78840761,0.605084783,0.915285406,0.913287142,0.938088804,1.075322424]

#These are the results for 10000 walks
stepNum10000 = [10,20,30,40,50,60,70,80,90,100]
meanDistance10000 = [0.32254,0.28542,0.62648,0.67557,0.59155,0.62207,0.89099,0.68,0.79872,0.77736]
standardDev10000 = [0.19044372,0.115930391,0.207755504,0.292243662,0.231435357,0.355796906,0.422583015,0.295360671,0.377449188,0.441284711]




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

def logStandardDevAgainstLogStepNum(x1,y1,x2,y2,x3,y3):

    logStepNum1 = []
    logStepNum2 = []
    logStepNum3 = []
    logStandardDev1 = []
    logStandardDev2 = []
    logStandardDev3 = []

    for i in range(len(x1)):
        logStepNum1.append(round(math.log(x1[i],10),8))
        logStandardDev1.append(round(math.log(y1[i],10),8))

    for j in range(len(x2)):
        logStepNum2.append(round(math.log(x2[j],10),8))
        logStandardDev2.append(round(math.log(y2[j],10),8))
        
    for k in range(len(x3)):
        logStepNum3.append(round(math.log(x3[k],10),8))
        logStandardDev3.append(round(math.log(y3[k],10),8))

    plt.scatter(logStepNum1,logStandardDev1, color='k', marker = 'x', s =25, label='500 Steps')#this draws the scatter diagram
    plt.scatter(logStepNum2,logStandardDev2, color='blue', marker = 'o', s =20, label='1000 Steps')#this draws the scatter diagram
    plt.scatter(logStepNum3,logStandardDev3, color='red', marker = '+', s =30, label='10000 Steps')#this draws the scatter diagram

    plt.legend()
    
    p1 = np.polyfit(logStepNum1,logStandardDev1,1)#this draws the line of best fit
    plt.plot(logStepNum1,np.polyval(p1,logStepNum1), color='k')

    p2 = np.polyfit(logStepNum2,logStandardDev2,1)#this draws the line of best fit
    plt.plot(logStepNum2,np.polyval(p2,logStepNum2), color='blue')

    p3 = np.polyfit(logStepNum3,logStandardDev3,1)#this draws the line of best fit
    plt.plot(logStepNum3,np.polyval(p3,logStepNum3), color='red')

    gradient1, intercept1 = np.polyfit(logStepNum1, logStandardDev1, 1)#this finds the gradient and intercept of the line
    gradient2, intercept2 = np.polyfit(logStepNum2, logStandardDev2, 1)#this finds the gradient and intercept of the line
    gradient3, intercept3 = np.polyfit(logStepNum3, logStandardDev3, 1)#this finds the gradient and intercept of the line

##    print("Gradient: ", round(gradient,4))
##    print("Intercept: ", round(intercept,4))

    p1 = round(gradient1, 4)
    b1 = round(10 ** math.log(abs(intercept1),10),4)#calculates the realtionship
    
    p2 = round(gradient2, 4)
    b2 = round(10 ** math.log(abs(intercept2),10),4)#calculates the realtionship

    p3 = round(gradient3, 4)
    b3 = round(10 ** math.log(abs(intercept3),10),4)#calculates the realtionship

    
    print("The relationship between the Standard Deviation(o) and Step Number (N) for 500 steps is: ")
    print(" \n  o(d) = " + str(b1) + " N^" + str(p1))
    print("\n")

    print("The relationship between the Standard Deviation(o) and Step Number (N) for 1000 steps is: ")
    print(" \n  o(d) = " + str(b2) + " N^" + str(p2))
    print("\n")
    
    print("The relationship between the Standard Deviation(o) and Step Number (N) for 10000 steps is: ")
    print(" \n  o(d) = " + str(b3) + " N^" + str(p3))
    print("\n")

    plt.xlabel('log(Step Number)')#labels the axes
    plt.ylabel('log(Standard Deviation)')

##    plt.figtext(0.85, 0.025," \n  o(d) = " + str(b) + " N^" + str(p), wrap=True,
##            horizontalalignment='center', fontsize=10)

    plt.title('log(Standard Deviation) against log(Step Number)')#title for the graph

    plt.show()




##meanDistAgainstStepNum(stepNum,meanDistance)
##standardDevAgainstStepNum(stepNum,standardDev)
logStandardDevAgainstLogStepNum(stepNum500,standardDev500,stepNum1000,standardDev1000,stepNum10000,standardDev10000)
