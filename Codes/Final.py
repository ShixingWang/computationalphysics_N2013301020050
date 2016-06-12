# import packages
import matplotlib.pyplot as plt
import numpy as np

class folding:
    def __init__(self,n=10,steps=10,T=10,randomOrder=True):
        '''n is the total number of amino acids; steps is the Monte Carlo simulation lenth; self.order is the list that records the types of the amino acids on each site.'''
        self.kT=T
        self.n=n
        self.steps=steps
        # 却定每一个位点上氨基酸的种类，若randomOrder为True，则随机选择
        if randomOrder:
            self.order=np.random.random_integers(1,20,size=[n])
        else:
            self.order=np.array(input('input the type order of the amino acids: '))
        self.J=[] #第i个氨基酸和第j个之间的相互作用能
        # 定义八个最近邻方向
        self.direction=np.array([[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]])
        # 定义初始位形
        self.position=self.initConfig(n=self.n)
        self.finalPosition=self.MonteCarlo(position=self.position,n=self.n,steps=self.steps)[-1]
        
    def initConfig(self,n):
        position=[np.array([0,0])]
        for i in range(n-1):
            position.append(position[-1]+np.array([1,0]))
        position=np.array(position)
        return position#一个二维np.array
        
    def MonteCarlo(self,position,n,steps):
        '''n是总的氨基酸数目; steps是总共的蒙卡模拟时间. 'Positions' is a list (or maybe 2-d np.array) that stores every configuration at every step.'''
        Positions=[position]
        Energies=[self.energy(configuration=position)]
        Lengths=[self.distance(position[0],position[-1])]
        Steps=[0]
        counter=0
        while len(Positions)<steps:
            randomNum=np.random.random_integers(0,n)
            if randomNum == 0 :
                randomDirection = np.random.random_integers(0,7)
                newPosition=Positions[-1][randomNum]+self.direction[randomDirection]
                if newPosition in Positions[-1]: # CHECK the type when debugging
                    counter=counter+1
                else:
                    if self.distance(newPosition,Positions[-1][randomNum+1])==1:
                        NewPosition=Positions[-1][:]
                        NewPosition[randomNum]=newPosition
                        NewLength=self.distance(NewPosition[0],NewPosition[-1])
                        NewEnergy=self.energy(NewPosition)                        
                        deltaEnergy=self.energy(NewPosition)-self.energy(Positions[-1])
                        if self.energy(NewPosition)<0:
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
            elif randomNum == n :
                randomDirection = np.random.random_integers(0,7)
                newPosition=Positions[-1][randomNum]+self.direction[randomDirection]
                if newPosition in Positions[-1]: # CHECK the type when debugging
                    counter=counter+1
                else:
                    if self.distance(newPosition,Positions[-1][randomNum-1])==1:
                        NewPosition=Positions[-1][:]
                        NewPosition[randomNum]=newPosition
                        NewLength=self.distance(NewPosition[0],NewPosition[-1])
                        NewEnergy=self.energy(NewPosition)                        
                        deltaEnergy=self.energy(NewPosition)-self.energy(Positions[-1])
                        if self.energy(NewPosition)<0:
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
                randomDirection = np.random.random_integers(0,7)
                newPosition=Positions[-1][randomNum]+self.direction[randomDirection]
                if newPosition in Positions[-1]: # CHECK the type when debugging
                    counter=counter+1
                else:
                    if self.distance(newPosition,Positions[-1][randomNum-1])==1 and self.distance(newPosition,Positions[-1][randomNum+1])==1:
                        NewPosition=Positions[-1][:]
                        NewPosition[randomNum]=newPosition
                        NewLength=self.distance(NewPosition[0],NewPosition[-1])
                        NewEnergy=self.energy(NewPosition)                        
                        deltaEnergy=self.energy(NewPosition)-self.energy(Positions[-1])
                        if self.energy(NewPosition)<0:
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

    def energy(self,configuration):
        E=0
        for i in range(len(configuration)-2):
            for j in range(len(configuration)-i-2):
                if self.distance(configuration[i],configuration[i+j+2])==1:
                    E=E+self.J[i][i+j+2]
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
    
        