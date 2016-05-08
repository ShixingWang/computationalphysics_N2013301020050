# import packages
import math
import numpy as np
import matplotlib.pyplot as plt
# physical constants
GM=4*(math.pi**2)
alpha=0.0008
perihelion=0.39*(1-0.206) # to remain the oerihelion the same as that of Mercury.
# begin the class
class precession:
    def __init__(self,e=0.206,time=2.,dt=0.0001):
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
            newX=self.X[-1]+newVx*self.dt
            newVy=self.Vy[-1]-(GM*(1+alpha/r**2)*self.Y[-1]/r**3)*self.dt
            newY=self.Y[-1]+newVy*self.dt
            if abs(newX*newVx+newY*newVy)<0.0014 and r<self.a:
                theta=math.acos(self.X[-1]/r)*180/math.pi
                if (self.Y[-1]/r)<0:
                    theta=360-theta
                theta=abs(theta-180)
                self.ThetaPrecession.append(theta)
                self.TimePrecession.append(self.T[-1])
            self.Vx.append(newVx)
            self.Vy.append(newVy)
            self.X.append(newX)
            self.Y.append(newY)
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

A=precession(e=0.206,time=5)
A.calculate()
A.plot(color='r',slogan=r'e=0.206')

B=precession(e=0.5,time=5.0)
B.calculate()
B.plot(color='b',slogan='e=0.5')
plt.legend(loc='upper right',frameon=False)

C=precession(e=0.8,time=25)
C.calculate()
C.plot(color='g',slogan='e=0.8')
plt.legend(loc='upper right',frameon=False)

#plt.xlim(-0.5,0.7)
plt.xlabel("x [AU]")
plt.ylabel("y [AU]")
plt.title("Simulation of the precession of Mercury")
plt.legend(loc='upper right',frameon=False)

'''
A=precession(e=0.206,time=2.)
A.calculate()
A.orientation(color='k',slogan=r'$\alpha=0.0008$')
plt.xlabel("Time [yr]")
plt.ylabel(r"$\theta$ [$\degree$]")
plt.title("Orbit Orientation versus Time")
'''
'''
PrecessionRate=[8.609, 6.129, 4.183, 2.769, 1.737, 0.999, 0.483, 0.146]
PrecessionRate=np.array(PrecessionRate)
Eccentricity=[0.206,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
Eccentricity=np.array(Eccentricity)
Lower=[8.536,6.095,4.161,2.750,1.720,0.970,0.483,0.132]
Lower=np.array(Lower)
Upper=[8.681,6.162,4.204,2.789,1.755,1.028,0.483,0.160]
Upper=np.array(Upper)
yUpper=Upper-PrecessionRate
yLower=PrecessionRate-Lower
plt.errorbar(Eccentricity,PrecessionRate,yerr=[yLower,yUpper],fmt='b-',ecolor='r',capthick=2,label='Precession Rate versus Eccentricity')
plt.xlabel("Eccentricity")
plt.ylabel(r"Precession Rate [$\degree/yr$]")
plt.title("Precession Rate versus Eccectricity")
#x=np.arange(0.2,0.95,0.01)
#y=13.67*np.sqrt((1-x)**3)/(1+x)
#plt.plot(x,y,'b',label=r'Fiiting Curve $f(x)=a*\sqrt{(1-x)^3}/(1+x)$')
#plt.legend(loc='upper right',frameon=False)
'''