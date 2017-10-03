##### 2.1 e) #####

def normalized(list):
    sum = sum(list)
    return list.map(lambda x: x/sum)

##b)##
import numpy as np

bandas = [0, 4, 8, 13, 30, 45]
bandaspaciente = []

for paciente in pacientes:
    dtfspatient = None
    test = sio.loadmat(paciente)["data"]
    avg1 = np.mean(test, axis = 1)
    avg2 = np.mean(avg1, axis = 0)
    freq, pot = sig.welch(avg2, fs = 250, nfft = 2048)
    bandaspaciente.append([])
    
    for i in range(len(bandas) -1):
        inicio = bandas[i] 
        fin = bandas[i+1]
        valores = [pot[i] for i in range(len(pot)) if freq[i] >= inicio and freq[i] < fin]
        bandaspaciente[-1].append(sum(valores))
        
pd.DataFrame(normalized(bandaspaciente), columns = ["delta", "theta", "alpha", "beta", "gamma"])