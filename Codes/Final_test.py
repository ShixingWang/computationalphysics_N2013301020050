# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 15:17:08 2016

@author: Bories

used for TEST!!!

"""

# import packages
import matplotlib.pyplot as plt
import numpy as np

n=15
steps=10000
T=0.010
randomOrder=True
'''n is the total number of amino acids; steps is the Monte Carlo simulation lenth; self.order is the list that records the types of the amino acids on each site; self.kT is the product of Boltzman constant and temperature; self.order is the kind of amino acids at each site of the protein chaim; self.J is the matrix recording the interaction energy between two animo acids; self.direction is the array recording eight nearest neighbor directions; self.position is the array recording the initial configuration; self.finalPosition is the array recording the final configuration'''
kT=T
# initialize the types of amino acid at each site on the chain. If randomOrder = True, the amino acids are chosen randomly. 
if randomOrder:
    order=np.random.random_integers(0,19,size=[n])
else:
    order=np.array(input('input the type order of the amino acids: '))
J=-np.random.rand(20,20)#第i个氨基酸和第j个之间的相互作用能, codes below makes it symmetric.
for i in range(20):
    for j in range(i):
        J[i][j]=J[j][i]
# define eight nearest directions 
direction=np.array([[1,1],[-1,1],[-1,-1],[1,-1]])
# define the initial configuration as a straight line 
        
def initConfig(n):
    position=[np.array([0,0])]
    for i in range(n-1):
        position.append(position[-1]+np.array([1,0]))
    position=np.array(position)
    return position#一个二维np.array
position=initConfig(n=10)
'''
# get the final configuration of the peotein.

def energy(configuration,order):
    E=0
    for i in range(len(configuration)-2):
        j=i+2
        while j < len(configuration):
            if distance(configuration[i],configuration[j])==1:
                E=E+J[order[i]][order[j]]
            j=j+1
    return E
        
def distance(a,b):
    a=np.array(a)
    b=np.array(b)
    c=a-b
    if len(c)==2:
        l=np.sqrt(c[0]**2+c[1]**2)
    else:
        l=None
    return l

def MonteCarlo(position,order,n,steps):
    ''''''n是总的氨基酸数目; steps是总共的蒙卡模拟时间. 'Positions' is a list (or maybe 2-d np.array) that stores every configuration at every step.''''''
    Positions=[position]
    Energies=[energy(configuration=position,order=order)]
    Lengths=[distance(position[0],position[-1])]
    Steps=[0]
    counter=0
    while counter < steps:
        randomNum=np.random.random_integers(0,n-1)
        if randomNum == 0 :
            randomDirection = np.random.random_integers(0,3)
            newPosition=Positions[-1][randomNum]+direction[randomDirection]
            if list(newPosition) in np.ndarray.tolist(Positions[-1]): # CHECK the type when debugging
                counter=counter+1
            else:
                if distance(newPosition,Positions[-1][randomNum+1])==1:
                    NewPosition=Positions[-1][:]
                    NewPosition[randomNum]=newPosition
                    NewLength=distance(NewPosition[0],NewPosition[-1])
                    NewEnergy=energy(configuration=NewPosition,order=order)                        
                    deltaEnergy=energy(configuration=NewPosition,order=order)-energy(configuration=Positions[-1],order=order)
                    if energy(NewPosition)<0:
                        Positions.append(NewPosition)
                        Energies.append(NewEnergy)
                        Lengths.append(NewLength)
                        counter=counter+1
                        Steps.append(counter)
                    else:
                        randomEnergy=np.random.rand()
                        if np.exp(-deltaEnergy/kT)>randomEnergy:
                            Positions.append(NewPosition)
                            Energies.append(NewEnergy)
                            Lengths.append(NewLength)
                            counter=counter+1
                            Steps.append(counter) 
                        else:
                            counter=counter+1
                else:
                    counter=counter+1
        elif randomNum == n-1 :
            randomDirection = np.random.random_integers(0,3)
            newPosition=Positions[-1][randomNum]+direction[randomDirection]
            if list(newPosition) in np.ndarray.tolist(Positions[-1]): # CHECK the type when debugging
                counter=counter+1
            else:
                if distance(newPosition,Positions[-1][randomNum-1])==1:
                    NewPosition=Positions[-1][:]
                    NewPosition[randomNum]=newPosition
                    NewLength=distance(NewPosition[0],NewPosition[-1])
                    NewEnergy=energy(configuration=NewPosition,order=order)                        
                    deltaEnergy=energy(configuration=NewPosition,order=order)-energy(configuration=Positions[-1],order=order)
                    if energy(NewPosition)<0:
                        Positions.append(NewPosition)
                        Energies.append(NewEnergy)
                        Lengths.append(NewLength)
                        counter=counter+1
                        Steps.append(counter)
                    else:
                        randomEnergy=np.random.rand()
                        if np.exp(-deltaEnergy/kT)>randomEnergy:
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
            newPosition=Positions[-1][randomNum]+direction[randomDirection]
            if list(newPosition) in np.ndarray.tolist(Positions[-1]): # CHECK the type when debugging
                counter=counter+1
            else:
                if distance(newPosition,Positions[-1][randomNum-1])==1 and distance(newPosition,Positions[-1][randomNum+1])==1:
                    NewPosition=Positions[-1][:]
                    NewPosition[randomNum]=newPosition
                    NewLength=distance(NewPosition[0],NewPosition[-1])
                    NewEnergy=energy(configuration=NewPosition,order=order)                        
                    deltaEnergy=energy(configuration=NewPosition,order=order)-energy(configuration=Positions[-1],order=order)
                    if energy(configuration=NewPosition,order=order)<0:
                        Positions.append(NewPosition)
                        Energies.append(NewEnergy)
                        Lengths.append(NewLength)
                        counter=counter+1
                        Steps.append(counter)
                    else:
                        randomEnergy=np.random.rand()
                        if np.exp(-deltaEnergy/kT)>randomEnergy:
                            Positions.append(NewPosition)
                            Energies.append(NewEnergy)
                            Lengths.append(NewLength)
                            counter=counter+1
                            Steps.append(counter) 
                        else:
                            counter=counter+1
                else:
                    counter=counter+1
    return Positions,Energies,Lengths,Steps,counter
Position=MonteCarlo(position=position,order=order,n=n,steps=steps)[0]
Energy=MonteCarlo(position=position,order=order,n=n,steps=steps)[1]
Length=MonteCarlo(position=position,order=order,n=n,steps=steps)[2]
Step=MonteCarlo(position=position,order=order,n=n,steps=steps)[3]
Counter=MonteCarlo(position=position,order=order,n=n,steps=steps)[4]
'''
print position



    
