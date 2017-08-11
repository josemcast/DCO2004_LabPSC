tf = 0.03                                    # Duração de cada tom
# Diconário de notas musicais:
# Do = 1 Ré = 2 Mi = 3 Fá = 4 Sol = 5 Lá = 6 Si = 7 Silêncio = 0
# Vetor de "música", usando o dicionário de notas pré-definido
vtmusic = [1,2,3,4,0,4,4,0,1,2,1,2,0,2,2,0,1,5,4,3,0,3,3,0,1,2,3,4,0,4,4]
fdo = 512                                    # Frequência da nota Dó (Hz)
vtTom2Freq = [1,9/8,5/4,4/3,3/2,5/3,15/8,2]  # Relação de frequências entre as notas musicais

import time
import numpy as np
import scipy.io.wavfile as wv 
import os
y = np.zeros(1)

for iplay in vtmusic:
    if iplay==0:
        y=np.append(y,np.zeros(3000))        #Implementaçao do silencio
    else:
        fs = vtTom2Freq[iplay]*fdo           # Escolhe a frequência do tom corrente
        fa = int(100*fs)                     # Escolhe a frequência de amostragem do tom corrente
        t = np.arange(0,tf+1/fa,1/fa)        # Gera o eixo do tempo para o tom corrente
        y=np.append(y,np.cos(2*np.pi*fs*t))  # Gera o tom corrente e o junta com os já gerados
        y=np.append(y,np.zeros(3000))


wv.write('../../MATERIAL/HD_02_PYTHON/tom_corrente.wav',44100,y)         #grava o tom para reprodução
#reproduz o tom gravado:
os.system('cvlc --play-and-exit ../../MATERIAL/HD_02_PYTHON/tom_corrente.wav')           
