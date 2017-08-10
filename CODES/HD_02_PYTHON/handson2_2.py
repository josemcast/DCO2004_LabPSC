tf = 0.03       # Duração de cada tom
# Diconário de notas musicais
# Do = 1 Ré = 2 Mi = 3 Fá = 4 Sol = 5 Lá = 6 Si = 7 Silêncio = 0
# Vetor de "música", usando o dicionário de notas pré-definido
vtmusic = [1,2,3,4,0,4,4,0,1,2,1,2,0,2,2,0,1,5,4,3,0,3,3,0,1,2,3,4,0,4,4]
fdo = 512                                    # Frequência da nota Dó (Hz)
vtTom2Freq = [1,9/8,5/4,4/3,3/2,5/3,15/8,2]  # Relação de frequências entre as notas musicais

import time
import numpy as np
import scipy.io.wavfile as wv 
import os
y = np.array([0])
for iplay in vtmusic: # Loop de geração e reprodução da música 
    if iplay==0:      #Implementação do silêncio
        time.sleep(tf)   
    else:
        fs = vtTom2Freq[iplay]*fdo           # Escolhe a frequência do tom corrente
        fa = 100*fs                          # Escolhe a frequência de amostragem do tom corrente
        t = np.arange(0,tf+1/fa,1/fa)          # Gera o eixo do tempo para o tom corrente
        np.append(y,np.cos(2*np.pi*fs*t))                    # Gera o tom corrente
        time.sleep(tf)


wv.write('./MATERIAL/HD_02_PYTHON/tom_corrente.wav',fa,y) #grava o tom para reprodução
os.system('cvlc ./MATERIAL/HD_02_PYTHON/tom_corrente.wav') #reproduz o tom gravado
   