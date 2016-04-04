> view this on ["作业部落"](https://www.zybuluo.com/ShixingWang/note/333176)
# Exercise 6： Crazy Cannon \_(:-↙∠)_

## Abstract
Projectile motion is one of the most common movement in daily life, and is said to have inspired Issac Newton of the gravitation laws.[\[1\]](https://en.wikipedia.org/wiki/Isaac_Newton) Strictly speaking, a projectile motion is defined as one under the action of gravity only,[\[2\]](https://en.wikipedia.org/wiki/Projectile_motion) while in reality modificaitons are in need due to the influence of air. Various conditions about the air drag force are discussed. (下面讲同一发射角度不同空气阻力对落点的改变)(下面讲对最远发射角度的改变) Finally a "stochastic cannon" with errors in the initial velocity, the firing angle and air drag force is presented. An algorithm is given to attain the best velocity and angle to hit the target.     
## Background     
### Projectile Motion and Modifications     
A projectile motion is defined as "a form of motion in which an object or particle (called a projectile) is thrown near the earth's surface, and it moves along a curved path under the action of gravity only."[\[2\]](https://en.wikipedia.org/wiki/Projectile_motion) This definition is an ideal model while in real life one can be assumed as a projectile motion if gravity takes the domineer significance. 

According to Newton's Law, $F=ma$, and the acceleration in horizentaal and vertical direction
$$\begin{array}{ll}a_x=0\\a_y=-g\end{array}$$
And since $a=\frac{d^2x}{dt^2}=\frac{d}{dt}(\frac{dx}{dt})=\frac{dv}{dt}$
$$\begin{array}{llll}v_x(t)=v_0\ cos(\theta)\\v_y(t)=v_0\ sin(\theta)-gt\\x(t)=v_0t\ cos(\theta)\\y(t)=v_0t\ sin(\theta)-\frac{1}{2}gt^2\end{array}$$
This has inspired us to convert two simultaneous second-order ordinary differential equation into four first-order equations by introducing velocity as a function of time.      
And if time is eliminated from the equations above we get
$$y(x)=tan(\theta)\cdot x-\frac{g}{2v_0^2cos^2(\theta)}x^2$$

When concerning about the air drag force, we assume that the impedence comes from the work needed to accelerate the air occupied in the volumn that the shell will sweep in unit time. So it is propotional to the density of air and the square of the velocity of the shell.
$$F_{drag}=-\frac{1}{2}C\rho Av^2$$

### Air Drag and Rifling     
As is mentioned above and will be discussed thoroughly in our codes, air drag force plays a critical role in the shells' trajactory. But engineers have come up ideas of rifling to fight against such impedence.  

![6_1](https://raw.githubusercontent.com/ShixingWang/computationalphysics_N2013301020050/master/Pictures/6_1.jpg)     

Rifling is a series of spiral line inside the pipe of fire guns like rifles and cannons.[\[3\]](https://en.wikipedia.org/wiki/Rifling) When the shells get out of the pipe pushed by the gunpowder at the end of the bore of a gun, the high temperarure will inflate the shell making it rub with the rifling and spin. Such spin motion will effectively reduce the air drag force.      
### Air Density Distribution     
In the first section we gave the form of air drag force under simple assumptions. Now we come to a stage a little more complex. The force is sill propotional to the density of air. However, the density of air is a decreaseing function of altitude.      
#### __Isothermal Condition__      
The simplest model is to treat the atmosphere as an ideal gas with constant temperature. For a thin air layer with area S and thickness dz, we have
$$\begin{array}{ll}p(z+dz)S+\rho gSdz=p(z)S\\pV=\rho RT\end{array}$$
And the solution: [\[4\]](http://www.amazon.com/Computational-Physics-Edition-Nicholas-Giordano/dp/0131469908) 
$$\begin{array}{ll}p(y)=p(0)e^{-mgy/k_BT}\\\rho=\rho_0e^{-y/y_0}\end{array}$$
where $y_0=k_BT/mg\approx1.0\times10^4m$, and $\rho_0$ is density at sea level.     
#### __Adiabatic Condition__     
The isothermal model is not quite realistic for it cannot explain the rapid temperature decrease over a small scale of altitude. Another model treats air as heat pool with very slow convection.  [\[4\]](http://www.amazon.com/Computational-Physics-Edition-Nicholas-Giordano/dp/0131469908)[\[5\]](https://en.wikipedia.org/wiki/Atmospheric_pressure#Altitude_variation)[\[6\]](https://en.wikipedia.org/wiki/Barometric_formula)      
$$\rho=\rho_0(1-\frac{ay}{T_0})^\alpha$$      
Both the isothermal and adiabatic condition gives the similar form modification of air drag force       
$$F^*_{drag}=\frac{\rho}{\rho_0}F_{drag}(y=0)$$     
### Coriolis Force

### Curvation of Earth
![6_2](https://raw.githubusercontent.com/ShixingWang/computationalphysics_N2013301020050/master/Pictures/6_2.jpg)
## Results
## Discussion: Main Features of the Codes
## Acknowlesgement
## Reference
1. Wikipedia contributors. "Isaac Newton." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 31 Mar. 2016. Web. 2 Apr. 2016.
2. Wikipedia contributors. "Projectile motion." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 5 Mar. 2016. Web. 2 Apr. 2016.
3. Wikipedia contributors. "Rifling." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 1 Apr. 2016. Web. 4 Apr. 2016.
4. Giodano, N.J., Nakanishi, H. Computational Physics. Tsinghua University Press, December 2007.
5. Wikipedia contributors. "Atmospheric pressure." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 31 Mar. 2016. Web. 4 Apr. 2016.
6. Wikipedia contributors. "Barometric formula." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 25 Jan. 2016. Web. 4 Apr. 2016.




