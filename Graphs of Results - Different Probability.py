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
##stepNum = [10,20,30,40,50,60,70,80,90,100]
##meanDistance = [0.32254,0.28542,0.62648,0.67557,0.59155,0.62207,0.89099,0.68,0.79872,0.77736]
##standardDev = [0.19044372,0.115930391,0.207755504,0.292243662,0.231435357,0.355796906,0.422583015,0.295360671,0.377449188,0.441284711]

#These are the results for PRight = 0.3 
stepNum1 = [10,20,30,40,50,60,70,80,90,100]
meanDistance1 = [30.04152,60.30389,89.94863,120.30013,149.8984,179.6632,210.13894,239.53046,270.28543,299.87383]
standardDev1 = [0.488812706,0.452722238,0.763935202,0.865366648,0.861351652,1.301069594,1.009998869,1.356940435,1.661526094,2.231319993]


#These are the results for PRight = 0.35
stepNum2 = [10,20,30,40,50,60,70,80,90,100]
meanDistance2 = [50.04171,100.36773,149.88033,199.20989,250.07518,300.68533,350.07157,399.70036,450.52475,500.40309]
standardDev2 = [0.476317907,0.724348725,0.995120702,0.915476919,1.212386046,0.742664899,1.464850436,1.590046546,0.916698102,1.797228882]


#These are the results for PRight = 0.7 
stepNum3 = [10,20,30,40,50,60,70,80,90,100]
meanDistance3 = [70.05286,140.05187,210.17237,280.51841,350.18707,419.75834,490.06407,549.58605,629.92302,699.38162]
standardDev3 = [0.390571551,0.707467662,1.023746584,0.861370935,0.959995452,0.894251051,1.859214012,29.59369708,1.750576022,1.12120581]


def meanDistAgainstStepNum(x1,y1,x2,y2,x3,y3):
    
    plt.scatter(x1,y1,color='k', marker = 'x', s =25)#this draws the scatter diagram
    plt.plot(x1, np.poly1d(np.polyfit(x1, y1, 1))(np.unique(x1)), color='k', label='0.3')#this draws the straight line of best fit

    plt.scatter(x2,y2,color='blue', marker = 'o', s =20)#this draws the scatter diagram
    plt.plot(x2, np.poly1d(np.polyfit(x2, y2, 1))(np.unique(x2)), color='blue', label='0.5')#this draws the straight line of best fit

    plt.scatter(x3,y3,color='red', marker = '+', s =30)#this draws the scatter diagram
    plt.plot(x3, np.poly1d(np.polyfit(x3, y3, 1))(np.unique(x3)), color='red', label='0.7')#this draws the straight line of best fit

    #p1 = np.polyfit(x,y,1)                     These lines also plot the line of best fit
    #plt.plot(x,np.polyval(p1,x), color='k')

    plt.legend()


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

meanDistAgainstStepNum(stepNum1,meanDistance1,stepNum2,meanDistance2,stepNum3,meanDistance3)

##meanDistAgainstStepNum(stepNum,meanDistance)
####standardDevAgainstStepNum(stepNum,standardDev)
##logStandardDevAgainstLogStepNum(stepNum,standardDev)
