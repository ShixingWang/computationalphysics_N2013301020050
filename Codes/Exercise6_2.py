import math
import matplotlib.pyplot as plt
# import modules
g=9.8
B2m=0.00004
y_zero=10000
a=0.0065
T0=300
alpha=2.5
# set constants
class cannon0:
    "the simplest model with no air drag, no air density variance, no probability distribution"
    # initialize variables    
    def __init__(self,v0,theta,yFinal=0):
        self.x0=0
        self.y0=0
        self.yFinal=yFinal
        self.v0=v0
        self.Theta=theta
        self.theta=theta*math.pi/180
        self.vx0=self.v0*math.cos(self.theta)
        self.vy0=self.v0*math.sin(self.theta)
        self.dt=0.01
        return None
    # external force other than gravity, no force in simplest case        
    def F(self,vx,vy,y=1):
        return 0,0
    # calculate the flying trajactory
    def fly(self):
        self.X=[self.x0]
        self.Y=[self.y0]
        self.Vx=[self.vx0]
        self.Vy=[self.vy0]
        self.T=[0]
        while not (self.Y[-1]<self.yFinal and self.Vy[-1]<0):
            newVx=self.Vx[-1]+self.F(vx=self.Vx[-1],vy=self.Vy[-1],y=self.Y[-1])[0]*self.dt
            newVy=self.Vy[-1]-g*self.dt+self.F(self.Vx[-1],self.Vy[-1])[1]*self.dt
            self.Vx.append(newVx)
            self.Vy.append(newVy)
            meanVx=0.5*(self.Vx[-1]+self.Vx[-2])
            meanVy=0.5*(self.Vy[-1]+self.Vy[-2])
#            meanV=math.sqrt(meanVx**2+meanVy**2) # not used in Cannon0 because there is no air drag
            newX=self.X[-1]+meanVx*self.dt
            newY=self.Y[-1]+meanVy*self.dt
            self.X.append(newX)
            self.Y.append(newY)
        # fix the final landing coordinate        
#        r=-self.Y[-2]/self.Y[-1]
        self.X[-1]=((self.Y[-2]-self.yFinal)*self.X[-1]+(self.yFinal-self.Y[-1])*self.X[-2])/(self.Y[-2]-self.Y[-1])
        self.Y[-1]=self.yFinal
        return 0
    # get the final distance shells can reach
    def distance(self):
        return self.X[-1]
    def height(self):
        return max(self.Y)
    # represent trajectory 
    def plot(self, color):
        plt.plot(self.X,self.Y,color,label="$%dm/s$,$%d\degree$, no air drag"%(self.v0,self.Theta))
        return 0
class cannon1(cannon0):
    "the second simplest model with no air drag under constant air density, no probability distribution"    
    # external force other than gravity        
    def F(self,vx,vy,y=1):
        vl=math.sqrt(vx**2+vy**2)
        self.Fx=-B2m*vx*vl
        self.Fy=-B2m*vy*vl
        return self.Fx,self.Fy
    def plot(self, color):
        plt.plot(self.X,self.Y,color,label="$%dm/s$,$%d\degree$, uniform air drag"%(self.v0,self.Theta))
        return 0
class cannon2(cannon0):
    "the model concerning ISOTHERMAL air density variance but no probability distribution"
    def F(self,vx,vy,x=1,y=1):
        vl=math.sqrt(vx**2+vy**2)
        self.Fx=-B2m*vx*vl*math.exp(-y/y_zero)
        self.Fy=-B2m*vy*vl*math.exp(-y/y_zero)
        return self.Fx,self.Fy
    def plot(self, color):
        plt.plot(self.X,self.Y,color,label="$%dm/s$,$%d\degree$, isothermal air drag"%(self.v0,self.Theta))
        return 0
class cannon3(cannon0):
    "the model concerning ADIABATIC air density variance but no probability distribution"    
    def F(self,vx,vy,y=1):
        vl=math.sqrt(vx**2+vy**2)
        self.Fx=-B2m*vx*vl*(1-a*y/T0)**alpha
        self.Fy=-B2m*vy*vl*(1-a*y/T0)**alpha
        return self.Fx,self.Fy
    def plot(self, color):
        plt.plot(self.X,self.Y,color,label="$%dm/s$,$%d\degree$, adiabatic air drag"%(self.v0,self.Theta))
        return 0

# select the angle casting the largest distance

Distance=[]
for i in range(90):
    A=cannon1(600,i)
    A.fly()
    newDistance=A.distance()
    Distance.append(newDistance)
maxDistance=max(Distance)
maxAngle=Distance.index(maxDistance)
print maxAngle

sub1=plt.subplot(221)
A=cannon0(600,45)
A.fly()
sub1.plot(A.X,A.Y,'r-',label='$45\degree$')
A1=cannon0(600,35)
A1.fly()
sub1.plot(A1.X,A1.Y,'r--',label='$35\degree$')
A2=cannon0(600,55)
A2.fly()
sub1.plot(A2.X,A2.Y,'r:',label='$55\degree$') 
sub1.set_title('No air drag')   
sub1.legend(loc="upper right",frameon=False)
plt.xlabel("Distance [m]")
plt.ylabel("Hieght [m]")  

sub2=plt.subplot(222)
B=cannon1(600,40)
B.fly()
sub2.plot(B.X,B.Y,'g-',label='$40\degree$')    
B1=cannon1(600,30)
B1.fly()
sub2.plot(B1.X,B1.Y,'g--',label='$30\degree$')
B2=cannon1(600,50)
B2.fly()
sub2.plot(B2.X,B2.Y,'g:',label='$50\degree$') 
sub2.set_title('Uniform Air Drag')
sub2.legend(loc="upper right",frameon=False)
plt.xlabel("Distance [m]")
plt.ylabel("Hieght [m]")  

sub3=plt.subplot(223)
C=cannon2(600,45)
C.fly()
sub3.plot(C.X,C.Y,'b-',label='$45\degree$')
C1=cannon2(600,35)
C1.fly()
sub3.plot(C1.X,C1.Y,'b--',label='$35\degree$')
C2=cannon2(600,55)
C2.fly()
sub3.plot(C2.X,C2.Y,'b:',label='$55\degree$') 
sub3.set_title('Isothermal Air Drag')
sub3.legend(loc="upper right",frameon=False)
plt.xlabel("Distance [m]")
plt.ylabel("Hieght [m]")  

sub4=plt.subplot(224)
D=cannon3(600,42)
D.fly()
sub4.plot(D.X,D.Y,'y-',label='$42\degree$')
D1=cannon3(600,32)
D1.fly()
sub4.plot(D1.X,D1.Y,'y--',label='$32\degree$')
D2=cannon3(600,52)
D2.fly()
sub4.plot(D2.X,D2.Y,'y:',label='$52\degree$') 
sub4.set_title('Adiabatic Air Drag')
sub4.legend(loc="upper right",frameon=False)


plt.xlabel("Distance [m]")
plt.ylabel("Hieght [m]")   
plt.show()

#print A.distance()
#print B.distance()
#print C.distance()
#print D.distance()