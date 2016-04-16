import math
import matplotlib.pyplot as plt
from visual import *
# import modules
g=9.8
B2m=0.00004
y_zero=10000
a=0.0065
T0=300
alpha=2.5
# set constants
class cannon0:
    "the simplest model with no air drag, no air density variance, no probability distribution"
    # initialize variables    
    def __init__(self,v0,theta,zFinal=0):
        self.x0=0
        self.y0=0
        self.z0=0
        self.zFinal=zFinal
        self.v0=v0
        self.Theta=theta
        self.theta=theta*math.pi/180
        self.vx0=self.v0*math.cos(self.theta)
        self.vy0=self.v0*math.sin(self.theta)
        self.vz0=0
        self.dt=0.05
        return None
    # external force other than gravity, no force in simplest case        
    def F(self,vx,vy,y=1):
        return 0,0,0
    # calculate the flying trajactory
    def fly(self):
        self.X=[self.x0]
        self.Y=[self.y0]
        self.Z=[self.z0]
        self.Vx=[self.vx0]
        self.Vy=[self.vy0]
        self.Vz=[self.vz0]
        self.T=[0]
        while (self.Z[-1] >= self.zFinal):
            newVx=self.Vx[-1]+self.F(vx=self.Vx[-1],vy=self.Vy[-1])[0]*self.dt
            newVz=self.Vy[-1]-g*self.dt+self.F(self.Vx[-1],self.Vy[-1])[1]*self.dt
            newVy=self.Vz[-1]+self.F(vx=self.Vx[-1],vy=self.Vy[-1])[2]*self.dt
            self.Vx.append(newVx)
            self.Vy.append(newVy)
            self.Vz.append(newVz)
            meanVx=0.5*(self.Vx[-1]+self.Vx[-2])
            meanVy=0.5*(self.Vy[-1]+self.Vy[-2])
            meanVz=0.5*(self.Vz[-1]+self.Vz[-2])
#            meanV=math.sqrt(meanVx**2+meanVy**2) # not used in Cannon0 because there is no air drag
            newX=self.X[-1]+meanVx*self.dt
            newY=self.Y[-1]+meanVy*self.dt
            newZ=self.Z[-1]+meanVz*self.dt
            self.X.append(newX)
            self.Y.append(newY)
            self.Z.append(newZ)
        # fix the final landing coordinate        
#        r=-self.Y[-2]/self.Y[-1]
        self.X[-1]=((self.Z[-2]-self.zFinal)*self.Z[-1]+(self.zFinal-self.Z[-1])*self.X[-2])/(self.Z[-2]-self.Z[-1])
        self.Z[-1]=self.zFinal
        print len(self.Vx)
        return 0
    # get the final distance shells can reach
    def distance(self):
        return math.sqrt((self.X[-1])**2+(self.Z[-1])**2)
    def height(self):
        return max(self.Y)
    # represent trajectory 
    def plot(self, color):
        plt.plot(self.X,self.Y,color,label="$%dm/s$,$%d\degree$, no air drag"%(self.v0,self.Theta))
        return 0
    def plot3D(self):
        return 0
    def plotVisual(self):
        ball=sphere(pos=(self.X[0],self.Y[0],self.Z[0]),radius=200,color=color.yellow)
        t=0
        delta=0.01
        i=0
        while ball.pos.z>=self.zFinal:
            rate(100)
            ball.velocity=vector(self.Vx[i],10*self.Vy[i],self.Vz[i])
            ball.pos=ball.pos+ball.velocity*delta
            t=t+delta
            i+=1

        
class cannon1(cannon0):
    "the second simplest model with no air drag under constant air density, no probability distribution"    
    # external force other than gravity        
    def F(self,vx,vy,y=1):
        vl=math.sqrt(vx**2+vy**2)
        self.Fx=-B2m*vx*vl
        self.Fy=-B2m*vy*vl
        return self.Fx,self.Fy
    def plot(self, color):
        plt.plot(self.X,self.Y,color,label="$%dm/s$,$%d\degree$, uniform air drag"%(self.v0,self.Theta))
        return 0
class cannon2(cannon0):
    "the model concerning ISOTHERMAL air density variance but no probability distribution"
    def F(self,vx,vy,x=1,y=1):
        vl=math.sqrt(vx**2+vy**2)
        self.Fx=-B2m*vx*vl*math.exp(-y/y_zero)
        self.Fy=-B2m*vy*vl*math.exp(-y/y_zero)
        return self.Fx,self.Fy
    def plot(self, color):
        plt.plot(self.X,self.Y,color,label="$%dm/s$,$%d\degree$, isothermal air drag"%(self.v0,self.Theta))
        return 0
class cannon3(cannon0):
    "the model concerning ADIABATIC air density variance but no probability distribution"    
    def F(self,vx,vy,y=1):
        vl=math.sqrt(vx**2+vy**2)
        self.Fx=-B2m*vx*vl*(1-a*y/T0)**alpha
        self.Fy=-B2m*vy*vl*(1-a*y/T0)**alpha
        return self.Fx,self.Fy
    def plot(self, color):
        plt.plot(self.X,self.Y,color,label="$%dm/s$,$%d\degree$, adiabatic air drag"%(self.v0,self.Theta))
        return 0

# select the angle casting the largest distance
A=cannon0(600,45)
A.fly()
arrow(pos = (0, 0, 0), axis = (10000, 0, 0), shaftwidth = 30, color = color.blue)
label(text = 'Horizontal distance', pos = (10000, 0, 0))
arrow(pos = (0, 0, 0), axis = (0, 10000, 0), shaftwidth = 30, color = color.blue)
label(text = 'Vertical distance', pos = (0, 10000, 0))
arrow(pos = (0, 0, 0), axis = (0, 0, 10000), shaftwidth = 30, color = color.blue)
label(text = 'Z axis', pos = (0, 0, 10000))
while True:
    A.plotVisual()
