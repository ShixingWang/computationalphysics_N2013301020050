import math
import matplotlib.pyplot as plt
from visual import *
import numpy as np
# import packages
sigma=10
b=8./3
# 二阶龙格-库塔方法
class Lorenz:
    def __init__(r=25,x,y,z,dt=0.0001,time=50):
        self.r=r
        self.x0=x
        self.y0=y
        self.z0=z
        self.X=[self.x0]
        self.Y=[self.y0]
        self.Z=[self.z0]
        self.T=[0]
    # second-order Runge-Kutta method
    def caculate(self):
        tPrime=self.T[-1]+0.5*self.dt
        xPrime=self.X[-1]+0.5*sigma*(self.Y[-1]-self.X[-1])*self.dt
        yPrime=
        zPrime=
        newX=
        newY=
        newZ=
        newT=self.T[-1]+dt
        
        