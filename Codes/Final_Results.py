# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 16:45:53 2016

@author: Bories
"""

# import packages
import matplotlib.pyplot as plt
import numpy as np

'''
J=np.array([[0. for cycle1 in range(20)] for cycle2 in range(20)])


J=2*np.random.random_integers(0,1,size=(20,20))-1
for cycle1 in range(20):
    for cycle2 in range(cycle1):
        J[cycle1][cycle2]=J[cycle2][cycle1]
'''

J=2*np.random.rand(20,20)-4
for cycle1 in range(20):
    for cycle2 in range(cycle1):
        J[cycle1][cycle2]=J[cycle2][cycle1]
order=np.random.random_integers(0,19,size=[15])

class folding:
    def __init__(self,n=15,steps=5*10**5,T=10,randomOrder=True):
        '''n is the total number of amino acids; 
        steps is the Monte Carlo simulation lenth; 
        self.order is the list that records the types of the amino acids on each site;
        self.kT is the product of Boltzman constant and temperature;
        self.order is the kind of amino acids at each site of the protein chaim;
        self.direction is the array recording eight nearest neighbor directions;
        self.position is the array recording the initial configuration;
        self.finalPosition is the array recording the final configuration
        '''
        self.kT=T
        self.n=n
        self.steps=steps
        # define eight nearest directions 
        self.direction=np.array([[1.,1.],[-1.,1.],[-1.,-1.],[1.,-1.]])
        # define the initial configuration as a straight line 
        self.position=self.initConfig(n=self.n)
        # get the final configuration of the peotein.
#        self.finalPosition=self.MonteCarlo()[0][-1]
#        self.Energies=self.MonteCarlo()[1]
#        self.Lengths=self.MonteCarlo()[2]
#        self.Steps=self.MonteCarlo()[3]
        
    def initConfig(self,n):
        position=[np.array([0.,0.])]
        for i in range(n-1):
            position.append(position[-1]+np.array([1.,0.]))
        position=np.array(position)
        return position #一个二维np.array
        
    def MonteCarlo(self):
        '''n是总的氨基酸数目; steps是总共的蒙卡模拟时间. 'Positions' is a list (or maybe 2-d np.array) that stores every configuration at every step.'''
        self.Positions=[self.position]
        self.Energies=[self.energy(configuration=self.position)]
        self.Lengths=[self.distance(self.position[0],self.position[-1])]
        self.Steps=[0]
        self.counter=0
        while self.counter < self.steps:
            randomNum=np.random.random_integers(0,self.n-1)
            if randomNum == 0 :
                randomDirection = np.random.random_integers(0,3)
                newPosition=self.Positions[-1][randomNum]+self.direction[randomDirection]
                if list(newPosition) in np.ndarray.tolist(self.Positions[-1]): # CHECK the type when debugging
                    self.counter=self.counter+1
                else:
                    if self.distance(newPosition,self.Positions[-1][randomNum+1])==1.:
                        NewPosition=self.Positions[-1][:]
                        NewPosition[randomNum]=newPosition
                        NewLength=self.distance(NewPosition[0],NewPosition[-1])
                        NewEnergy=self.energy(configuration=NewPosition)                        
                        deltaEnergy=self.energy(configuration=NewPosition)-self.energy(configuration=self.Positions[-1])
                        if self.energy(NewPosition)<0:
                            self.Positions.append(NewPosition)
                            self.Energies.append(NewEnergy)
                            self.Lengths.append(NewLength)
                            self.counter=self.counter+1
                            self.Steps.append(self.counter)
                        else:
                            randomEnergy=np.random.rand()
                            if np.exp(-deltaEnergy/self.kT)>randomEnergy:
                                self.Positions.append(NewPosition)
                                self.Energies.append(NewEnergy)
                                self.Lengths.append(NewLength)
                                self.counter=self.counter+1
                                self.Steps.append(self.counter) 
                            else:
                                self.counter=self.counter+1
                    else:
                        self.counter=self.counter+1
            elif randomNum == self.n-1 :
                randomDirection = np.random.random_integers(0,3)
                newPosition=self.Positions[-1][randomNum]+self.direction[randomDirection]
                if list(newPosition) in np.ndarray.tolist(self.Positions[-1]): # CHECK the type when debugging
                    self.counter=self.counter+1
                else:
                    if self.distance(newPosition,self.Positions[-1][randomNum-1])==1:
                        NewPosition=self.Positions[-1][:]
                        NewPosition[randomNum]=newPosition
                        NewLength=self.distance(NewPosition[0],NewPosition[-1])
                        NewEnergy=self.energy(configuration=NewPosition)                        
                        deltaEnergy=self.energy(configuration=NewPosition)-self.energy(configuration=self.Positions[-1])
                        if self.energy(NewPosition)<0:
                            self.Positions.append(NewPosition)
                            self.Energies.append(NewEnergy)
                            self.Lengths.append(NewLength)
                            self.counter=self.counter+1
                            self.Steps.append(self.counter)
                        else:
                            randomEnergy=np.random.rand()
                            if np.exp(-deltaEnergy/self.kT)>randomEnergy:
                                self.Positions.append(NewPosition)
                                self.Energies.append(NewEnergy)
                                self.Lengths.append(NewLength)
                                self.counter=self.counter+1
                                self.Steps.append(self.counter) 
                            else:
                                self.counter=self.counter+1
                    else:
                        self.counter=self.counter+1
            else:
                randomDirection = np.random.random_integers(0,3)
                newPosition=self.Positions[-1][randomNum]+self.direction[randomDirection]
                if list(newPosition) in np.ndarray.tolist(self.Positions[-1]): # CHECK the type when debugging
                    self.counter=self.counter+1
                else:
                    if self.distance(newPosition,self.Positions[-1][randomNum-1])==1 and self.distance(newPosition,self.Positions[-1][randomNum+1])==1:
                        NewPosition=self.Positions[-1][:]
                        NewPosition[randomNum]=newPosition
                        NewLength=self.distance(NewPosition[0],NewPosition[-1])
                        NewEnergy=self.energy(configuration=NewPosition)                        
                        deltaEnergy=self.energy(configuration=NewPosition)-self.energy(configuration=self.Positions[-1])
                        if self.energy(configuration=NewPosition)<0:
                            self.Positions.append(NewPosition)
                            self.Energies.append(NewEnergy)
                            self.Lengths.append(NewLength)
                            self.counter=self.counter+1
                            self.Steps.append(self.counter)
                        else:
                            randomEnergy=np.random.rand()
                            if np.exp(-deltaEnergy/self.kT)>randomEnergy:
                                self.Positions.append(NewPosition)
                                self.Energies.append(NewEnergy)
                                self.Lengths.append(NewLength)
                                self.counter=self.counter+1
                                self.Steps.append(self.counter) 
                            else:
                                self.counter=self.counter+1
                    else:
                        self.counter=self.counter+1
        return None

    def energy(self,configuration):
        E=0
        for i in range(len(configuration)-2):
            j=i+2
            while j < len(configuration):
                if self.distance(configuration[i],configuration[j])==1:
                    E=E+J[order[i]][order[j]]
                j=j+1
        return E
        
    def distance(self,a,b):
        a=np.array(a)
        b=np.array(b)
        c=a-b
        if len(c)==2:
            l=np.sqrt(c[0]**2+c[1]**2)
        else:
            l=None
        return l

A=folding(steps=500000,T=1)
A.MonteCarlo()

plt.ylim(-30,10)
plt.xticks([0, 100000, 200000, 300000, 400000, 500000],
       [r'0', r'1', r'2', r'3', r'4', r'5'])
plt.plot(A.Steps,A.Energies)