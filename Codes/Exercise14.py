# import packages
import math
import numpy as np
import matplotlib.pyplot as plt
# physical constants
c=1000
r=1
k=1000

class wave:
    def __init__(self,x0=0.3,length=1,time=10,dt=0.001):
        self.x0=x0
        self.length=length
        self.time=time
        self.dt=dt
        self.dx=c*dt/r
        self.i=length/self.dx
        self.n=time/dt
        self.X0=np.linspace(0,length,self.i,endpoint=True)
        self.Y0=np.exp(-k*(self.X0-x0)**2)
        return None
    def calculate(self):
        self.Y=[None for cycle1 in range(self.n+1)]
        self.Y[0]=self.Y0
        
        