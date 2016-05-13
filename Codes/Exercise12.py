# import packages
import math
import numpy as np
import matplotlib.pyplot as plt
# physical constants
GM=4*(math.pi**2)
MjMs=0.00095 # mass ratio of Jupiter over Sun
MmMs=0.00000012 # mass ratio of Mercury over Sun
e=0.206 # eccentricity of Mercury
aMercury=0.39 # SEMIMAJOR axis of Mercury
radiusJupiter=5.2  # radius of Jupiter
# perihelion=0.39*(1-0.206) # to remain the oerihelion the same as that of Mercury.

class precession:
    def __init__(self,Mj=1,theta=0,time=2.,dt=0.0001):
        self.theta=theta*math.pi/180
#        self.a=perihelion/(1-e)
        self.x0Mercury=aMercury
        self.y0Mercury=0
        self.vx0Mercury=0
        self.vy0Mercury=math.sqrt((GM*(1-e))(1+MmMs)/(aMercury*(1+e)))
        self.Xmercury=[self.x0Mercury]
        self.Ymercury=[self.y0Mercury]
        self.VxMercury=[self.vx0Mercury]
        self.VyMercury=[self.vy0Mercury]
# ------------Mercury above and Jupiter below----------------------------------
        self.x0Jupiter=radiusJupiter*math.cos(self.theta)
        self.y0Jupiter=radiusJupiter*math.sin(self.theta)
        self.v0Jupiter=math.sqrt(GM(1+MjMs)/(radiusJupiter))
        self.vx0Jupiter=-self.v0Jupiter*math.sin(self.theta)
        self.xy0Jupiter=self.v0Jupiter*math.cos(self.theta)
        self.Xjupiter=[self.x0Jupiter]
        self.Yjupiter=[self.y0Jupiter]
        self.VxJupiter=[self.vx0Jupiter]
        self.VyJupiter=[self.xy0Jupiter]
# ---------------Time Relevent Variables below---------------------------------
        self.T=[0]
        self.dt=dt
        self.time=time
        self.PsiPrecession=[]
        self.TimePrecession=[]
        return None
    def calculate(self):
        while self.T[-1]<self.time:
            rMercury=math.sqrt(self.Xmercury[-1]**2+self.Ymercury[-1]**2)
            rJupiter=math.sqrt(self.Xjupiter[-1]**2+self.Yjupiter[-1]**2)
            rMJ=math.sqrt((self.Xmercury[-1]-self.Xjupiter[-1])**2+(self.Ymercury[-1]-self.Yjupiter[-1])**2)
            newVxMercury=self.VxMercury[-1]-(GM*self.X[-1]/rMercury**3)*self.dt-(GM*MjMs*(self.Xmercury[-1]-self.Xjupiter[-1])/rMJ**3)*self.dt
            newXmercury=self.Xmercury[-1]+newVxMercury*self.dt
            newVyMercury=self.VyMercury[-1]-(GM*self.Ymercury[-1]/rMercury**3)*self.dt-(GM*MjMs*(self.Ymercury[-1]-self.Yjupiter[-1])/rMJ**3)*self.dt
            newYmercury=self.Ymercury[-1]+newVyMercury*self.dt
            if abs(newXmercury*newVxMercury+newYmercury*newVyMercury)<0.001 and rMercury<aMercury:
                psi=math.acos(self.Xmercury[-1]/rMercury)*180/math.pi
                if (self.Ymercury[-1]/rMercury)<0:
                    psi=360-psi
                psi=abs(psi-180)
                self.PsiPrecession.append(psi)
                self.TimePrecession.append(self.T[-1])
            self.VxMercury.append(newVxMercury)
            self.VyMercury.append(newVyMercury)
            self.Xmercury.append(newXmercury)
            self.Ymercury.append(newYmercury)
            # ---------------Mercury Above and Jupiter Above-------------------
            newVxJupiter=self.VxJupiter[-1]-(GM*self.Xjupiter[-1]/rJupiter**3)*self.dt-(GM*MmMs*(self.Xjupiter[-1]-self.Xmercury[-1])/rMJ**3)*self.dt
            newXjupiter=self.Xjupiter[-1]+newVxJupiter*self.dt
            newVyJupiter=self.VyJupiter[-1]-(GM*self.Yjupiter[-1]/rJupiter**3)*self.dt-(GM*MmMs*(self.Yjupiter[-1]-self.Ymercury[-1])/rMJ**3)*self.dt
            newYjupiter=self.Yjupiter[-1]+newVyJupiter*self.dt
            self.VxJupiter.append(newVxJupiter)
            self.VyJupiter.append(newVyJupiter)
            self.Xjupiter.append(newXjupiter)
            self.Yjupiter.append(newYjupiter)           
            self.T.append(self.T[-1]+self.dt)
        return 0
    def plot(self,color1='k',color2='k',slogan1='',slogan2=''):
        plt.plot(self.Xmercury,self.Ymercury,color1,label=slogan1)
        plt.plot(self.Xjupiter,self.Yjupiter,color2,label=slogan2)
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