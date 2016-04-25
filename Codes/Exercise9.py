import math
import matplotlib.pyplot as plt
from visual import *
import numpy as np
# import modules above
l=9.8
g=9.8
# define constants above
class Chaos:
    def __init__(self,Fd=1.2,OmegaD=2./3,q=0.5,theta0=0.2,omega0=0,time=1000,step=1000):
        self.Fd=Fd
        self.OmegaD=OmegaD
        self.theta0=theta0
        self.omega0=omega0
        self.step=step
        self.cycle=2*math.pi/OmegaD
        self.dt=self.cycle/step
        self.time=time
        self.Theta=[self.theta0]
        self.originTheta=[self.theta0]
        self.Omega=[self.omega0]
        self.T=[0]
        self.q=q
        return None
    def sway(self):
        while not self.T[-1]>self.time:
            newOmega=self.Omega[-1]+(-math.sin(self.Theta[-1])-self.q*self.Omega[-1]+self.Fd*math.sin(self.OmegaD*self.T[-1]))*self.dt
            self.Omega.append(newOmega)
            newTheta=self.Theta[-1]+newOmega*self.dt
            self.originTheta.append(newTheta)
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
        plt.scatter(self.Theta,self.Omega,s=0.5,c=color,label=slogan)
        return 0        
    def PoincareSection(self,init,color,slogan):
        "init is a value from zero to one"
        n=int(self.time//self.cycle)
        PoincareTheta=[]
        PoincareOmega=[]
        for i in range(n):
            PoincareTheta.append(self.Theta[int((i+init)*self.step)])
            PoincareOmega.append(self.Omega[int((i+init)*self.step)])
        plt.scatter(PoincareTheta,PoincareOmega,s=0.5,c=color,label=slogan)
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

# Bifurcation Diagram
# F_D is just Fd in class Chaos, frequency is just OmegaD, frinction is just q
# start of bifurcation diagram
def bifurcation(init=0,F_D=1.2,frequency=2./3,friction=0.5,color='black',slogan=''):
    B=Chaos(Fd=F_D,OmegaD=frequency,q=friction,time=400*2*math.pi/frequency,)
    B.sway()
    bifurcationTheta=[]
    for i in range(100):
        bifurcationTheta.append(B.Theta[(300+i+init)*B.step])
    bifurcationFd=[F_D]*len(bifurcationTheta)   
    return (bifurcationFd,bifurcationTheta)
# bifurcation diagram for various OmegaD
'''
fd=[]
theta=[]
for i1 in np.arange(1.3,1.80,0.005):
    som=bifurcation(F_D=i1,frequency=1./2)
    fd.extend(som[0])
    theta.extend(som[1])
plt.ylim(1,3)
plt.subplot(221)
plt.scatter(fd,theta,s=0.1,c='black',label=r'$\Omega_D=1/2$')
plt.legend(loc='upper right',frameon=False)
# end of bifurcation diagram


fd=[]
theta=[]
for i2 in np.arange(1.3,1.48,0.001):
    som=bifurcation(F_D=i2,frequency=2./3)
    fd.extend(som[0])
    theta.extend(som[1])
plt.ylim(1,3)
plt.subplot(222)
plt.scatter(fd,theta,s=0.1,c='black',label=r'$\Omega_D=2/3$')
plt.legend(loc='upper right',frameon=False)


fd=[]
theta=[]
for i3 in np.arange(1.8,3.0,0.005):
    som=bifurcation(F_D=i3,frequency=1.)
    fd.extend(som[0])
    theta.extend(som[1])
plt.ylim(1,3)
plt.subplot(223)
plt.scatter(fd,theta,s=0.1,c='black',label=r'$\Omega_D=1$')
plt.legend(loc='upper right',frameon=False)


fd=[]
theta=[]
for i4 in np.arange(1.5,3.,0.01):
    som=bifurcation(F_D=i4,frequency=4./3)
    fd.extend(som[0])
    theta.extend(som[1])
plt.subplot(224)
plt.scatter(fd,theta,s=0.1,c='black',label=r'$\Omega_D=4/3$')
plt.legend(loc='upper right',frameon=False)
'''
# bifurcation diagram for various q
'''
fd=[]
theta=[]
for i1 in np.arange(1.3,1.6,0.005):
    som=bifurcation(F_D=i1,friction=0.4)
    fd.extend(som[0])
    theta.extend(som[1])
plt.ylim(1,3)
plt.subplot(221)
plt.scatter(fd,theta,s=0.1,c='black',label=r'$q=0.4$')
plt.legend(loc='upper right',frameon=False)
# end of bifurcation diagram


fd=[]
theta=[]
for i2 in np.arange(1.3,1.48,0.005):
    som=bifurcation(F_D=i2,friction=0.1)
    fd.extend(som[0])
    theta.extend(som[1])
plt.ylim(1,3)
plt.subplot(222)
plt.scatter(fd,theta,s=0.1,c='black',label=r'$q=0.6$')
plt.legend(loc='upper right',frameon=False)
'''
'''
fd=[]
theta=[]
for i3 in np.arange(1.3,1.60,0.005):
    som=bifurcation(F_D=i3,friction=0.1)
    fd.extend(som[0])
    theta.extend(som[1])
plt.ylim(1,3)
plt.subplot(223)
plt.scatter(fd,theta,s=0.1,c='black',label=r'$q=0.1$')
plt.legend(loc='upper right',frameon=False)


fd=[]
theta=[]
for i4 in np.arange(1.6.,2.6,0.01):
    som=bifurcation(F_D=i4,friction=1.)
    fd.extend(som[0])
    theta.extend(som[1])
plt.subplot(224)
plt.scatter(fd,theta,s=0.1,c='black',label=r'$q=1$')
plt.legend(loc='upper right',frameon=False)
'''

# Figure 9_2
'''
A=Chaos(time=10000,step=1000)
A.sway()
plt.title("Poincare Section")
plt.subplot(221)
A.PoincareSection(init=0,color='b',slogan=r'$t\approx 2\pi n/\Omega_D$')
plt.xlabel(r'$\theta$ [rad]')
plt.ylabel(r'$\omega$ [$s^{-1}$]')
plt.xlim(-4,4)
plt.xticks([-math.pi,-math.pi/2,0,math.pi/2,math.pi],[r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])
plt.legend(loc='upper right',frameon=False)
plt.subplot(222)
A.PoincareSection(init=0.125,color='r',slogan=r'$t\approx 2\pi n/\Omega_D+\pi/4$')
plt.xlabel(r'$\theta$ [rad]')
plt.ylabel(r'$\omega$ [$s^{-1}$]')
plt.xlim(-4,4)
plt.xticks([-math.pi,-math.pi/2,0,math.pi/2,math.pi],[r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])
plt.legend(loc='upper right',frameon=False)
plt.subplot(223)
A.PoincareSection(init=0.25,color='b',slogan=r'$t\approx 2\pi n/\Omega_D+\pi/2$')
plt.xlabel(r'$\theta$ [rad]')
plt.ylabel(r'$\omega$ [$s^{-1}$]')
plt.xlim(-4,4)
plt.xticks([-math.pi,-math.pi/2,0,math.pi/2,math.pi],[r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])
plt.legend(loc='upper right',frameon=False)
plt.subplot(224)
A.PoincareSection(init=0.375,color='g',slogan=r'$t\approx 2\pi n/\Omega_D+3\pi/4$')
plt.xlabel(r'$\theta$ [rad]')
plt.ylabel(r'$\omega$ [$s^{-1}$]')
plt.xlim(-4,4)
plt.xticks([-math.pi,-math.pi/2,0,math.pi/2,math.pi],[r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])
plt.legend(loc='upper right',frameon=False)
plt.show()
'''
# Figure 9_3
'''
A=Chaos(time=10000,step=1000)
A.sway()
plt.title("Poincare Section")
A.PoincareSection(init=0,color='b',slogan=r'$t\approx 2\pi n/\Omega_D$')
#A.PoincareSection(init=0.125,color='r',slogan=r'$t\approx 2\pi n/\Omega_D+\pi/4$')
#A.PoincareSection(init=0.25,color='b',slogan=r'$t\approx 2\pi n/\Omega_D+\pi/2$')
#A.PoincareSection(init=0.375,color='g',slogan=r'$t\approx 2\pi n/\Omega_D+3\pi/4$')
plt.xlabel(r'$\theta$ [rad]')
plt.ylabel(r'$\omega$ [$s^{-1}$]')
plt.xlim(-4,4)
plt.xticks([-math.pi,-math.pi/2,0,math.pi/2,math.pi],[r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])
plt.legend(loc='upper right',frameon=False)
plt.show()
'''