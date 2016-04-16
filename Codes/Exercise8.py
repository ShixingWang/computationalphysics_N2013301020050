import math
import matplotlib.pyplot as plt
# import modules above
l=1
k=1
# define constants above
class pandulum:
    def __init__(self,alpha=1,x0=0.1,v0=0,time=5):
        self.alpha=alpha
        self.x0=x0
        self.v0=v0
        self.theta=math.asin(self.x0/l)
        self.omega=self.v0/l
        self.dt=0.1
        self.time=time
        return 0
    def sway(self):
        self.Theta=[self.theta]
        self.Omega=[self.omega]
        self.T=[0]
        while not self.T[-1]>self.time:
            newOmega=self.Omega[-1]-k*(self.Theta[-1])**self.alpha*self.dt
            newTheta=self.Theta[-1]+newOmega*self.dt
            newT=self.T[-1]+self.dt
            self.Omega.append(newOmega)
            self.Theta.append(newTheta)
            self.T.append(newT)
        return 0
    def plotTheta(self,color='red',linestyle='-'):
        plt.plot(self.T,self.Theta,color,linestyle,label='$\alpha=$%d,amplitude=%f'%(self.alpha,max(self.Theta)))
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
    