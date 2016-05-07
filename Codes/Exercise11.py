# import packages
import math
import matplotlib.pyplot as plt
# physical constants
GM=4*math.pi**2
alpha=0.0008
perihelion=0.39*(1-0.206) # to remain the oerihelion the same as that of Mercury.
# begin the class
class precession:
    def __init__(self,e=0.206,time=2.5,dt=0.0001):
        self.e=e
        self.a=perihelion/(1-e)
        self.x0=self.a*(1+e)
        self.y0=0
        self.vx0=0
        self.vy0=math.sqrt((GM*(1-e))/(self.a*(1+e)))
        self.X=[self.x0]
        self.Y=[self.y0]
        self.Vx=[self.vx0]
        self.Vy=[self.vy0]
        self.T=[0]
        self.dt=dt
        self.time=time
        self.ThetaPrecession=[]
        self.TimePrecession=[]
        return None
    def calculate(self):
        while self.T[-1]<self.time:
            r=math.sqrt(self.X[-1]**2+self.Y[-1]**2)
            newVx=self.Vx[-1]-(GM*(1+alpha/r**2)*self.X[-1]/r**3)*self.dt
            self.Vx.append(newVx)
            newX=self.X[-1]+newVx*self.dt
            self.X.append(newX)
            newVy=self.Vy[-1]-(GM*(1+alpha/r**2)*self.Y[-1]/r**3)*self.dt
            self.Vy.append(newVy)
            newY=self.Y[-1]+newVy*self.dt
            self.Y.append(newY)
            if abs(newX*newVx+newY*newVy)<0.001 and r<self.a:
                theta=math.acos(newX/r)
                if newY/r <0:
                    theta=360-theta
                self.ThetaPrecession.append(theta)
                self.TimePrecession.append(self.T[-1])
            self.T.append(self.T[-1]+self.dt)
        return 0
    def plot(self,color='k',slogan=''):
        plt.plot(self.X,self.Y,color,label=slogan)
        return 0
    def orientation(self,color='k',slogan=''):
        plt.scatter(self.TimePrecession,self.ThetaPrecession,c=color,label=slogan)
        print self.ThetaPrecession
        print self.TimePrecession
        return 0

A=precession()
A.calculate()
A.orientation()