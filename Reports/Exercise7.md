
> View this in [Github](https://github.com/ShixingWang/computationalphysics_N2013301020050/blob/master/Reports/Exercise7.md).    
> View this in ["作业部落"](https://www.zybuluo.com/ShixingWang/note/339854)

# Exercise 7: Backspin of Baseball and 3D Cannon Shell

 __王世兴__     
 __2013301020050__      

> + Problem 2.19: Backspin of Baseball      
> + Visualize the cannon shell or baseball with VPython     

## Abstract      
Baseball is a sport of great interest for physics for its appropriately complexity of combining the elastic dynamics of bats, fluid dynamics of the ball and so on. [\[1\]](http://www.amazon.com/Physics-Baseball-Robert-Kemp-Adair/dp/0060084367) VPython has been introduced in early exercises to visualize results. In the report a discussion of the backspin of the baseball is presented as level 1 and an emendation of [Exercise 6](https://www.zybuluo.com/ShixingWang/note/333176) [2] concerning Coriolis effect is made, with 3D plot attribute inside the module realized with VPython.           
## Background      
### Bernoulli's principle and Magnus Effect      
Bernoulli's principle states that an increase in the speed of a fluid occurs simultaneously with a decrease in pressure or a decrease in the fluid's potential energy. [\[3\]](https://en.wikipedia.org/wiki/Bernoulli%27s_principle) The principle is named after Daniel Bernoulli who published it in his book Hydrodynamica in 1738. [\[4\]](http://global.britannica.com/biography/Daniel-Bernoulli#ref200813) This principle is often demonstrated as the following equation
$$p+\frac{1}{2}\rho V^2+\rho g h = const.$$
But we should be careful since this equation is based on the conseravtion of mechanical energy, thus is valid only when fluid of interest is inviscid and uncompressable.

Now we consider a special case of such principle, a spinning in a fluid.      

![7_1](https://raw.githubusercontent.com/ShixingWang/computationalphysics_N2013301020050/master/Pictures/7_1.png)       
Magnus Effect [\[5\]](https://en.wikipedia.org/wiki/Magnus_effect)

In terms of ball games, topspin is defined as spin about an axis perpendicular to the direction of travel, where the top surface of the ball is moving forward with the spin. Under the Magnus effect, topspin produces a downward swerve of a moving ball, greater than would be produced by gravity alone, and backspin has the opposite effect. [\[5\]](https://en.wikipedia.org/wiki/Magnus_effect)

Several ways can help comprehend the mechanism. First, the back spin makes the air below flow with a lower velocity than the air above, thus a pressure variance is made. Also, the faster the air moves, the more likely turbulent flow forms, making an extremely low pressure above the ball, making it fly higher and longer.

Further research reveals that under ordinary cases, the force caused by Magnus Effect can be expressed as
$$\vec F_{Magnus}=S_0\vec\omega\times \vec v$$
In the backspin cases, since the spin vector is perpendicular to the plane of the gravity and the velocity vector, no Magnus Effect is shown in this direction, the form of force becomes 
$$\begin{array}{ll}F_x=-\frac{S_0\omega v_y}{m}\\F_y=\frac{S_0\omega v_x}{m}\end{array}$$

### Air Drag as a Function of Velocity       
In the last program we have assumed that the air drag is propotional to the square of velocity in the form $F=-B_2v^2/m$. However, in realistic cases the drag coefficient is a function of the velocity. At low sppeds, the coefficient is close to 1/2, However as the speeds increases, is drops substaintially. As an approximation we use the analytical function
$$\frac{B_2}{m}=0.0039+\frac{0.0058}{1+e^{(v-v_d)/\Delta}}$$
where $v_d=35m/s$ and $\Delta=5m/s$, the numbers above are in the SI unit.
## Results
### Level 1: Problem 2.19
### Level 2: Visualization
## Discussion

## Reference     
+ [1] Adair, R.K. The Physics of Baseball. Harpercollins. Jan, 1990

+ [2] Shixing Wang. Exercise 6: Cannon Shell. Github, https://github.com/ShixingWang/computationalphysics_N2013301020050/blob/master/Reports/Exercise6.md, April 10, 2016

+ [3] Wikipedia contributors. "Bernoulli's principle." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 31 Mar. 2016. Web. 10 Apr. 2016.

+ [4] "Hydrodynamica". Britannica Online Encyclopedia. Retrieved 2008-10-30.

+ [5] Wikipedia contributors. "Magnus effect." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 16 Jan. 2016. Web. 10 Apr. 2016.