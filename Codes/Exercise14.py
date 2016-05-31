# import packages
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation 
# physical constants
c=1
r=1
k=1000

class wave:
    """Gaussian Initial Condition, Fixed Boundary Condition"""
    def __init__(self,x0=0.3,x1=0.7,length=1,time=30,dt=0.01):
        self.x0=x0
        self.x1=x1
        self.length=length
        self.time=time
        self.dt=dt
        self.dx=c*dt/r
        self.i=int(length/self.dx)+1
        self.n=time/dt
        self.X=np.linspace(0,length,self.i,endpoint=True)
        self.Y0=np.exp(-k*(self.X-x0)**2)+np.exp(-k*(self.X-x1)**2)
        return None
    def calculate(self):
        self.Y=[self.Y0]
        Y1=np.linspace(0,0,self.i)
        for cycle1 in range(self.i-2):
            Y1[cycle1+1]=2*(1-r**2)*self.Y0[cycle1+1]-self.Y0[cycle1+1]+r**2*(self.Y0[cycle1+2]+self.Y0[cycle1])
        self.Y.append(Y1)
        while not len(self.Y) > (self.n+1):
            newY=np.linspace(0,0,self.i)
            for cycle2 in range(self.i-2):
                newY[cycle2+1]=2*(1-r**2)*self.Y[-1][cycle2+1]-self.Y[-2][cycle2+1]+r**2*(self.Y[-1][cycle2+2]+self.Y[-1][cycle2])
            self.Y.append(newY)
        return None
    def plot(self,i):
        plt.plot(self.X,self.Y[i])
        return 0
    def movie(self):
        # New figure with white background
        fig = plt.figure(figsize=(6,6), facecolor='white')
        # New axis over the whole figure, no frame and a 1:1 aspect ratio
        ax = fig.add_axes([0,0,1,1], frameon=False, aspect=1)
        line, = ax.plot([], [], lw=2)
        def init():  
            line.set_data([], [])  
            return line,
        def animate(i):
            x = self.X
            y = self.Y[i]
            line.set_data(list(x), list(y))	  
            return line,
        anim1=animation.FuncAnimation(fig, animate, init_func=init, frames=3000, interval=30)
        plt.show()
        return 0

A=wave()
A.calculate()
#A.plot(0)
#print A.Y
#print type(A.Y[1])


# New figure with white background
fig = plt.figure(figsize=(6,6), facecolor='white')
# New axis over the whole figure, no frame and a 1:1 aspect ratio
ax = plt.axes(xlim=(0, 1), ylim=(-1, 1))
line, = ax.plot([], [], lw=2)
def init():  
    line.set_data([], [])  
    return line,
def animate(i):
    x = A.X
    y = A.Y[i]
    line.set_data(list(x), list(y))	  
    return line,
anim1=animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=10)
plt.show()
anim1.save('demoanimation.gif', writer='imagemagick', fps=4)
