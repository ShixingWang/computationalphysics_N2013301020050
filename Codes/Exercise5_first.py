import matplotlib.pyplot as plt
import packle
import visual as vs
import easygui

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
        return None

    def __str__(self):
        message="The initial population is %f, the growth rate is %f and the death rate is%f" %(self.N0, self.a, self.b)
        return message

    def calculate(self):
        self.N=[self.N0]
        self.t=[0]
        length=int(self.time/self.dt)
        for cycle in range(length):
            newN=self.N[cycle]+(self.a*self.N[cycle]-self.b*(self.N[cycle])^2)*self.dt
            newTime=self.t[cycle]+self.dt            
            self.N.append(newN)
            self.t.append(newTime)

    def plot2D(self):
        plt.plot(self.T, self.n_uranium, '-*')
        plt.title("Population Growth")
        plt.xlabel("time[s]")
        plt.ylabel("Population")
        plt.show()
        plt.savefig("PopulationGrowth")
        
    def plot3D(self):
        axis_length = 10.0
        xaxis = vs.arrow(pos = (-5, -5, 0), axis = (axis_length, 0, 0), shaftwidth = 0.01)
        yaxis = vs.arrow(pos = (-5, -5, 0), axis = (0, axis_length, 0), shaftwidth = 0.01)
        balls = []
        for (i, j) in zip(self.n_uranium, self.T):
            balls.append(vs.sphere(pos = ((j / self.time) * axis_length * 0.9- 4.9, (i / self.N) * axis_length * 0.9 - 4.9, 0), radius = 0.2, color = vs.color.red))
        xlabel = vs.label(text = "time[s]", pos = (5, -5, 0))
        ylabel = vs.label(text = "Population", pos = (-5, 5, 0))
        while 1:
            pass
            
        