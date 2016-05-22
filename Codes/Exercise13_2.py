import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

class Jacobi:
    def __init__(self,L=30):
        self.L=L
        self.i=range(0,L,1)
        self.j=range(0,L,1)
        self.V=[[0. for cycle001 in self.i] for cycle002 in self.j]
        for cycle01 in range(int(L/3.),int(2*L/3.),1):
            self.V[int(L/3.)][cycle01]=1.
        for cycle02 in range(int(L/3.),int(2*L/3.),1):
            self.V[int(2*L/3.)][cycle02]=-1.        
        self.deltaV=1
        self.Nite=0
        self.newV=[[0. for cycle001 in self.i] for cycle002 in self.j]
        for cycle03 in range(int(L/3.),int(2*L/3.),1):
            self.newV[int(L/3.)][cycle03]=1.
        for cycle04 in range(int(L/3.),int(2*L/3.),1):
            self.newV[int(2*L/3.)][cycle04]=-1.  
        return None
    def calculate(self):
        iterate=0
        while self.deltaV > 0.000000000001:
            for cycle1 in self.i:
                for cycle2 in self.j:
                    if cycle1==0 or cycle1==int(self.L/3.)-1 or cycle1==int(2*self.L/3.)-1 or cycle1==int(self.L*1.)-1 or cycle2==0 or cycle2==int(self.L*1.)-1:
                        self.newV[cycle1][cycle2]=self.V[cycle1][cycle2]                        
                        iterate=iterate+abs(self.newV[cycle1][cycle2]-self.V[cycle1][cycle2])
                    else:
                        self.newV[cycle1][cycle2]=(self.V[cycle1-1][cycle2-1]+self.V[cycle1-1][cycle2+1]+self.V[cycle1+1][cycle2-1]+self.V[cycle1+1][cycle2+1])/4
                        iterate=iterate
                self.deltaV=iterate
                self.V=self.newV
                self.Nite=self.Nite+1
        return None

    def plot(self):
        x=np.linspace(-1,1,self.L)
        y=np.linspace(-1,1,self.L)
        X,Y=np.meshgrid(x,y)
        fig=plt.figure()
        ax=Axes3D(fig)
        ax.plot_surface(X, Y, self.V, rstride=5, cstride=5, cmap='hot')

A=Jacobi(60)
A.calculate()
print A.Nite
A.plot()