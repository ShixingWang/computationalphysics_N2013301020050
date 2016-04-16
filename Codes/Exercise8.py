import math
import matplotlib.pyplot as plt
# import modules above
l=1
k=1
alpha=1
# define constants above
class pandulum:
    def __init__(self,x0=0.1,v0=0,time=5):
        self.x0=x0
        self.v0=v0
        self.theta=self.x0/l
        self.omega=self.v0/l
        self.dt=0.1
        self.time=time
        return 0
    def sway(self):
        self.Theta=[self.theta]
        self.Omega=[self.omega]
        self.T=[0]
        while not self.T[-1]>self.time:
            newOmega=self.Omega[-1]-k*(self.Theta[-1])**alpha*self.dt
            newTheta=self.Theta[-1]+newOmega*self.dt
            newT=self.T[-1]+self.dt
            self.Omega.append(newOmega)
            self.Theta.append(newTheta)
            self.T.append(newT)
        return 0
    def visual(self):
        
    