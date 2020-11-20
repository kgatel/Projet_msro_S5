import numpy as np
import random
import matplotlib.pyplot as plt
import math as m

N=2000
Lambda=0.5
esperance=0.0
ecart_moyen=0.0
tab=np.zeros(N)
for i in range(N):
    tab[i]=random.random()
    tab[i]=(-1/Lambda)*m.log(1-tab[i])
tabtrie=sorted(tab)

t1 = np.arange(0.0,5.0,5.0/N)

tabcompteur = np.zeros(N)

i=1
for i in range(N):
    for j in range(N):
        if (tabtrie[j]<=t1[i])or((tabtrie[j]>=5.0)and(t1[i]>=5.0)):
            tabcompteur[i]+=1
            
F=tabcompteur/N
plt.plot(t1,F,label='F_exp')

    
#plt.plot(tabtrie,f,'x')

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
print("En calculant l'écart moyen entre les deux courbes on trouve {}".format(round(ecart_moyen,5)))
print("Donc notre courbe experimentale se superpose presque parfaitement avec la courbe théorique")

for i in range(N):
    esperance+=tabtrie[i]
esperance=esperance/N

print()
print("Nous avons pris λ = {}, notre esperance théorique est donc: 1/λ = {}".format(Lambda, round(1/Lambda,5)))
print("L'esperance de notre tirage est {}. Ce qui nous donne un écart en valeur absolue de {}".format(round(esperance,5), round(abs(esperance-(1/Lambda)),5)))
print("Cette différence est toujours très faible, et comfirme que notre tirage se rapproche bien d'un tirage aléatoire")
print("selon une loi exponentielle de paramètre λ = {}".format(round(Lambda,5)))
