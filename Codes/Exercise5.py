import matplotlib.pyplot as plt
import math
# import packle
import visual as vs
# import easygui

class population_growth:
    """
    the program for Problem 1.6 of Computational Physics
    """
    def __init__(self, N0, a, b, dt, time):
        self.N0=N0
        self.a=a
        self.b=b
        self.dt=dt
        self.time=time
        self.N=[self.N0]
        self.t=[0]
        self.analytic=[self.N0]
        self.timeAna=[0]        
        return None

    def __str__(self):
        message="The initial population is %f, the growth rate is %f and the death rate is%f" %(self.N0, self.a, self.b)
        return message

    def calculate(self):
        length=int(self.time/self.dt)
        for cycle in range(length):
            self.newN=self.N[cycle]+(self.a*self.N[cycle]-self.b*(self.N[cycle])**2)*self.dt
            self.newTime=self.t[cycle]+self.dt            
            self.N.append(self.newN)
            self.t.append(self.newTime)
        return 0

    def plot2D(self):
        plt.scatter(self.t, self.N, c='red',edgecolor='red',linewidth=0.5,label='Numerical',alpha=1)
        plt.xlabel("time[Year]")
        plt.ylabel("Population")
        plt.xlim(min(self.t),max(self.t))
        plt.xticks([min(self.t),0.8*min(self.t)+0.2*max(self.t),0.6*min(self.t)+0.4*max(self.t),0.4*min(self.t)+0.6*max(self.t),0.2*min(self.t)+0.8*max(self.t),max(self.t)])
        plt.ylim(0,1.1*max(self.N))
#        plt.show()
#        plt.savefig("PopulationGrowth")
        return 0
    
    def analytical(self):
        lengthAna=int(self.time/0.0001)        
        self.timeAna=[0]*lengthAna
        self.analytic=[self.N0]*lengthAna
        for cycle2 in range(lengthAna):
            self.timeAna[cycle2]=0.0001*cycle2
            self.analytic[cycle2]=(self.N0*self.a*math.exp(self.a*self.timeAna[cycle2]))/(self.a-self.b*self.N0+self.b*self.N0*math.exp(self.a*self.timeAna[cycle2]))
        plt.plot(self.timeAna,self.analytic,color='blue',linestyle='-',linewidth=1.5,label='Theoretical')        
        
    def plot3D(self):
        axis_length = 10.0
        xaxis = vs.arrow(pos = (-5, -5, 0), axis = (axis_length, 0, 0), shaftwidth = 0.01)
        yaxis = vs.arrow(pos = (-5, -5, 0), axis = (0, axis_length, 0), shaftwidth = 0.01)
        balls = []
        for (i, j) in zip(self.N, self.t):
            balls.append(vs.sphere(pos = ((j / self.time) * axis_length * 0.9- 4.9, (i / self.N) * axis_length * 0.9 - 4.9, 0), radius = 0.2, color = vs.color.red))
        xlabel = vs.label(text = "time[s]", pos = (5, -5, 0))
        ylabel = vs.label(text = "Population", pos = (-5, 5, 0))
        while 1:
            pass


plt.title("Population Growth")

p1=plt.subplot(131)            
pop=population_growth(100,10,0.05,0.001,3)
pop.calculate()
pop.plot2D()
pop.analytical()
      
p1.set_title("dt=0.001")
p1.legend(loc='right',frameon=False)
# ------------------------- 1st subplot above----------------------------------
p2=plt.subplot(132)            
pop=population_growth(100,10,0.05,0.01,3)
pop.calculate()
pop.plot2D()
pop.analytical()
      
p2.set_title("dt=0.01")
p2.legend(loc='right',frameon=False)
# ------------------------- 2nd subplot above----------------------------------
p3=plt.subplot(133)            
pop=population_growth(100,10,0.05,0.1,3)
pop.calculate()
pop.plot2D()
pop.analytical()
      
p3.set_title("dt=0.1")
p3.legend(loc='right',frameon=False)
# ------------------------- 3rd subplot above----------------------------------
plt.show()