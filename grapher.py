import matplotlib.pyplot as plt
import math
import numpy as np

#
g = 9.81
B = 5*(10**-5)

#declaring data
x1 = [0.6,1.2,1.8,2.4,3,3.6]
y1 = [0.0001,0.00022,0.00034,0.00043,0.00056,0.00064]

x2 = [0.4,0.8,1.2,1.6,2,2.4]
y2 = [0.00008,0.00019,0.00028,0.00039,0.00047,0.00058]

x3 = [1,2,3,4,5,5.88]
y3 = [3.441,4.615,6.575,7.5,8.496,9.057]

#calculation of centroid

def centroid(data):
    centroid = sum(data)/len(data)
    return centroid

centroidX1 = sum(x1)/len(x1)
centroidY1 = sum(y1)/len(y1)

centroidX2 = sum(x2)/len(x2)
centroidY2 = sum(y2)/len(y2)

centroidX3 = centroid(x3)
centroidY3 = centroid(y3)
#sorting from least to greatest 
x1.sort()
y1.sort()
x2.sort()
y2.sort()
x3.sort()
y3.sort()

#converting to numpy array for easier operation
x1 = np.array(x1)
x2 = np.array(x2)
y1 = np.array(y1)
y2 = np.array(y2)
x3 = np.array(x3)
y3 = np.array(y3)

m1 = (centroidY1 - y1[0])/(centroidX1 - x1[0])
c1 = centroidY1 - (m1*centroidX1)

m2 = (centroidY2 - y2[0])/(centroidX2 - x2[0])
c2 = centroidY2 - (m2*centroidX2)

m3 = (centroidY3 - y3[0])/(centroidX3 - x3[0])
c3 = centroidY3 - (m2*centroidX3)

#start best fit line algorithm

#calculate and return y value
def f(x,m,c):
    y = m*x+c
    return y 

#calculate the shortest distance of a point to the line

def shortestDistanceToLine(x,y,m,c):
    distance =  abs(x + m*y + c)/math.sqrt(1+(m**2))
    return distance

#sum of the shortest distance of all point to the line
def sumDistance(x,m,c):
    sumDistance = 0
    for i in x:
        y = f(i, m, c)
        sumDistance += shortestDistanceToLine(i, y, m, c)
    return sumDistance

#calculate gradient
def gradient(x,y,centroidX,centroidY):
    yMinusMeanY = []
    xMinusMeanX = []
    
    for i in range(0,len(x)-1):
        xMinusMeanX.append(x[i]-centroidX)
        yMinusMeanY.append(y[i]-centroidY)
    
    sumXMinusMeanXSquared = 0
    productXY = 0
    
    for i in range(0,len(xMinusMeanX)-1):
        sumXMinusMeanXSquared += xMinusMeanX[i]**2
        productXY += xMinusMeanX[i] * yMinusMeanY[i]
        
    m = productXY/sumXMinusMeanXSquared
    
    return m

#calculate the y-intercept
def yIntercept(x,y,m):
    c = y - (m*x)
    return c
m1 = gradient(x1, y1, centroidX1, centroidY1)
m2 = gradient(x2, y2, centroidX2, centroidY2)
m3 = gradient(x3, y3, centroidX3, centroidY3)

c1 = yIntercept(centroidX1, centroidY1, m1)
c2 = yIntercept(centroidX2, centroidY2, m2)
c3 = yIntercept(centroidX3, centroidY3, m3)

sumDistance1 = sumDistance(x1, m1, c1)
sumDistance2 = sumDistance(x2, m2, c2)
#end of best fit algorithm

#calculation of the lenght of current carrying conductor

def L(m):
    lenght = m*(g/B)
    return lenght 

L1 = L(round(m1,6))
L2 = L(round(m2,6))

#appending y intercept to the data point 
# x1 = np.append(x1,0)
# y1 = np.append(y1,c1)

# x2 = np.append(x2,0)
# y2 = np.append(y2,c2)

# x3 = np.append(x3, 0)
# y3 = np.append(y3,c3)

plt.figure(figsize=(8,6), dpi=300)

x = np.linspace(0,3.8)

plt.scatter(x1,y1, marker = 'x', color = 'blue')
plt.scatter(centroidX1, centroidY1, marker= 'x', color = 'blue')
plt.plot(x,f(x,m1,c1), color  = 'blue', label = "L1")
print("gradient L1: " , round(m1,6), "lenght of L1: ", round(L1, 3), 'm')

plt.scatter(x2,y2, marker='x', color = 'green')
plt.scatter(centroidX2, centroidY2, marker= 'x', color='green')
plt.plot(x,f(x,m2,c2), color = 'green', label="L2")
print("gradient L2: " , round(m2, 6), "lenght of L2: ", round(L2, 3), 'm')

plt.title("Mass(M) against Current(I)")
plt.ylabel("Mass (M)")
plt.xlabel("Current (I)")

plt.legend()
plt.grid()
plt.savefig("C:/Users/coder/OneDrive/Desktop/fig1")

# plt.scatter(x3, y3)
# plt.scatter(centroidX3, centroidY3)
# plt.plot(x3, f(x3,m3,c3))
# print(m3)

plt.show()

