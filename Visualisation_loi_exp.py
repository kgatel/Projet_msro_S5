import numpy as np
import random
import matplotlib.pyplot as plt
import math as m

N=2000
Lambda=1.5
esperance=0.0
ecart_moyen=0.0
tab=np.zeros(N)
for i in range(N):
    tab[i]=random.random()
    tab[i]=(-1/Lambda)*m.log(1-tab[i])
tabtrie=sorted(tab)    #tableau trie

t1 = np.arange(0.0,5.0,5.0/N)   #tableau N valeurs entre 0 5 par pas 5/5

tabcompteur = np.zeros(N)

i=1
for i in range(N):
    for j in range(N):
        if (tabtrie[j]<=t1[i])or((tabtrie[j]>=5.0)and(t1[i]>=5.0)):
            tabcompteur[i]+=1
            
F=tabcompteur/N
plt.plot(t1,F,label='F_exp')


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

print("En calculant l'ecart moyen entre les deux courbes on trouve ")
print(round(ecart_moyen,5))
print("Donc notre courbe experimentale se superpose presque ")
print("parfaitement avec la courbe theorique")

for i in range(N):
    esperance+=tabtrie[i]
esperance=esperance/N

print()
print("Nous avons pris lambda = ",Lambda)
print("Notre esperance theorique est donc: 1/lambda = ",round(1/Lambda,5))
print("Ce qui nous donne un ecart en valeur absolue de ")
print(round(abs(esperance-(1/Lambda)),5))
print("Cette difference est toujours tres faible, et comfirme ")
print("que notre tirage se rapproche bien d'un tirage aleatoire ")
print("selon une loi exponentielle de parametre lambda = ")
print(format(round(Lambda,5)))
