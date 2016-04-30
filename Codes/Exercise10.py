import math
import matplotlib.pyplot as plt
from visual import *
import numpy as np
# import packages
sigma=10
b=8./3
# 二阶龙格-库塔方法
class Lorenz:
    def __init__(r=25,x=1,y=0,z=0,dt=0.0001,time=50):
        self.r=r
        self.x0=x
        self.y0=y
        self.z0=z
        self.X=[self.x0]
        self.Y=[self.y0]
        self.Z=[self.z0]
        self.T=[0]
        self.time=time
        return None
    # second-order Runge-Kutta method
    def caculate(self):
        while not self.T[-1]>self.time:
            xPrime=self.X[-1]+0.5*sigma*(self.Y[-1]-self.X[-1])*self.dt
            yPrime=self.Y[-1]+0.5*(-self.X[-1]*self.Z[-1]+self.r*self.X[-1]-self.Y[-1])*self.dt
            zPrime=self.Z[-1]+0.5*(self.X[-1]*self.Y[-1]-b*self.Z[-1])*self.dt
            newX=self.X[-1]+sigma*(yPrime-zPrime)*self.dt
            newY=self.Y[-1]+(-xPrime*zPrime+r*xPrime-yPrime)*self.dt
            newZ=self.Z[-1]+(xPrime*yPrime-b*zPrime)*self.dt
            newT=self.T[-1]+self.dt
            self.X.append(newX)
            self.Y.append(newY)
            self.Z.append(newZ)
            self.T.append(newT)
        return 0
    def visual(self):
        return 0