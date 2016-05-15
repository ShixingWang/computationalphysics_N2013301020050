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
        xCenter=MeMs*xEarth+self.MjMs*xJupiter
        yCenter=MeMs*yEarth+self.MjMs*yJupiter
        vxSun=math.sqrt(GM*(1+self.MjMs)/Rj)*math.sin(self.theta)/(1+MeMs+self.MjMs)
        vySun=-(MeMs*math.sqrt(GM*(1+MeMs)/Re)+self.MjMs*math.sqrt(GM*(1+self.MjMs)/Rj)*math.cos(self.theta))/(1+MeMs+self.MjMs)
        vxEarth=self.MjMs*math.sqrt(GM*(1+self.MjMs)/Rj)*math.sin(self.theta)/(1+MeMs+self.MjMs)
        vyEarth=-(-math.sqrt(GM*(1+MeMs)/Re)-self.MjMs*math.sqrt(GM*(1+MeMs)/Re)+self.MjMs*math.sqrt(GM*(1+self.MjMs)/Rj)*math.cos(self.theta))/(1+MeMs+self.MjMs)
        vxJupiter=-(1+MeMs)*math.sqrt(GM*(1+self.MjMs)/Rj)*math.sin(self.theta)/(1+MeMs+self.MjMs)
        vyJupiter=-(MeMs*math.sqrt(GM*(1+MeMs)/Re)-(math.sqrt(GM*(1+self.MjMs)/Rj)*math.cos(self.theta))-(MeMs*math.sqrt(GM*(1+self.MjMs)/Rj)*math.cos(self.theta)))/(1+MeMs+self.MjMs)
        self.x0Earth=xEarth-xCenter
        self.y0Earth=yEarth-yCenter
        self.vx0Earth=0
        self.vy0Earth=math.sqrt(GM*(1+MeMs)/Re)
        self.Xearth=[self.x0Earth]
        self.Yearth=[self.y0Earth]
        self.VxEarth=[vxEarth]
        self.VyEarth=[vyEarth]
# --------------Earth above and Jupiter below----------------------------------
        self.x0Jupiter=xJupiter-xCenter
        self.y0Jupiter=yJupiter-yCenter
        self.v0Jupiter=math.sqrt(GM*(1+self.MjMs)/Rj)
        self.vx0Jupiter=-self.v0Jupiter*math.sin(self.theta)
        self.vy0Jupiter=self.v0Jupiter*math.cos(self.theta)
        self.Xjupiter=[self.x0Jupiter]
        self.Yjupiter=[self.y0Jupiter]
        self.VxJupiter=[vxJupiter]
        self.VyJupiter=[vyJupiter]
# ----------------Jupiter above and Sun below----------------------------------
        self.x0Sun=xSun-xCenter
        self.y0Sun=ySun-yCenter
        self.vx0Sun=-MeMs*self.vx0Earth-self.MjMs*self.vx0Jupiter
        self.vy0Sun=-MeMs*self.vy0Earth-self.MjMs*self.vy0Jupiter
        self.Xsun=[self.x0Sun]
        self.Ysun=[self.y0Sun]
        self.VxSun=[vxSun]
        self.VySun=[vySun]        
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
    def plot(self,color1='r',slogan1='Sun',color2='b',slogan2='Earth',color3='orange',slogan3='Jupiter'):
        plt.plot(self.Xsun,self.Ysun,color1,label=slogan1)
        plt.plot(self.Xearth,self.Yearth,color2,label=slogan2)
        plt.plot(self.Xjupiter,self.Yjupiter,color3,label=slogan3)
        return 0
plt.title('Motion with Different Jupiter Masses')
plt.subplot(221)
plt.xlim(-6,6)
plt.ylim(-8,6)
plt.xlabel('x [AU]')
plt.ylabel('y [AU]')
A=precession(Mj=1,theta=0,time=15)
A.calculate()
A.plot()
plt.legend(loc='lower right',frameon=False)
plt.subplot(222)
plt.xlim(-6,6)
plt.ylim(-8,6)
plt.xlabel('x [AU]')
plt.ylabel('y [AU]')
A=precession(Mj=10,theta=0,time=15)
A.calculate()
A.plot()
plt.legend(loc='lower right',frameon=False)
plt.subplot(223)
plt.xlim(-6,6)
plt.ylim(-8,6)
plt.xlabel('x [AU]')
plt.ylabel('y [AU]')
A=precession(Mj=100,theta=0,time=15)
A.calculate()
A.plot()
plt.legend(loc='lower right',frameon=False)
plt.subplot(224)
plt.xlim(-6,6)
plt.ylim(-8,6)
plt.xlabel('x [AU]')
plt.ylabel('y [AU]')
A=precession(Mj=1000,theta=0,time=15)
A.calculate()
A.plot()
plt.legend(loc='lower right',frameon=False)
plt.show()
