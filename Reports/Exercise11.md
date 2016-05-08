> View this in [Github](https://github.com/ShixingWang/computationalphysics_N2013301020050/blob/master/Reports/Exercise11.md)         
> View this in ["作业部落"](https://www.zybuluo.com/ShixingWang/note/369774)

# Exercise 11: Precession versus Eccentricity

---

__王世兴__
__2013301020050__

---

> __Problem 4.11__          
> Investigate how the precession of the perihelion of a planet's orbit due to general relativity varies as a function of the eccentricity of the orbit. Study the precession of different elliptical orbits with different eccentricities, but with the same value of the perihelion. Let the perihelion have the same value as for Mercury, so that you can compare it with the results shown in this section.

---

## Abstract
## Background

### Precession of the Perihelion of Mercury

Under Newtonian physics, a two-body system consisting of a lone object orbiting a spherical mass would trace out an ellipse with the spherical mass at a focus. The point of closest approach, called the periapsis (or, because the central body in the Solar System is the Sun, __perihelion__), is fixed. A number of effects in the Solar System cause the perihelia of planets to precess (rotate) around the Sun. The principal cause is the presence of other planets which perturb one another's orbit. Another (much less significant) effect is solar oblateness.

Mercury deviates from the precession predicted from these Newtonian effects. A number of ad hoc and ultimately unsuccessful solutions were proposed, but they tended to introduce more problems. In general relativity, this remaining precession, or change of orientation of the orbital ellipse within its orbital plane, is explained by gravitation being mediated by the curvature of spacetime. Einstein showed that general relativity[2] agrees closely with the observed amount of perihelion shift. This was a powerful factor motivating the adoption of general relativity.

The total observed precession of Mercury is 574.10±0.65 arc-seconds per century[6] relative to the inertial ICFR. This precession can be attributed to the following causes:

The correction by 42.98" is 3/2 multiple of classical prediction with PPN parameters $\gamma=\beta=0.[8]$

Thus the effect can be fully explained by general relativity. More recent calculations based on more precise measurements have not materially changed the situation.



In general relativity the perihelion shift σ, expressed in radians per revolution, is approximately given by:[12]

$$\sigma=\frac{24\pi^3L^2}{T^2c^2(1-e^2)}$$

where L is the semi-major axis, T is the orbital period, c is the speed of light, and e is the orbital eccentricity.
## Main Features of the Codes

* __Object-Oriented Manner__       
    We defined a class `Lorenz` to include the initialization of parameters, calculation of the differential equations, display of phase plots and 3D animation. This is extra conventient when we change the parameters and repeat the same processes. 

- __Only One Cycle__       
    To obtain the attractor in chaos phemonenon, we need to get two of the coordinates when the third is zero. This means judging and cycle structure is inevitable in the program, which is a terrible time consumer. We solve this problem by combining choosing points for the attractor plot with solving differential equations. In this way can we use only one cycle to give all the plots needed, while the drawback is also obvious that this program may take more memory.

* __Inner Product to Find Perihelion__      
    Unlike the trajectory in polar coordinates where we can easily find the perihelion as the point at which the differential of radius about angle is zero, we recognize the perihelion by the fact that as perihelion the position vector is orthogonal to the velocity vector.

* __Errorbar Plot__        
    Since every precession rate is obtained by fitting the curve of anglar shift versus time, there are errors in these values. So we plotted the errorbar plot in Figure 11.4. However, since the fine linearity of the data the error bar is too short to be seen.

* __MATLAB Curve Fitting__
    MATLAB is a commercial software with powerful tools to fit almost all kinds of curves. Here we use a custome equation obtained in the `Result` section to get a relatively good fit.

## Results

### Consisitence with the Results from Textbook

To check the correctness of our codes we choose the same parameters as those in the text book and plotted the figure of the trajectory of the "Mercury" when $\alpha$=0.01. 

![11_1](https://raw.githubusercontent.com/ShixingWang/computationalphysics_N2013301020050/master/Pictures/11_1.png)      
__Figure 11.1__ Simulated orbit of Mercuryorniting the Sun, with $\alpha$=0.01, the time step 0.0001 yr

Then we change $\alpha$ to be 0.0008 and obtain the scatter plot of the precession angle of the  perihelion versus time in Figure 11.2

![11_2](https://raw.githubusercontent.com/ShixingWang/computationalphysics_N2013301020050/master/Pictures/11_2.png)      
__Figure 11.2__ Precession of the axis of Mercury's orbit as a function of time, for $\alpha$=0.0008 and time step of 0.0001 yr

There is minor inconsistence between the result here and that in the textbook. Since we used the semimajor axis and eccentricity to calculate the perihelion and we have no idea what value the textbook uses for this parameter, we assume that this accounts for the difference.

### Trajectories for Different Eccentricity

For interest we plot the trajectories under different eccentricities keeping the length of the perihelion the same.

![11_3](https://raw.githubusercontent.com/ShixingWang/computationalphysics_N2013301020050/master/Pictures/11_3.png)      
__Figure 11.3__ Precession of the axis of Mercury's orbit as a function of time, for $\alpha$ equals 0.0008 and 0.01 respectively, and time step of 0.0001 yr

### Precession Rate as a Function of Eccentricity

Here we define the __precession rate__ as the angle deviation of the semiminor axis of the orbit in a unit time. The method to find the angle of the semiminor axis is introduced in the `Discussion` section. By changing the eccentricities we get a series of precession angle and the time. By fitting the tangent of the dots we get the precession rate and its upper and lower limit with 95% confidence.

|Eccentricity|Precession Rate (degree/yr)|Lower Limit (degree/yr)|Upper Limit (degree/yr)|
| --- | --- | --- | --- |
| 0.206 | 8.609 | 8.536 | 8.681 |
| 0.300 | 6.129 | 6.095 | 6.162 |
| 0.400 | 4.183 | 4.161 | 4.204 |
| 0.500 | 2.769 | 2.750 | 2.789 |
| 0.600 | 1.737 | 1.720 | 1.755 |
| 0.700 | 0.999 | 0.970 | 1.028 |
| 0.800 | 0.483 | 0.483 | 0.483 |
| 0.900 | 0.146 | 0.132 | 0.160 |

__Chart 1.__ the relationship between the precession rate and the eccentricity. $\alpha$=0.0008, perihelion=0.3AU

From the equation in the `introduction` section, perihelion shift σ, expressed in radians per revolution
$$\sigma=\frac{24\pi^3L^2}{T^2c^2(1-e^2)}$$
the since the perihelion is fixed, the semimajor axis has a relation with the eccentricity
$$L(1-e)=const.$$
And according to the Kepler's Third Law
$$T^2/L^3=const.$$
Our precession rate should be 
$$\frac{\sigma}{T} = \frac{24\pi^3L^2}{T^3c^2(1-e^2)}\propto \frac{(1-e)^{\frac{3}{2}}}{1+e}$$
By experience function fitting of MATLAB we get a fitting curve with R-square of 0.9839.

![11_4](https://raw.githubusercontent.com/ShixingWang/computationalphysics_N2013301020050/master/Pictures/11_4.png)      
__Figure 11.4__ (left)The errorbar plot of the precession rate and time, the errorbar is too short to be conspicuous; (right) the fitting curve with function $f(x)=13.67\frac{(1-e)^{3/2}}{1+e}$

## Reference

2. Wikipedia contributors. "Tests of general relativity." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 23 Apr. 2016. Web. 8 May. 2016.

3. Einstein, Albert (1916). "The Foundation of the General Theory of Relativity" (PDF). Annalen der Physik 49 (7): 769–822. Bibcode:1916AnP...354..769E. doi:10.1002/andp.19163540702. Retrieved 2006-09-03.
 
3. Clemence, G. M. (1947). "The Relativity Effect in Planetary Motions". Reviews of Modern Physics 19 (4): 361–364. Bibcode:1947RvMP...19..361C. doi:10.1103/RevModPhys.19.361.
  
4. Dediu, Adrian-Horia; Magdalena, Luis; Martín-Vide, Carlos (2015). Theory and Practice of Natural Computing: Fourth International Conference, TPNC 2015, Mieres, Spain, December 15-16, 2015. Proceedings (illustrated ed.). Springer. p. 141. ISBN 978-3-319-26841-5. Extract of page 141


