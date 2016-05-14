# import packages
import math
# import numpy as np
import matplotlib.pyplot as plt
# physical constants
GM=4*(math.pi**2)
Me=0.000003
MjMs=0.00095 # mass ratio of Jupiter over Sun
MeMs=0.000003 # mass ratio of Earth over Sun
Re=1. # SEMIMAJOR axis of Mercury
Rj=5.2  # radius of Jupiter
# perihelion=0.39*(1-0.206) # to remain the oerihelion the same as that of Mercury.

class precession:
    def __init__(self,Mj=1,theta=0,time=2.,dt=0.0001):
        self.MjMs=Mj*MjMs
        self.theta=theta*math.pi/180
        xEarth=Re
        yEarth=0
        xJupiter=Rj*math.cos(self.theta)
        yJupiter=Rj*math.sin(self.theta)
        xSun=0
        ySun=0
        xCenter=MeMs*xEarth+MjMs*xJupiter
        yCenter=MeMs*yEarth+MjMs*yJupiter
        self.x0Earth=xEarth-xCenter
        self.y0Earth=yEarth-yCenter
        self.vx0Earth=0
        self.vy0Earth=math.sqrt(GM*(1+MeMs)/Re)
        self.Xearth=[self.x0Earth]
        self.Yearth=[self.y0Earth]
        self.VxEarth=[self.vx0Earth]
        self.VyEarth=[self.vy0Earth]
# --------------Earth above and Jupiter below----------------------------------
        self.x0Jupiter=xJupiter-xCenter
        self.y0Jupiter=yJupiter-yCenter
        self.v0Jupiter=math.sqrt(GM*(1+self.MjMs)/Rj)
        self.vx0Jupiter=-self.v0Jupiter*math.sin(self.theta)
        self.vy0Jupiter=self.v0Jupiter*math.cos(self.theta)
        self.Xjupiter=[self.x0Jupiter]
        self.Yjupiter=[self.y0Jupiter]
        self.VxJupiter=[self.vx0Jupiter]
        self.VyJupiter=[self.xy0Jupiter]
# ----------------Jupiter above and Sun below----------------------------------
        self.x0Sun=xSun-xCenter
        self.y0Sun=ySun-yCenter
        self.vx0Sun=-MeMs*self.vx0Earth-MjMs*self.vx0Jupiter
        self.vy0Sun=-MeMs*self.vy0Earth-MjMs*self.vy0Jupiter
        self.Xsun=[self.x0Sun]
        self.Ysun=[self.y0Sun]
        self.VxSun=[self.vx0Sun]
        self.VySun=[self.xy0Sun]        
# ---------------Time Relevent and Special Variables below---------------------
        self.T=[0]
        self.dt=dt
        self.time=time
        return None
    def calculate(self):
        while self.T[-1]<self.time:
            rES=math.sqrt((self.Xearth[-1]-self.Xsun[-1])**2+(self.Yearth[-1]-self.Ysun[-1])**2)
            rJS=math.sqrt((self.Xjupiter[-1]-self.Xsun[-1])**2+(self.Yjupiter[-1]-self.Ysun[-1])**2)
            rEJ=math.sqrt((self.Xearth[-1]-self.Xjupiter[-1])**2+(self.Yearth[-1]-self.Yjupiter[-1])**2)
            newVxEarth=self.VxEarth[-1]-(GM*(self.Xearth[-1]-self.Xsun[-1])/rES**3)*self.dt-(GM*self.MjMs*(self.Xearth[-1]-self.Xjupiter[-1])/rEJ**3)*self.dt
            newXearth=self.Xearth[-1]+newVxEarth*self.dt
            newVyEarth=self.VyEarth[-1]-(GM*(self.Yearth[-1]-self.Ysun[-1])/rES**3)*self.dt-(GM*self.MjMs*(self.Yearth[-1]-self.Yjupiter[-1])/rEJ**3)*self.dt
            newYearth=self.Yearth[-1]+newVyEarth*self.dt
            self.VxEarth.append(newVxEarth)
            self.VyEarth.append(newVyEarth)
            self.Xearth.append(newXearth)
            self.Yearth.append(newYearth)
            # -----------------Earth Above and Jupiter Above-------------------
            newVxJupiter=self.VxJupiter[-1]-(GM*(self.Xjupiter[-1]-self.Xsun[-1])/rJS**3)*self.dt-(GM*MeMs*(self.Xjupiter[-1]-self.Xearth[-1])/rEJ**3)*self.dt
            newXjupiter=self.Xjupiter[-1]+newVxJupiter*self.dt
            newVyJupiter=self.VyJupiter[-1]-(GM*(self.Yjupiter[-1]-self.Ysun[-1])/rJS**3)*self.dt-(GM*MeMs*(self.Yjupiter[-1]-self.Yearth[-1])/rEJ**3)*self.dt
            newYjupiter=self.Yjupiter[-1]+newVyJupiter*self.dt
            self.VxJupiter.append(newVxJupiter)
            self.VyJupiter.append(newVyJupiter)
            self.Xjupiter.append(newXjupiter)
            self.Yjupiter.append(newYjupiter)           
            # -----------------Jupiter Above and Sun Below---------------------            
            newVxSun=self.VxSun[-1]-(GM*MeMs*(self.Xsun[-1]-self.Xearth[-1])/rES**3)*self.dt-(GM*self.MjMs*(self.Xsun[-1]-self.Xjupiter[-1])/rJS**3)*self.dt
            newXsun=self.Xsun[-1]+newVxSun*self.dt
            newVySun=self.VySun[-1]-(GM*MeMs*(self.Ysun[-1]-self.Yearth[-1])/rES**3)*self.dt-(GM*self.MjMs*(self.Ysun[-1]-self.Yjupiter[-1])/rJS**3)*self.dt
            newYsun=self.Ysun[-1]+newVySun*self.dt
            self.VxSun.append(newVxSun)
            self.VySun.append(newVySun)
            self.Xsun.append(newXsun)
            self.Ysun.append(newYsun)              
            self.T.append(self.T[-1]+self.dt)
        return 0
    def plotMercury(self,color='k',slogan='Mercury'):
        plt.plot(self.Xmercury,self.Ymercury,color,label=slogan)
        plt.scatter([0],[0],s=5,c='y',label='Sun')
        return 0
    def plotJupiter(self,color='k',slogan='Jupiter'):
        plt.plot(self.Xjupiter,self.Yjupiter,color,label=slogan)
        return 0

A=precession(Mj=100,theta=0,time=20)
A.calculate()
plt.subplot(121)
A.plotMercury(color='c',slogan='Mercury')
plt.subplot(122)
A.orientation()
'''
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