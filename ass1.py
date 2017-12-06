from numpy import *
import random

class ass1():
    def testProb(xList,wList,theta,alpha,RAND_MAX = 2**32-1):
        xList.insert(0,1)
        wList.insert(0,-theta)
        xArray = array(xList)
        wArray = array(wList)
        S = sum(xArray*wArray)
        p = 1/(1+exp(-S*alpha))
        Count0 = 0
        Count1 = 0
        for i in range(1000):
            a = random.uniform(0,RAND_MAX)
            if a>RAND_MAX*p:
                Count0+=1
            else:
                Count1+=1
        print "alpha is equal to: %d"%(alpha)
        print "Ideal classification: 1: %d   0: %d"%(int(1000*p),1000-int(1000*p))
        print "The number of classificatin result as 1: %d"%Count1
        print "The number of classificatin result as 0: %d"%Count0

    if __name__ == "__main__":
 #       xList = input('Please type in xList in the form of list of 0 or 1\n')
 #       wList = input('Please type in wList in the form of list of float\n')
 #       theta = input('Please type in the vale of theta to initialize w0\n')
        testProb([1.0,1.0,-1.0,-1.0],[3.0,-4.0,2.0,-4.0],3,1)
        testProb([1.0,1.0,-1.0,-1.0],[3.0,-4.0,2.0,-4.0],3,2)
        testProb([1.0,1.0,-1.0,-1.0],[3.0,-4.0,2.0,-4.0],3,3) 
        testProb([1.0,1.0,-1.0,-1.0],[3.0,-4.0,2.0,-4.0],3,4) 
