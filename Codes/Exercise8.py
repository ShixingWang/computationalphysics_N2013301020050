import math
import matplotlib.pyplot as plt
from visual import *
# import modules above
l=1
k=1
# define constants above
class pendulum:
    def __init__(self,alpha=1,x0=0.2,v0=0,time=10,dt=0.001):
        self.alpha=alpha
        self.x0=x0
        self.v0=v0
        self.theta=math.asin(self.x0/l)
        self.omega=self.v0/l
        self.dt=dt
        self.time=time
        self.Theta=[self.theta]
        self.Omega=[self.omega]
        self.T=[0]
        return None
    def sway(self):
        while not self.T[-1]>self.time:
            newOmega=self.Omega[-1]-k*(self.Theta[-1])**self.alpha*self.dt
            self.Omega.append(newOmega)
            newTheta=self.Theta[-1]+newOmega*self.dt
            self.Theta.append(newTheta)
            newT=self.T[-1]+self.dt
            self.T.append(newT)
        return 0
    def period(self):
        period=[]
        for i in range(len(self.Theta)):
            if abs(self.Theta[i]-self.theta)<0.0000005:
                period.append(self.T[i])
#        for j in range(len(period)-1):
#            period[i+1]=period[i+1]-period[1]
        return period[5]-period[4]
    def plotTheta(self,style='black',slogan=''):
        plt.plot(self.T,self.Theta,style,label=slogan)
        return 0        
    def visual(self):
        ball=sphere(pos=(self.x0,math.cos(self.theta),0),radius=2,color=color.white)
        t=0
        delta=self.dt
        i=0
        while 1:
            rate(100)
            ball.velocity=vector(-l*self.Omega[i]*math.cos(self.Theta[i]),-l*self.Omega[i]*math.sin(self.Theta[i]),0)
            ball.pos=ball.pos+ball.velcity*delta
            t=t+delta            
            i+=1
'''
# ----------------part 1 of Exercise 8-----------------------------------------
A=pendulum(alpha=3,x0=0.2,time=40)
A.sway()
A.plotTheta(slogan='Amplitude=0.2')
print A.period()    
'''
'''
# ----------------part 2 of Exercise 8-----------------------------------------
C=pendulum(alpha=3,x0=0.4,time=40)
C.sway()
C.plotTheta(style='blue',slogan='Amplitude=0.4')
print C.period() 
'''
'''
# ----------------part 4 of Exercise 8-----------------------------------------
D=pendulum(alpha=3,x0=0.6,time=40)
D.sway()
D.plotTheta(style='green',slogan='Amplitude=0.6') 
print D.period()
'''
'''
B=pendulum(alpha=3,x0=0.8,time=40)
B.sway()
#B.plotTheta(style='red',slogan='Amplitude=0.8')
print B.period()
'''

E=pendulum(alpha=2,x0=0.1,dt=0.04,time=15)
E.sway()
E.plotTheta(style='purple',slogan='Amplitude=1.0')
#print E.period()
# ----------------part 3 of Exercise 8-----------------------------------------

'''
plt.xlabel("Time[s]")
plt.xlim(0,A.time)
# plt.ylim(-0.25,0.4)
plt.ylabel("$\Theta(t)$[rad]")
plt.legend(loc='upper right',frameon=False)
plt.title('Comparison of Harmonic and Anharmonic')
plt.show()
'''