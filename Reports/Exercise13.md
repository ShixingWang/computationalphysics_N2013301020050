> View this in [Github](https://github.com/ShixingWang/computationalphysics_N2013301020050/blob/master/Reports/Exercise13.md)         
> View this in ["作业部落"](https://www.zybuluo.com/ShixingWang/note/386050)

# Exercise 13: Potential Field between Finite Capacitor Plates

__王世兴__      
__2013301020050__

---       
__Problem 5.7__        
Write two programs to solve the capacitor problem of Figure 5.6 and 5.7, one using Jacobi method and one using simultaneous over relaxation (SOR) algrithem . For a fixed accuracy compare the number of iterations, $N_{iter}$ that each algrithm requires as a function of the number of grid elements, $L$. Show that for Jacobi method $N_{iter}\thicksim L^2$, while with SOR, $N_{iter}\thicksim L$.

---      

## Abstract

The partial differential equation is of physicists' great interest for its widely applicaiton in decribing physical systems. Jacobi method and simultaneous over relaxation (SOR) method are two algrithm that keep a balance of the simplicity for comprehension and accuracy of computation. Thanks to Li Yao's code, we realized the two algorithm with Python in calculating a finite parallel capacitor system.

## Background

### Jacobi Method [2]
 
In numerical linear algebra, the Jacobi method (or Jacobi iterative method) is an algorithm for determining the solutions of a diagonally dominant system of linear equations. Each diagonal element is solved for, and an approximate value is plugged in. The process is then iterated until it converges. This algorithm is a stripped-down version of the Jacobi transformation method of matrix diagonalization. The method is named after Carl Gustav Jacob Jacobi.

### Simultaneous Over Relaxation Method [3]

In numerical linear algebra, the method of successive over-relaxation (SOR) is a variant of the Gauss–Seidel method for solving a linear system of equations, resulting in faster convergence. A similar method can be used for any slowly converging iterative process.

It was devised simultaneously by David M. Young, Jr. and by H. Frankel in 1950 for the purpose of automatically solving linear systems on digital computers. Over-relaxation methods had been used before the work of Young and Frankel. An example is the method of Lewis Fry Richardson, and the methods developed by R. V. Southwell. However, these methods were designed for computation by human calculators, and they required some expertise to ensure convergence to the solution which made them inapplicable for programming on digital computers. These aspects are discussed in the thesis of David M. Young, Jr.

## Features of the Codes

1.  __Initial condition__        
    At first we give a guess about the system with all the points zero other than the boundary conditions. Thus we need a quick way to creat a two-dimension zero list. Fistly we used the list calculation 

    > [[0.0]*m]*n

    However, this method proved inappropriate because when we want to change the value of some elements in one row, the elements at the same position in other rows will also be changed. The reason is not clear at present. So we use the following code

    > [[0.0 for i in range(m)] for j in range(n)]

2. __Interating Number and Judge for Convergence__       
    To measure the complexity of the paorgram we need to define the how we can claim that the algorithm is at convergence, then we defined the interating number `self.N` to see how many cycle we need to reach the convergence. We define the sum of the difference at each point before and after one turn as `self.delta`. `self.N` is added one to itself every time the program enters the cycle.

## Results

### Jacobi method

![13_1](https://raw.githubusercontent.com/ShixingWang/computationalphysics_N2013301020050/master/Pictures/13_1.png)      
__Figure 13.1__ Fitting curve of interating time versus time step; the expresssion is given in the figure.

### SOR method

![13_2](https://raw.githubusercontent.com/ShixingWang/computationalphysics_N2013301020050/master/Pictures/13_3.png)      
__Figure 13.2__ Fitting curve of interating time versus time step; the expresssion is given in the figure.

### $N_{iter}$ versus Step Length $L$

|Step Length|Jacobi Method|SOR method|
|---|---|---|
|10|68|33|
|20|265|70|
|30|589|107|
|40|1028|146|

We used MATLAB to fit the curve with quadrant and linear functions as the result  is shown below.

![13_3](https://raw.githubusercontent.com/ShixingWang/computationalphysics_N2013301020050/master/Pictures/13_3.png)      
__Figure 13.3__ Fitting curve of interating time versus time step; the expresssion is given in the figure.

## Reference and Acknowledgment

I must devote my appreciation to Li Yao for his code.

1. Giodano, N.J., Nakanishi, H. Computational Physics. Tsinghua University Press, December 2007

2. Jacobi method. (2016, May 16). In Wikipedia, The Free Encyclopedia. Retrieved 12:47, May 22, 2016, from https://en.wikipedia.org/w/index.php?title=Jacobi_method&oldid=720500900

3. Successive over-relaxation. (2016, April 27). In Wikipedia, The Free Encyclopedia. Retrieved 12:46, May 22, 2016, from https://en.wikipedia.org/w/index.php?title=Successive_over-relaxation&oldid=717363228



