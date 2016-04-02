import math
import matplotlib.pyplot as plt
# import modules
g=9.8
# set constants
class cannon0:
    "the simplest model with no air drag, no air density variance, no probability distribution"
    def __init__(self, x0=0,y0,v0,theta,dt):
        self.x0=x0
        self.y0=y0
        self.v0=v0
        self.theta=theta
        self.vx0=self.v0*math.cos(self.theta)
        self.vy0=self.v0*math.sin(self.theta)
        self.dt=dt        
        return 0
    def fly(self):
        self.X=[self.x0]
        self.Y=[self.y0]
        self.Vx=[self.vx0]
        self.Vy=[self.vy0]
        self.T=[0]
        while not(self.y[-1]<0):
            newVx=self.Vx[-1]
            newVy=self.Vy[-1]-g*self.dt
            self.Vx.append(newVx)
            self.Vy.append(newVy)
            meanVx=0.5*(self.Vx[-1]+self.Vx[-2])
            meanVy-0.5*(self.Vy[-1]+self.Vy[-2])
            meanV=sqrt(meanVx**2+meanVy**2)
            newX=self.X[-1]+meanVx*self.dt
            newY=self.Y[-1]+meanVy*self.dt
            self.X.append(newX)
            self.Y.append(newY)
        r=-self.Y[-2]/self.Y[-1]
        self.X[-1]=(self.X[-2]+r*self.X[-1])/(r+1)
        self.Y[-1]=0
        return 0
    def traj(self, color):
        col=str(color)
        plt.plot[X,Y,col,label="$v_0$=%d,$theta$=%d degrees"%(self.v0,self.theta)]
        return 0
        