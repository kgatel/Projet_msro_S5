import numpy as np
import random
import matplotlib.pyplot as plt
import math as m

N=1000
Lambda=1.5
tab=np.zeros(N)
for i in range(N):
    tab[i]=random.random()
    tab[i]=(-1/Lambda)*m.log(1-tab[i])
tabtrie=sorted(tab)
tabtriedec=sorted(tab,reverse=True)

t2 = np.arange(0.0, 5.0, 5/N)
t1 = np.arange(0.0,4.0,4.0/N)

tabcompteur = np.zeros(N)

for i in range(N):
    for j in range(N):
        if (tabtrie[j]<=t1[i])or(tabtrie[j]>=4):
            tabcompteur[i]+=1
            
F=tabcompteur/N
plt.plot(tabtrie,F,label='F_exp')

f=np.zeros(N)


#plt.plot(tabtrie,f,'x')

F_th=np.zeros(N)
for i in range(N):
    F_th[i]=1-m.exp(-Lambda*tabtrie[i])

plt.plot(tabtrie,F_th,label='F_th')

f_th=np.zeros(N)
for i in range(N):
    f_th[i]=Lambda*m.exp(-Lambda*t2[i])
plt.plot(t2,f_th,label='f_th')

plt.legend()
plt.axis([0, 5, 0, 2])
plt.show()
