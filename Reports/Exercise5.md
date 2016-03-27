written with [作业部落](https://www.zybuluo.com/ShixingWang/note/326064)

# Exercise 5: Problem 1.6 - Population Growth
[toc]
## Abstract     
A population growth problem is investigated about the linear birth rate and a quadratic death rate. Compared with the similar problem in the [previous exercise](https://github.com/ShixingWang/computationalphysics_N2013301020050/blob/master/Codes/Exercise4_Chapter1_5_equation.py), a new program finished in an object-oriented way is presented, in which the four steps a reader-friendly program should have are presented in a natural way as four internal functions of the class. Also the 3-D plotting is practiced with the importing of `visual` package.     
## Background     
### Object Oriented Programming     
Object-oriented programming is a program paradigm based on the concept "class". [\[1\]](https://en.wikipedia.org/w/index.php?title=Object-oriented_programming&oldid=711907543) A class is an abstract of several objects sharing the same characteristics and behaviors. In Python it can be treated as a data type. It is only required in this course to master the definition and single inheritance of the class.       
### VPython     
VPython is a python module used for the 3-D display and animation.[\[2\]](http://www.vpython.org/) The package can be used if you `import visual` at the front of the program. The download and install is a little troublesome for the Internet connection problems. For Windoes and Anaconda environment, the command
> conda intall -c https://conda.binstar.org/mwcraig vpython     

is always hindered with error report. You can download the package from the [official link](http://sourceforge.net/projects/vpythonwx/files/6.11-release/VPython-Win-64-Py2.7-6.11.exe/download) for the official Pyhton platform, but I have tested and it is okay to install this on Anaconda environment.      
### Pickle      
Storing results is a critical step in a physics computation. Although this was emphasized in the previous exercise report, it was not presented in the codes for the lack of knowledge about the `pickle` module. [\[3\]](https://www.zybuluo.com/ShixingWang/note/321753) The `pickle` module is one that can "create portable serialized representations of Python objects". [\[4\]](https://docs.python.org/2/reference/) More information can be found on IPython when you input `import pickle` and `pickle?`. With this we can output the data we get into a file and reload later.       
## Programs     
To practise the object-oriented paradigm we include the main body of the program into the class `population_growth`, in which there are four parts coorespongding with the initialization of variables and parameters, calculation, and restoring and representing of results.       
The code is uploaded to [Github](https://github.com/ShixingWang/computationalphysics_N2013301020050/blob/master/Codes/Exercise5_first.py).      
## Discussion     
### Comparasion with Analytical Solution
For a first-order ordinary differential equation with the form in the problem        
$$\begin{array}{ll}\frac{dN(t)}{dt}=aN(t)-bN^2(t)\\N(0)=N_0\end{array}$$
and the solution can be figured out through the method of elementary integrals and the solution is
$$N(t)=\frac{N_0ae^{ax}}{a-bN_0+bN_0e^{ax}}$$
## Acknowledgement     
I must appreciate Prof. Cai for the usage of `pickle` and `visual`. That part of the program are cloned from the sample codes on [Prof. Cai's Repository](https://github.com/caihao/computational_physics_whu.git).      
## Reference     
+ [1] Wikipedia contributors. "Object-oriented programming." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 25 Mar. 2016. Web. 27 Mar. 2016.     
+ [2] VPython, 3D Programming for Ordinary Mortals. http://www.vpython.org/, March 27, 2016.      
+ [3] Shixing Wang. Exercise 4: Problem 1.5 - Double Decay. https://Github/ShixingWang/computationalphysics_N2013301020050/blob/master/Reports/Exercise4.md, March 27, 2016.        
+ [4] Pyhton Software Foundation. The Python Language Reference. https://docs.python.org/2/reference/, March 27, 2016.       