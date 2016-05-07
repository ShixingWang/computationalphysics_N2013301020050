# import packages
import math
import matplotlib.pyplot as plt
# physical constants
GM=4*math.pi**2
alpha=
a=0.39 # the semimajor axis of Mecury, be be included into the class as an entry later.
# begin the class
class precession:
    def __init__(self,e,perihelion,time,dt):
        self.e=e
        self.x0=a*(1+e)
        self.vx0=0
        self.y0=0
        self.vy0=math.sqrt((GM*(1-e))/a*(1+e))
        self.X=[self.x0]
        self.Vx=[self.vx0]
        self.Y=[self.y0]
        self.Vy=[self.vy0]
        self.T=[0]
        self.dt=dt
        self.time=time
        return None
    def calculate(self):
        while self.T[-1]<self.time:
            r=math.sqrt(self.X[-1]**2+self.Y[-1]**2)
            newVx=self.Vx[-1]-GM*(1+alpha/r**2)self.X[-1]/r**3*self.dt
            self.Vx.append(newVx)
            newX=self.X[-1]+newVx*self.dt
            self.X.append(newX)
            newVy=self.Vy[-1]-GM*(1+alpha/r**2)self.Y[-1]/r**3*self.dt
            self.Vy.append(newVy)
            newY=self.Y[-1]+newVy*self.dt
            self.Y.append(newY)
            self.T.append(self.T[-1]+self.dt)
        return 0
    def plot(self,color,slogan):
        return 0