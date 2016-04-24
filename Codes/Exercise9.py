import math
import matplotlib.pyplot as plt
from visual import *
# import modules above
l=9.8
g=9.8
q=0.5
# define constants above
class Chaos:
    def __init__(self,Fd=1.2,OmegaD=2./3,alpha=1,theta0=0.2,omega0=0,time=100,dt=0.001):
        self.Fd=Fd
        self.OmegaD=OmegaD
        self.theta0=theta0
        self.omega0=omega0
        self.dt=dt
        self.time=time
        self.Theta=[self.theta0]
        self.Omega=[self.omega0]
        self.T=[0]
        return None
    def sway(self):
        while not self.T[-1]>self.time:
            newOmega=self.Omega[-1]+(-math.sin(self.Theta[-1])-q*self.Omega[-1]+self.Fd*math.sin(self.OmegaD*self.T[-1]))*self.dt
            self.Omega.append(newOmega)
            newTheta=self.Theta[-1]+newOmega*self.dt
            if newTheta<-math.pi:
                newTheta=newTheta+2*math.pi
            if newTheta>math.pi:
                newTheta=newTheta-2*math.pi
            self.Theta.append(newTheta)
            newT=self.T[-1]+self.dt
            self.T.append(newT)
        return 0
    def plotTheta(self,style='black',slogan=''):
        plt.title(r"$\theta$ v.s. Time")
        plt.xlabel('Time [s]')
        plt.ylabel(r'$\theta\quad [rad]$')
        plt.xlim(min(self.T),max(self.T))
        plt.ylim(-4,4)
        plt.yticks([-math.pi,-math.pi/2,0,math.pi/2,math.pi],[r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])
        plt.plot(self.T,self.Theta,style,label=slogan)
        return 0
    def plotPhase(self,color='black',slogan=''):
        plt.title("Phase Trajectory")
        plt.xlabel(r'$\theta$ [rad]')
        plt.ylabel(r'$\omega$ [$s^{-1}$]')
        plt.xlim(-4,4)
        plt.xticks([-math.pi,-math.pi/2,0,math.pi/2,math.pi],[r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])
        plt.scatter(self.Theta,self.Omega,s=0.01,c=color,label=slogan)
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
A=Chaos()
A.sway()
A.plotPhase()
plt.show()