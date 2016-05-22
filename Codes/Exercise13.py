# -*- coding: utf-8 -*-
"""
Created on Sat May 21 21:48:44 2016

@author: 李尧
"""

from math import *
import matplotlib.pyplot as p
import mpl_toolkits.mplot3d
import numpy as np
class scalarfield():
    def inti(self,lx,ly,b1,b2,b3,b4):
        self.lx=lx
        self.ly=ly
        self.N=1
        self.v=[[0.0 for j in range(lx)] for i in range(ly)]
        self.innerboundary=[[None for j in range(lx)] for i in range(ly)]
        self.chargedensity=[[0 for j in range(lx)] for i in range(ly)]
        self.delta=1.0
        for i in range(ly):        
            self.v[0][i]=b1[i]
        for i in range(ly):
            self.v[lx-1][i]=b3[i]
        for i in range(lx-2):
            self.v[i+1][0]=b2[i+1]
        for i in range(lx-2):
            self.v[i+1][ly-1]=b4[i+1]
        return None
    def sor(self):
       delta=0.0
       a=2/(1+pi/self.lx)
       #a=1
       for i in range(self.lx-2):
           for j in range(self.ly-2):
               if self.innerboundary[i+1][j+1]==None:
                  deltav=(self.v[i][j+1]+self.v[i+2][j+1]+self.v[i+1][j]+self.v[i+1][j+2])/4-self.v[i+1][j+1]+self.chargedensity[i+1][j+1]
                  delta=delta+abs(deltav)
                  self.v[i+1][j+1]=self.v[i+1][j+1]+deltav*a
               else:
                  self.v[i+1][j+1]=self.innerboundary[i+1][j+1]
       self.delta=delta
       self.N=self.N+1
       return None
    def jacobirun(self):
        delta=0.0
        vi=[[1.0 for j in range(self.lx)] for i in range(self.ly)]
        for i in range(self.ly):        
            vi[i]=self.v[i]
        for i in range(self.lx-2):
           for j in range(self.ly-2):
               if self.innerboundary[i+1][j+1]==None:
                  delta=delta+abs((self.v[i][j+1]+self.v[i+2][j+1]+self.v[i+1][j]+self.v[i+1][j+2])/4-self.v[i+1][j+1]+self.chargedensity[i+1][j+1])
                  vi[i+1][j+1]=(self.v[i][j+1]+self.v[i+2][j+1]+self.v[i+1][j]+self.v[i+1][j+2])/4+self.chargedensity[i+1][j+1]
               else:
                  vi[i+1][j+1]=self.innerboundary[i+1][j+1]
        self.v=vi
        self.delta=delta
        self.N=self.N+1
        return None
    def setinnerboundary(self,inbd):
        self.innerboundary=inbd
        return None
    def setchargedensity(self,chargedensity):
        self.setchargedensity=chargedensity
        return None


m=50#input('m=')
n=m
u=scalarfield()
b1=[0.0 for i in range(m)]
b2=[0.0 for i in range(n)]
b3=[0.0 for i in range(m)]
b4=[0.0 for i in range(n)]
u.inti(m,n,b1,b2,b3,b4)
x,y=np.mgrid[0:m:1,0:n:1]
inbd=[[None for j in range(m)] for i in range(n)]
for i in range(n/2):
    inbd[m/4][i+m/4]=1.0
    inbd[3*m/4][i+m/4]=-1.0
    #inbd[i+m/4][m/4]=1.0
    #inbd[i+m/4][3*m/4]=1.0
u.setinnerboundary(inbd)
while u.delta>10**-13:
    #u.jacobi()
    u.sor()
print(u.N)
z=u.v
a=p.subplot(111,projection='3d')
a.plot_surface(x,y,z,rstride=2,cstride=1,cmap=p.cm.coolwarm,alpha=0.8)

p.show()