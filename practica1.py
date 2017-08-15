import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import random

f = open("tiempo.txt")
next(f)
data = np.loadtxt(f)
#for col in range(1,len(data[0])):
#    plt.scatter(range(len(data[:,col])), data[:,col])


#Corregimos el dato porque consideramos que es un error humano, al agregar un .
#queda lo suficientemente cerca de la media

##Test de si el tiempo obtenido con lluvia es independiente del obtenido con sol/nublado
print (np.corrcoef(data[:,1], data[:,3]))
print (np.corrcoef(data[:,2], data[:,3]))

## test de apareamiento para ver si el clima nublado influye
print (scipy.stats.ttest_rel(data[:,1], data[:,2]))

## test de permutaciones para ver si en dias de lluvia los atletas son mas lentos
datos = data[:,1] + data[:,3]
print (datos)
labels = ["sol"]*len(data[:,1]) + ["lluvia"]*len(data[:,3])

delta0 = np.mean(data[:,1]) - np.mean(data[:,3])
deltas = [delta0]
for i in range(999999):
    random.shuffle(labels)
    meanSol = np.mean([datos[i] for i in range(len(datos)) if labels[i] == "sol"])
    meanLluvia = np.mean([datos[i] for i in range(len(datos)) if labels[i] != "sol"])
    deltas.append(meanSol - meanLluvia)

print(delta0)
plt.hist(deltas)
plt.show()

print(len([delta for delta in deltas if delta <= delta0])/len(deltas))
