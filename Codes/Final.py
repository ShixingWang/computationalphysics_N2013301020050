# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 16:45:53 2016

@author: Bories
"""

# import packages
import matplotlib.pyplot as plt
import numpy as np

class folding:
    def __init__(self,n=10,steps=10,T=10,randomOrder=True):
        '''n is the total number of amino acids; 
        steps is the Monte Carlo simulation lenth; 
        self.order is the list that records the types of the amino acids on each site;
        self.kT is the product of Boltzman constant and temperature;
        self.order is the kind of amino acids at each site of the protein chaim;
        self.J is the matrix recording the interaction energy between two animo acids;
        self.direction is the array recording eight nearest neighbor directions;
        self.position is the array recording the initial configuration;
        self.finalPosition is the array recording the final configuration
        '''
        self.kT=T
        self.n=n
        self.steps=steps
        # initialize the types of amino acid at each site on the chain. If randomOrder = True, the amino acids are chosen randomly. 
        if randomOrder:
            self.order=np.random.random_integers(0,19,size=[n])
        else:
            self.order=np.array(input('input the type order of the amino acids: '))
        self.J=np.random.rand(20,20)#第i个氨基酸和第j个之间的相互作用能, codes below make it symmetric.
        for i in range(20):
            for j in range(i):
                self.J[i][j]=self.J[j][i]
        # define eight nearest directions 
        self.direction=np.array([[1.,1.],[-1.,1.],[-1.,-1.],[1.,-1.]])
        # define the initial configuration as a straight line 
        self.position=self.initConfig(n=self.n)
        # get the final configuration of the peotein.
        self.finalPosition=self.MonteCarlo()[0][-1]
        
    def initConfig(self,n):
        position=[np.array([0.,0.])]
        for i in range(n-1):
            position.append(position[-1]+np.array([1.,0.]))
        position=np.array(position)
        return position#一个二维np.array
        
    def MonteCarlo(self):
        '''n是总的氨基酸数目; steps是总共的蒙卡模拟时间. 'Positions' is a list (or maybe 2-d np.array) that stores every configuration at every step.'''
        Positions=[self.position]
        Energies=[self.energy(configuration=self.position)]
        Lengths=[self.distance(self.position[0],self.position[-1])]
        Steps=[0]
        counter=0
        while counter < self.steps:
            randomNum=np.random.random_integers(0,self.n-1)
            if randomNum == 0 :
                randomDirection = np.random.random_integers(0,3)
                newPosition=Positions[-1][randomNum]+self.direction[randomDirection]
                if list(newPosition) in np.ndarray.tolist(Positions[-1]): # CHECK the type when debugging
                    counter=counter+1
                else:
                    if self.distance(newPosition,Positions[-1][randomNum+1])==1.:
                        NewPosition=Positions[-1][:]
                        NewPosition[randomNum]=newPosition
                        NewLength=self.distance(NewPosition[0],NewPosition[-1])
                        NewEnergy=self.energy(configuration=NewPosition)                        
                        deltaEnergy=self.energy(configuration=NewPosition)-self.energy(configuration=Positions[-1])
                        if deltaEnergy<0:
                            Positions.append(NewPosition)
                            Energies.append(NewEnergy)
                            Lengths.append(NewLength)
                            counter=counter+1
                            Steps.append(counter)
                        else:
                            randomEnergy=np.random.rand()
                            if np.exp(-deltaEnergy/self.kT)>randomEnergy:
                                Positions.append(NewPosition)
                                Energies.append(NewEnergy)
                                Lengths.append(NewLength)
                                counter=counter+1
                                Steps.append(counter) 
                            else:
                                counter=counter+1
                    else:
                        counter=counter+1
            elif randomNum == self.n-1 :
                randomDirection = np.random.random_integers(0,3)
                newPosition=Positions[-1][randomNum]+self.direction[randomDirection]
                if list(newPosition) in np.ndarray.tolist(Positions[-1]): # CHECK the type when debugging
                    counter=counter+1
                else:
                    if self.distance(newPosition,Positions[-1][randomNum-1])==1:
                        NewPosition=Positions[-1][:]
                        NewPosition[randomNum]=newPosition
                        NewLength=self.distance(NewPosition[0],NewPosition[-1])
                        NewEnergy=self.energy(configuration=NewPosition)                        
                        deltaEnergy=self.energy(configuration=NewPosition)-self.energy(configuration=Positions[-1])
                        if deltaEnergy<0:
                            Positions.append(NewPosition)
                            Energies.append(NewEnergy)
                            Lengths.append(NewLength)
                            counter=counter+1
                            Steps.append(counter)
                        else:
                            randomEnergy=np.random.rand()
                            if np.exp(-deltaEnergy/self.kT)>randomEnergy:
                                Positions.append(NewPosition)
                                Energies.append(NewEnergy)
                                Lengths.append(NewLength)
                                counter=counter+1
                                Steps.append(counter) 
                            else:
                                counter=counter+1
                    else:
                        counter=counter+1
            else:
                randomDirection = np.random.random_integers(0,3)
                newPosition=Positions[-1][randomNum]+self.direction[randomDirection]
                if list(newPosition) in np.ndarray.tolist(Positions[-1]): # CHECK the type when debugging
                    counter=counter+1
                else:
                    if self.distance(newPosition,Positions[-1][randomNum-1])==1 and self.distance(newPosition,Positions[-1][randomNum+1])==1:
                        NewPosition=Positions[-1][:]
                        NewPosition[randomNum]=newPosition
                        NewLength=self.distance(NewPosition[0],NewPosition[-1])
                        NewEnergy=self.energy(configuration=NewPosition)                        
                        deltaEnergy=self.energy(configuration=NewPosition)-self.energy(configuration=Positions[-1])
                        if deltaEnergy<0:
                            Positions.append(NewPosition)
                            Energies.append(NewEnergy)
                            Lengths.append(NewLength)
                            counter=counter+1
                            Steps.append(counter)
                        else:
                            randomEnergy=np.random.rand()
                            if np.exp(-deltaEnergy/self.kT)>randomEnergy:
                                Positions.append(NewPosition)
                                Energies.append(NewEnergy)
                                Lengths.append(NewLength)
                                counter=counter+1
                                Steps.append(counter) 
                            else:
                                counter=counter+1
                    else:
                        counter=counter+1
        return Positions,Energies,Lengths,Steps

    def energy(self,configuration):
        E=0
        for i in range(len(configuration)-2):
            j=i+2
            while j < len(configuration):
                if self.distance(configuration[i],configuration[j])==1:
                    E=E+self.J[self.order[i]][self.order[j]]
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
    
A=folding(steps=1000)
print A.finalPosition