import matplotlib.pyplot as plt

tau=1
tau_A=tau
tau_B=tau
dt=0.01
timescale=5

N_A=[100]  # the initial value of A
N_B=[0]    # the initial value of B
dN_A=[]    # 
dN_B=[]    # 
t=[0]      # to equate the length of t with A and B

for cycle in range(int(timescale/dt)):
    newNA=N_A[cycle]+(N_B[cycle]/tau_B-N_A[cycle]/tau_A)*dt
    newNB=N_B[cycle]+(N_A[cycle]/tau_A-N_B[cycle]/tau_B)*dt
    newtime=t[cycle]+dt
    N_A.append(newNA)
    N_B.append(newNB)
    dN_A.append(N_B[cycle]/tau_B-N_A[cycle]/tau_A)
    dN_B.append(N_A[cycle]/tau_A-N_B[cycle]/tau_B)
    t.append(newtime)
dN_A.append(dN_A[-1])
dN_B.append(dN_B[-1])

# size of figure
plt.figure(figsize=(14,8),dpi=80)
p1=plt.subplot(111)

# plot the line, color, width, style
p1.plot(t, N_A, color="blue", linewidth=2.0, linestyle="-", label="$N_A(t)$")
p1.plot(t, N_B, color="red", linewidth=2.0, linestyle="-", label="$N_B(t)$")
p1.plot(t, dN_A, color="blue", linewidth=2.0, linestyle="--", label="$d\ N_A(t)/dt$")
p1.plot(t, dN_B, color="red", linewidth=2.0, linestyle="--", label="$d\ N_B(t)/dt$")

# limits and ticks
p1.xlim(min(t),max(t))
p1.xticks([0,1,2,3,4,5])
alldata=N_A+N_B
p1.ylim(min(alldata), max(alldata))
p1.yticks([0,20,40,60,80,100,120])
p1.legend(loc="upper right", frameon=False)



# save and show figures in the tablet
plt.show()