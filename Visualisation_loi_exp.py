import numpy as np
import random
import matplotlib.pyplot as plt
import math as m

N=1000
Lambda=1.5
esperance=0.0
ecart_moyen=0.0
tab=np.zeros(N)
tabu=np.zeros(N)

for i in range(N):
    tab[i]=random.random()
    tabu[i]=1-tab[i]				#construction de G(1-U)
    tab[i]=(-1/Lambda)*m.log(1-tab[i])
    tabu[i]=(-1/Lambda)*m.log(1-tabu[i])

tabtrie=sorted(tab)    #tableau trie
tabutrie=sorted(tabu)

t1 = np.arange(0.0,5.0,5.0/N)   #tableau N valeurs entre 0 5 par pas 5/5

tabcompteur = np.zeros(N)
tabucompteur = np.zeros(N)

for i in range(N):
    for j in range(N):
        if (tabtrie[j]<=t1[i])or((tabtrie[j]>=5.0)and(t1[i]>=5.0)):
            tabcompteur[i]+=1
        if (tabutrie[j]<=t1[i])or((tabutrie[j]>=5.0)and(t1[i]>=5.0)):
            tabucompteur[i]+=1
F=tabcompteur/N
FU=tabucompteur/N

ecartU=0                  #ecart moyen entre F et FU
for i in range(N):
	ecartU+=abs(F[i]-FU[i])
ecartU=ecartU/N

plt.plot(t1,F,label='F_exp')
plt.plot(t1,FU,label='F(1-U) exp')

F_th=np.zeros(N)
for i in range(N):
    F_th[i]=1-m.exp(-Lambda*tabtrie[i])

plt.plot(tabtrie,F_th,label='F_th')

plt.legend()
plt.axis([0, 5, 0, 2])
plt.show()

for i in range(N):
    ecart_moyen+=abs(F[i]-(1-m.exp(-Lambda*t1[i])))
ecart_moyen=ecart_moyen/N


for i in range(N):
    esperance+=tabtrie[i]
esperance=esperance/N

print()
print("Nous avons pris lambda = ",Lambda)
print("Notre esperance theorique est donc: 1/lambda = ",round(1/Lambda,5))

print("Notre esperance experimentale = ",esperance)

print("En calculant l'ecart moyen entre les deux courbes on trouve ")
print(round(ecart_moyen,5))
print("Donc notre courbe experimentale se superpose presque ")
print("parfaitement avec la courbe theorique")

print("Cette difference est toujours tres faible, et comfirme ")
print("que notre tirage se rapproche bien d'un tirage aleatoire ")
print("selon une loi exponentielle de parametre lambda = ")
print(round(Lambda,5))

print("L'ecart moyen entre G(U) et G(1-U) vaut ",round(ecartU,5))
