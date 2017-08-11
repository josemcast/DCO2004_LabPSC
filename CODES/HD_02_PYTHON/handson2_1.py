#importando as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt 
import scipy.io.wavfile as wv 
import os

tf = 1                                  # Tempo de duração da nota
fc = 512                                # Frequência da nota Dó
fs = 100*fc                  # Frequencia de amostragem da nota. 
t =np.arange(0,tf+1/fs,1/fs) # Vetor tempo. Para cada elemento do vetor t, haverá um elemento em y correspondente.
A = 1                    # Amplitude do sinal
y=A*np.cos(2*np.pi*fc*t)       # Sinal senoidal

plt.plot(t,y)                # Visualizar o sinal gerado  
plt.axis([0,0.02,-2,2])     # Zoom para melhor visualização  
plt.show() 

#DESCOMENTE AS LINHAS DE COMANDO ABAIXO APÓS AJUSTAR O ENDEREÇO, COMO SUGERIDO

#importando e armazenando o arquivo de áudio numa variável
fs_som, som = wv.read('../../MATERIAL/HD_02_MATLAB/sound_01.wav')

#salvando o tom gerado em um arquivo de extensão .wav :
wv.write('../../MATERIAL/HD_02_PYTHON/tom_gerado.wav',fs,y)
#reproduzindo o arquivo

os.system('cvlc --play-and-exit ../../MATERIAL/HD_02_PYTHON/tom_gerado.wav') 
#vlc chama o programa VLC Audio Player
#'c' serve para que nenhuma interface seja aberta

