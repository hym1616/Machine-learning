import numpy as np
import matplotlib.pyplot as plt

def h(X,theta):
    return theta[0]+theta[1]*X
def Cost(X,Y,theta):
    tmp2=np.power(h(X,theta)-Y,2)
    Sum=0
    for i in range(0,len(tmp2)):
        Sum=Sum+tmp2[i]
    return ((1/(2*len(Y)))*Sum)
def gradient_descent(X,Y,theta,alpha,n):
    theta_new=np.zeros(2)
    for k in range(0,n):
        for i in range(0,len(theta)):
            if i==0:
                Sum=sum(h(X,theta)-Y)
            else:
                Sum=sum(np.multiply((h(X,theta)-Y),X))
            theta_new[i]=theta[i]-alpha*(1/len(Y))*Sum
        theta=theta_new[:]
    return theta_new

print(0)
data=np.loadtxt("C:/Users/12168/Desktop/data.txt",delimiter=',')
print(data)
xdata=data[:,0]
ydata=data[:,1]
theta=np.zeros(2)
print(theta)
tmp=Cost(xdata,ydata,theta)
print("初始成本为 ",tmp)
alpha=0.01
n=1500
theta=gradient_descent(xdata,ydata,theta,alpha,n)
print("最后的参数为：",theta)

