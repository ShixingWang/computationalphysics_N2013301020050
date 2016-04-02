import math
import matplotlib.pyplot as plt
# import modules
g=9.8
B2m=0.004
y_zero=10000
a=0.0065
T0=300
alpha=2.5
# set constants
class cannon0:
    "the simplest model with no air drag, no air density variance, no probability distribution"
    # initialize variables    
    def __init__(self,v0,theta):
        self.x0=0
        self.y0=0
        self.v0=v0
        self.theta=theta*math.pi/180
        self.vx0=self.v0*math.cos(self.theta)
        self.vy0=self.v0*math.sin(self.theta)
        self.dt=0.01        
        return None
    # external force other than gravity, no force in simplest case        
    def F(self,vx,vy,y=1):
        return 0,0
    # calculate the flying trajactory
    def fly(self):
        self.X=[self.x0]
        self.Y=[self.y0]
        self.Vx=[self.vx0]
        self.Vy=[self.vy0]
        self.T=[0]
        while not(self.Y[-1]<0):
            newVx=self.Vx[-1]+self.F(vx=self.Vx[-1],vy=self.Vy[-1],y=self.Y[-1])[0]*self.dt
            newVy=self.Vy[-1]-g*self.dt+self.F(self.Vx[-1],self.Vy[-1])[1]*self.dt
            self.Vx.append(newVx)
            self.Vy.append(newVy)
            meanVx=0.5*(self.Vx[-1]+self.Vx[-2])
            meanVy=0.5*(self.Vy[-1]+self.Vy[-2])
#            meanV=math.sqrt(meanVx**2+meanVy**2) # not used in Cannon0 because there is no air drag
            newX=self.X[-1]+meanVx*self.dt
            newY=self.Y[-1]+meanVy*self.dt
            self.X.append(newX)
            self.Y.append(newY)
        # fix the final landing coordinate        
        r=-self.Y[-2]/self.Y[-1]
        self.X[-1]=(self.X[-2]+r*self.X[-1])/(r+1)
        self.Y[-1]=0
        return 0
    # represent trajectory 
    def plot(self, color):
#        col=str(color)
#        plt.plot(X,Y)
        plt.plot(self.X,self.Y,color,label="$v_0=%dm/s$,$\psi=%d\degree$"%(self.v0,self.theta))
        return 0

class cannon1(cannon0):
    "the second simplest model with no air drag under constant air density, no probability distribution"    
    # external force other than gravity        
    def F(self,vx,vy,y=1):
        vl=math.sqrt(vx**2+vy**2)
        self.Fx=-B2m*vx*vl
        self.Fy=-B2m*vy*vl
        return self.Fx,self.Fy
class cannon2(cannon0):
    "the model concerning ISOTHERMAL air density variance but no probability distribution"
    def F(self,vx,vy,x=1,y=1):
        vl=math.sqrt(vx**2+vy**2)
        self.Fx=-B2m*vx*vl*math.exp(-y/y_zero)
        self.Fy=-B2m*vy*vl*math.exp(-y/y_zero)
        return self.Fx,self.Fy
class cannon3(cannon0):
    "the model concerning ADIABATIC air density variance but no probability distribution"    
    def F(self,vx,vy,y=1):
        vl=math.sqrt(vx**2+vy**2)
        self.Fx=-B2m*vx*vl*(1-a*y/T0)**alpha
        self.Fy=-B2m*vy*vl*(1-a*y/T0)**alpha
        return self.Fx,self.Fy
class cannon4(cannon0):
    "the model concerning probability distribution"

A=cannon0(20,45)
A.fly()
A.plot('red')

B=cannon1(20,45)
B.fly()
B.plot('green')

C=cannon2(20,45)
C.fly()
C.plot('blue')

D=cannon3(20,45)
D.fly()
D.plot('orange')

plt.legend(loc='upper right', frameon=False)