> Written with [作业部落](https://www.zybuluo.com/ShixingWang/note/311331).

# Exercise 3 - Patterns on a Screen


## Abstract

The monitor is one of the most important output devices of computers[\[1\]](#jump1) and the graphic processing has been paid great attention in both hardware and software industry.[\[2\]](#jump2)[\[3\]](#jump3) In this exercise we managed to show the our name on the pixel lattice, and additionally, arbitrary charater strings. The highest level of this project is to show an animation on the screen. My project owns the advantage of the ability to changge lines if the string is too long, although failing to notice the usage of the dictionary prevents from showing punctions. [\[4\]](#jump4)

## Background

Although different monitors use various imaging materials like LCD, LED and so on, the rudiment of monitors is just a panel with million small pixels that can emit lights of various colors and various brightness, which involves discipines like vision perception that has little relation with this course.   [\[1\]][cite1][\[3\]][cite3] To determine when and which color to show on the screen, the computer has to process large amount of calcuation simultaneusly, which led to the independence of GPU from CPU.[\[2\]][cite2] In this exercise we simplify the monitor into a dot matrix by ignoring the color and brightness of pixels, showing patterns in a binary way of either blank or "#". 

## Code and Result

### General Codes

First I designed each character with a list of length 12.

> A=["   #   ","  # #  "," #   # "," #   # "," ##### "," #   # "," #   # "," #   # "," #   # ","       ","       ","       "]
B=[' ####  ', ' #   # ', ' #   # ',' #   # ', ' ####  ', ' #   # ', ' #   # ', ' #   # ', ' ####  ', '       ', '       ', '       ']
C=['  ###  ',' #   # ',' #     ',' #     ',' #     ',' #     ',' #     ',' #   # ','  ###  ','       ','       ','       ']
D=[' ###   ',' #  #  ',' #   # ',' #   # ',' #   # ',' #   # ',' #   # ',' #  #  ',' ###   ','       ','       ','       ']
E=[' ##### ',' #     ',' #     ',' #     ',' ##### ',' #     ',' #     ',' #     ',' ##### ','       ','       ','       ']
F=[' ##### ',' #     ',' #    ',' #     ',' ##### ',' #     ',' #     ',' #     ',' #     ','       ','       ','       ']
G=['  ###  ',' #   # ',' #     ',' #     ',' # ### ',' #   # ',' #   # ',' #  ## ','  ## # ','       ','       ','       ']
H=[' #   # ',' #   # ',' #   # ',' #   # ',' ##### ',' #   # ',' #   # ',' #   # ',' #   # ','       ','       ','       ']
I=[' ##### ','   #   ','   #   ','   #   ','   #   ','   #   ','   #   ','   #   ',' ##### ','       ','       ','       ']
J=['    ## ','     # ','     # ','     # ','     # ','     # ','     # ',' #   # ','  ###  ','       ','       ','       ']
K=[' #   # ',' #   # ',' #  #  ',' # #   ',' ##    ',' # #   ',' #  #  ',' #   # ',' #   # ','       ','       ','       ']
L=[' #     ',' #     ',' #     ',' #     ',' #     ',' #     ',' #     ',' #     ',' ##### ','       ','       ','       ']
M=['#     #','##   ##','# # # #','#  #  #','#     #','#     #','#     #','#     #','#     #','       ','       ','       ']
N=[' #   # ',' ##  # ',' ##  # ',' # # # ',' # # # ',' # # # ',' #  ## ',' #  ## ',' #   # ','       ','       ','       ']
O=['  ###  ',' #   # ',' #   # ',' #   # ',' #   # ',' #   # ',' #   # ',' #   # ','  ###  ','       ','       ','       ']
P=[' ####  ',' #   # ',' #   # ',' #   # ',' ####  ',' #     ',' #     ',' #     ',' #     ','','','']
Q=['  ###  ',' #   # ',' #   # ',' #   # ',' #   # ',' #   # ',' # # # ',' #  ## ','  #### ','       ','       ','       ']
R=[' ####  ',' #   # ',' #   # ',' #   # ',' ####  ',' # #   ',' # #   ',' #  #  ',' #   # ','       ','       ','       ']
S=['  ###  ',' #   # ',' #     ',' #     ','  ###  ','     # ','     # ',' #   # ','  ###  ','       ','       ','       ']
T=[' ##### ','   #   ','   #   ','   #   ','   #   ','   #   ','   #   ','   #   ','   #   ','       ','       ','       ']
U=[' #   # ',' #   # ',' #   # ',' #   # ',' #   # ',' #   # ',' #   # ',' #   # ','  ###  ','       ','       ','       ']
V=[' #   # ',' #   # ',' #   # ',' #   # ',' #   # ','  # #  ','  # #  ','   #   ','   #   ','       ','       ','       ']
W=['#     #', '#     #', '#     #', '#     #', '#     #', '#  #  #', '# # # #', '##   ##', '#     #','       ','       ','       ']
X=[' #   # ',' #   # ','  # #  ','  # #  ','   #   ','  # #  ','  # #  ',' #   # ',' #   # ','       ','       ','       ']
Y=[' #   # ',' #   # ',' #   # ','  # #  ','   #   ','   #   ','   #   ','   #   ','   #   ','       ','       ','       ']
Z=[' ##### ','     # ','     # ','    #  ','   #   ','  #    ',' #     ',' #     ',' ##### ','       ','       ','       ']
_=['       ','       ','       ','       ','       ','       ','       ','       ','       ','       ','       ','       ']
a=['       ','       ','       ','   ### ','  #  # ',' #   # ',' #   # ',' #  ## ',' ### # ','       ','       ','       ']
b=[' #     ',' #     ',' #     ',' ####  ',' #   # ',' #   # ',' #   # ',' #   # ',' ####  ','       ','       ','       ']
c=['       ','       ','       ','  ###  ',' #   # ',' #     ',' #     ',' #     ','  #### ','       ','       ','       ']
d=['     # ','     # ','     # ','  #### ',' #   # ',' #   # ',' #   # ',' #   # ','  #### ','       ','       ','       ']
e=['       ','       ','       ','  ###  ',' #   # ',' ##### ',' #     ',' #     ','  #### ','       ','       ','       ']
f=['    ## ','   #   ','   #   ',' ##### ','   #   ','   #   ','   #   ','   #   ','   #   ','   #   ','   #   ',' ##    ']
g=['       ','       ','       ','  ###  ',' #   # ',' #   # ',' #   # ',' #  ## ','  #### ','     # ','     # ',' ####  ']
h=[' #     ',' #     ',' #     ',' ####  ',' #   # ',' #   # ',' #   # ',' #   # ',' #   # ','       ','       ','       ']
i=['       ','   #   ','       ','   #   ',' ###   ','   #   ','   #   ','   # # ',' ####  ','       ','       ','       ']
j=['       ','     # ','       ','    ## ','     # ','     # ','     # ','     # ','     # ','     # ',' #   # ','  ### ']
k=[' #     ',' #     ',' #     ',' #  #  ',' # #   ',' ##    ',' # #   ',' #  #  ',' #   # ','       ','       ','       ']
l=['   #   ','   #   ','   #   ','   #   ','   #   ','   #   ','   #   ','   #   ','    ## ','       ','       ','       ']
m=['       ','       ','       ',' ## #  ',' # # # ',' # # # ',' # # # ',' #   # ',' #   # ','       ','       ','       ']
n=['       ','       ','       ',' ####  ',' #   # ',' #   # ',' #   # ',' #   # ',' #   # ','       ','       ','       ']
o=['       ','       ','       ','  ###  ',' #   # ',' #   # ',' #   # ',' #   # ','  ###  ','       ','       ','       ']
p=['       ','       ','       ',' ####  ',' #   # ',' #   # ',' #   # ',' #   # ',' ####  ',' #     ',' #     ',' #     ']
q=['       ','       ','       ','  #### ',' #   # ',' #   # ',' #   # ',' #   # ','  #### ','     # ','     # ','     # ']
r=['       ','       ','       ',' # ##  ',' ##  # ',' #     ',' #     ',' #     ',' #     ','       ','       ','       ']
s=['       ','       ','       ','  #### ',' #     ','  ###  ','     # ','     # ',' ####  ','       ','       ','       ']
t=['       ','  #    ','  #    ',' ##### ','  #    ','  #    ','  #    ','  #  # ','   ##  ','       ','       ','       ']
u=['       ','       ','       ',' #   # ',' #   # ',' #   # ',' #   # ',' #  ## ','  ## # ','       ','       ','       ']
v=['       ','       ','       ',' #   # ',' #   # ',' #   # ',' #   # ','  # #  ','   #   ','       ','       ','       ']
w=['       ','       ','       ',' #   # ',' #   # ',' # # # ',' # # # ',' # # # ','  # #  ','       ','       ','       ']
x=['       ','       ','       ',' #   # ','  # #  ','   #   ','   #   ','  # #  ',' #   # ','       ','       ','       ']
y=['       ','       ','       ',' #   # ',' #   # ',' #   # ',' #   # ','  # ## ','   # # ','     # ',' #   # ','  ###  ']
z=['       ','       ','       ',' ##### ','    #  ','   #   ','  #    ',' #     ',' ##### ','       ','       ','       ']

The spacing in each element of the lists above gets lost in Markdown environment. In my code every element has a length of 7.

Then I used `raw_input` to get character strings from the user and used `list()` function to turn it into a list of strings.[\[4\]](#jump4)[\[5\]](#jump5) The variale `Width` is set to chage lines if the string is too long. 

> Width=input("How many characters would you like to see in one line?  ")

> \# Width=20 \# Fixed length for conventience of testing.

> ans=list(raw\_input('Input Anything You Like with "_" for Blank:  '))

Then I wrote the commands to change lines by changing the initial list into a new list with each line an element of the new list. Every time a line is fulled, the elements are put inside the new list and the corresponding elements in the old list get deleted.

> line=[None]*(len(ans)//Width)

> for cycle1 in range(len(ans)//Width):

> ____line[cycle1]=ans[:Width]

> ____del ans[:Width]

> if len(ans)!=0:

> ____line.append(ans)

And I defined a function `Conflate()` for convenience to show the pattern on the screen. It returns a list of the length 12. The n-th element of the list is the conflation of every character that should be in this line. We used the internal function `exec()`, which needs character strings as the argument and can turn the string into the python commands.[\[4\]](#jump4)[\[5\]](#jump5)

> def Conflate(arg1):

>\____"Conflate each line"

>\____arg2=len(arg1)

>\____screen=['']*12

>\____for cycle2 in range(12):

>\____ \____for cycle3 in range(arg2):

>\____ \____ \____exec("screen[cycle2]+="+arg1[cycle3]+'[cycle2]')

>\____return(screen)

At last it is time to show each line on the screen.

> for cycle4 in range(len(line)): 
> \____ cycle5 in range(12):
> \____ \____ print(Conflate(line[cycle4])[cycle5])

### Level 1. Show my Name on the Screen

![3_1](https://raw.githubusercontent.com/ShixingWang/computationalphysics_N2013301020050/master/Pictures/3_1.png)

### Level 2. Show Arbitrary Characters on the Screen

![3_2](https://raw.githubusercontent.com/ShixingWang/computationalphysics_N2013301020050/master/Pictures/3_2.png)

Notice that our program can adjust the number of characters in each line and change lines if the string is too long.

### Level 3. Animation of Characters

Since we do not want the images to flash too fast we need to include the `time` module and `time.sleep()` function for time interval between frames. To clear the screen we need `os` module and `os.system('cls')` function.

In our animation we want the sentence to show up chracter by character, so there is one more procedure between the input from users and the list. 

So at the begining

> import time

> import os

> ans1=list(raw_input('Input Anything You Like with "_" for Blank:  '))

> for cycle6 in range(len(ans1)+1):

> \____ ans=ans1[:cycle6]

> \____ line=['']*(len(ans)//Width)

And every line below shoule be in the `for` cycle.

At the last few lines

>     for cycle4 in range(len(line)): 

>        for cycle5 in range(12):

>            print(Conflate(line[cycle4])[cycle5])

>    time.sleep(2) #The time intervel you  like between images. 

>    os.system('cls')

![3_3](https://raw.githubusercontent.com/ShixingWang/computationalphysics_N2013301020050/master/Pictures/3_3.gif)

## Discussion and Future Direction

This project shows briefly how our monitor works under the control of GPU. The meaningful code is not very long and I even think the hardest part is to tolerate the bore to design and input the list of the characters! \_(:з」∠)_ The shining point, unmodestly speaking, is the ling changeing codes along with the `exec()` function. And this project elucidates how powerful list is in Python. Also as a novice of programming the control structures like `if` and `for` are good practices for me.

However, in this process I failed to notice the convenience to use dictionary as the connection between what users input with our patterns. This is much more convenient for it circumvents the `exec()` function and the complex character computation inside it. Also, this has made great inconvience that users have to supplant "_" for blank, further preventing the project to expand to show the punctuations.

## Acknowledgement

The code in this project is finished all by myself. But I have to devote appreciation to my friend and roommate Li Yao (2013301020048). It was him who shared with me the idea to use dictionary to correspond each character the user inputs with the pattern we design. 

## Reference

1. [Wikipedia contributors. "Computer monitor." Wikipedia, The Free Encyclopedia, 4 Mar. 2016. Web. 13 Mar. 2016.](https://en.wikipedia.org/wiki/Computer_monitor)<span id="jump1"></span>     

2. [Wikipedia contributors. "Graphics processing unit." Wikipedia, The Free Encyclopedia, 27 Jan. 2016. Web. 13 Mar. 2016.](https://en.wikipedia.org/wiki/Graphics_processing_unit) <span id="jump2"></span>       

3. [Wikipedia contributors. "Graphical user interface." Wikipedia, The Free Encyclopedia, 27 Feb. 2016. Web. 13 Mar. 2016.](https://en.wikipedia.org/wiki/Graphical_user_interface)<span id="jump3"></span>    

4. Allen Downey. Think Python-How to Think Like a Computer Scientist. Green Tea Press, 2012.<span id="jump4"></span>     

5. Magnus Lie Hetland. Begining Python-from Novice to Professional (2nd Edition). Posts & Telecom Press, July 2010. <span id="jump5"></span>    