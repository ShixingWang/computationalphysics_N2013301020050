import matplotlib.pyplot as plt
from visual import *
from mpl_toolkits.mplot3d import Axes3D
# import packages
sigma=10
b=8./3
# 二阶龙格-库塔方法
class Lorenz:
    def __init__(self,r=25,x=1,y=0,z=0,dt=0.0001,time=50):
        self.r=r
        self.x0=x
        self.y0=y
        self.z0=z
        self.X=[self.x0]
        self.Y=[self.y0]
        self.Z=[self.z0]
        self.T=[0]
        self.Y_x0=[]
        self.Z_x0=[]
        self.X_y0=[]
        self.Z_y0=[]
        self.dt=dt
        self.time=time
        return None
    # second-order Runge-Kutta method
    def caculate(self):
        while not self.T[-1]>self.time:
            xPrime=self.X[-1]+0.5*sigma*(self.Y[-1]-self.X[-1])*self.dt
            yPrime=self.Y[-1]+0.5*(-self.X[-1]*self.Z[-1]+self.r*self.X[-1]-self.Y[-1])*self.dt
            zPrime=self.Z[-1]+0.5*(self.X[-1]*self.Y[-1]-b*self.Z[-1])*self.dt
            newX=self.X[-1]+sigma*(yPrime-xPrime)*self.dt
            newY=self.Y[-1]+(-xPrime*zPrime+self.r*xPrime-yPrime)*self.dt
            newZ=self.Z[-1]+(xPrime*yPrime-b*zPrime)*self.dt
            newT=self.T[-1]+self.dt
            self.X.append(newX)
            self.Y.append(newY)
            self.Z.append(newZ)
            self.T.append(newT)
            if self.T[-1]>30:
                if newX<0.001 and newX>-0.001:
                    self.Y_x0.append(newY)
                    self.Z_x0.append(newZ)
                if newY<0.001 and newY>-0.001:
                    self.X_y0.append(newX)
                    self.Z_y0.append(newZ)
        return 0
    def phaseXY(self,slogan):
        plt.title("Phase Plot: y versus x")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.plot(self.X,self.Y,label=slogan)
        return 0
    def phaseXZ(self,slogan):
#        plt.title("Phase Plot: z versus x")
        plt.xlabel("x")
        plt.ylabel("z")
        plt.plot(self.X,self.Z,label=slogan)
        return 0
    def phaseYZ(self,slogan):
        plt.title("Phase Plot: z versus y")
        plt.xlabel("y")
        plt.ylabel("z")
        plt.plot(self.Y,self.Z,label=slogan)
        return 0
    def phase(self,slogan):
        fig = plt.figure()
        ax=fig.add_subplot(111, projection='3d')
        ax.plot(self.X,self.Y,self.Z,label=slogan)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        return 0
    def phaseYZ0(self,slogan):
        plt.title("Phase Space Plot: z versus y when x=0")
        plt.xlabel("y")
        plt.ylabel("z")
        plt.scatter(self.Y_x0,self.Z_x0,s=0.1,c='b',label=slogan)
        return 0
    def phaseXZ0(self,slogan):
        plt.title("Phase Space Plot: z versus x when y=0")
        plt.xlabel("x")
        plt.ylabel("z")
        plt.scatter(self.X_y0,self.Z_y0,s=0.1,c='b',label=slogan)
        return 0
    def visual(self):
        return 0
'''
A=Lorenz(time=1000)
A.caculate()

plt.subplot(131)
A.phaseXY()
plt.subplot(132)
A.phaseXZ()
plt.subplot(133)
A.phaseYZ()
# Figure 10_1
'''

A=Lorenz(r=25,time=1000)
A.caculate()
plt.subplot(221)
A.phaseXZ0(slogan='r=25')
plt.legend(loc='upper right',frameon=False)
B=Lorenz(r=50,time=1000)
B.caculate()
plt.subplot(222)
B.phaseXZ0(slogan='r=50')
plt.legend(loc='upper right',frameon=False)
C=Lorenz(r=100,time=1000)
C.caculate()
plt.subplot(223)
C.phaseXZ0(slogan='r=100')
plt.legend(loc='upper right',frameon=False)
D=Lorenz(r=160,time=1000)
D.caculate()
plt.subplot(224)
D.phaseXZ0(slogan='r=160')
#plt.ylim(-1,1)
plt.legend(loc='upper right',frameon=False)
plt.show()
# Figure 10_2

'''
plt.subplot(121)
A.phaseYZ0()
plt.subplot(122)
A.phaseXZ0()
plt.show()
'''