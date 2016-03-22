import matplotlib.pyplot as plt

# size of figure
plt.figure(figsize=(14,32),dpi=80)


tau=1
tau_A0=1.
tau_B0=1
dt1=0.001
timescale0=5

N_A0=[100]  # the initial value of A
N_B0=[0]    # the initial value of B
dN_A0=[]    # 
dN_B0=[]    # 
t0=[0]      # to equate the length of t with A and B

for cycle0 in range(int(timescale0/dt1)):
    newNA0=N_A0[cycle0]+(N_B0[cycle0]/tau_B0-N_A0[cycle0]/tau_A0)*dt1
    newNB0=N_B0[cycle0]+(N_A0[cycle0]/tau_A0-N_B0[cycle0]/tau_B0)*dt1
    newtime0=t0[cycle0]+dt1
    N_A0.append(newNA0)
    N_B0.append(newNB0)
    dN_A0.append(N_B0[cycle0]/tau_B0-N_A0[cycle0]/tau_A0)
    dN_B0.append(N_A0[cycle0]/tau_A0-N_B0[cycle0]/tau_B0)
    t0.append(newtime0)
dN_A0.append(dN_A0[-1])
dN_B0.append(dN_B0[-1])

p0=plt.subplot(221)

# plot the line, color, width, style
p0.set_title('$dt=0.001s$')
p0.plot(t0, N_A0, color="blue", linewidth=2.0, linestyle="-", label="$N_A(t)$")
p0.plot(t0, N_B0, color="red", linewidth=2.0, linestyle="-", label="$N_B(t)$")

# limits and ticks
p0.set_xlim(min(t0),max(t0))
p0.set_xticks([1,2,3,4,5])
alldata0=N_A0+N_B0
p0.set_ylim(0, 120)
p0.set_yticks([0,20,40,60,80,100,120])
p0.legend(loc="right", frameon=False)

# -----------------------------Figure 1 Above----------------------------------

tau=1
tau_A=1
tau_B=1
dt2=0.01
timescale=5

N_A=[100]  # the initial value of A
N_B=[0]    # the initial value of B
dN_A=[]    # 
dN_B=[]    # 
t=[0]      # to equate the length of t with A and B

for cycle in range(int(timescale/dt2)):
    newNA=N_A[cycle]+(N_B[cycle]/tau_B-N_A[cycle]/tau_A)*dt2
    newNB=N_B[cycle]+(N_A[cycle]/tau_A-N_B[cycle]/tau_B)*dt2
    newtime=t[cycle]+dt2
    N_A.append(newNA)
    N_B.append(newNB)
    dN_A.append(N_B[cycle]/tau_B-N_A[cycle]/tau_A)
    dN_B.append(N_A[cycle]/tau_A-N_B[cycle]/tau_B)
    t.append(newtime)
dN_A.append(dN_A[-1])
dN_B.append(dN_B[-1])

# size of figure
p1=plt.subplot(222)

# plot the line, color, width, style
p1.set_title('$dt=0.01s$')
p1.plot(t, N_A, color="blue", linewidth=2.0, linestyle="-", label="$N_A(t)$")
p1.plot(t, N_B, color="red", linewidth=2.0, linestyle="-", label="$N_B(t)$")

# limits and ticks
p1.set_xlim(min(t),max(t))
p1.set_xticks([0,1,2,3,4,5])
alldata=N_A+N_B
p1.set_ylim(min(alldata), max(alldata))
p1.set_yticks([0,20,40,60,80,100,120])
p1.legend(loc="upper right", frameon=False)

# -----------------------------Figure 2 Above----------------------------------

tau=1
tau_A2=1
tau_B2=1
dt3=0.1
timescale=5

N_A2=[100]  # the initial value of A
N_B2=[0]    # the initial value of B
dN_A2=[]    # 
dN_B2=[]    # 
t2=[0]      # to equate the length of t with A and B

for cycle2 in range(int(timescale/dt3)):
    newNA2=N_A2[cycle2]+(N_B2[cycle2]/tau_B2-N_A2[cycle2]/tau_A2)*dt3
    newNB2=N_B2[cycle2]+(N_A2[cycle2]/tau_A2-N_B2[cycle2]/tau_B2)*dt3
    newtime2=t[cycle2]+dt3
    N_A2.append(newNA2)
    N_B2.append(newNB2)
    dN_A2.append(N_B2[cycle2]/tau_B2-N_A2[cycle2]/tau_A2)
    dN_B2.append(N_A2[cycle2]/tau_A2-N_B2[cycle2]/tau_B2)
    t2.append(newtime2)
dN_A2.append(dN_A2[-1])
dN_B2.append(dN_B2[-1])


p2=plt.subplot(223)

# plot the line, color, width, style
p2.set_title('$dt=0.1s$')
p2.plot(t2, N_A2, color="blue", linewidth=2.0, linestyle="-", label="$N_A(t)$")
p2.plot(t2, N_B2, color="red", linewidth=2.0, linestyle="-", label="$N_B(t)$")

# limits and ticks
p2.set_xlim(min(t2),max(t2))
p2.set_xticks([0,1,2,3,4,5])
alldata2=N_A2+N_B2
p2.set_ylim(0, 120)
p2.set_yticks([0,20,40,60,80,100,120])
p2.legend(loc="upper right", frameon=False)

# -----------------------------Figure 3 Above----------------------------------

tau=1
tau_A3=1
tau_B3=1
dt4=1
timescale3=5

N_A3=[100]  # the initial value of A
N_B3=[0]    # the initial value of B
dN_A3=[]    # 
dN_B3=[]    # 
t3=[0]      # to equate the length of t with A and B

for cycle3 in range(int(timescale3/dt4)):
    newNA3=N_A3[cycle3]+(N_B3[cycle3]/tau_B3-N_A3[cycle3]/tau_A3)*dt4
    newNB3=N_B3[cycle3]+(N_A3[cycle3]/tau_A3-N_B3[cycle3]/tau_B3)*dt4
    newtime3=t[cycle3]+dt4
    N_A3.append(newNA3)
    N_B3.append(newNB3)
    dN_A3.append(N_B3[cycle3]/tau_B3-N_A3[cycle3]/tau_A3)
    dN_B3.append(N_A3[cycle3]/tau_A3-N_B3[cycle3]/tau_B3)
    t3.append(newtime3)
dN_A3.append(dN_A3[-1])
dN_B3.append(dN_B3[-1])


p3=plt.subplot(224)

# plot the line, color, width, style
p3.set_title('$dt=1s$')
p3.plot(t3, N_A3, color="blue", linewidth=2.0, linestyle="-", label="$N_A(t)$")
p3.plot(t3, N_B3, color="red", linewidth=2.0, linestyle="-", label="$N_B(t)$")

# limits and ticks
p3.set_xlim(min(t3),max(t3))
p3.set_xticks([1,2,3,4,5])
alldata3=N_A3+N_B3
p3.set_ylim(0,120)
p3.set_yticks([0,20,40,60,80,100,120])
p3.legend(loc="right", frameon=False)

# -----------------------------Figure 4 Above----------------------------------
# -----------------------------------------------------------------------------

# save and show figures in the tablet
plt.show()