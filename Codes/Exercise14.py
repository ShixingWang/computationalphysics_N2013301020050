# import packages
import math
import numpy as np
import matplotlib.pyplot as plt
# physical constants
c=1000
r=1

class wave:
    def __init__(self,length=1,time=10,dt=0.001):
        self.length=length
        self.time=time
        self.dt=dt
        self.dx=c*dt/r
        self.i=length/self.dx
        self.n=time/dt
        return None
    def calculate(self):
        self.Y=[0.]*self.i
        self.newY=[0.]*self.j
        