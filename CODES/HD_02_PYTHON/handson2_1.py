# %matplotlib inline : gráficos estáticos
import numpy as np                              # Imorta biblioteca de vetores e funções matemáticas
import scipy.io.wavfile as wv                   # Imporra biblioteca para ler/escrever arquivos .wav
chSoundFile = "../../MATERIAL/HD_02_MATLAB/sound_01.wav"
[fs,sinal] = wv.read(chSoundFile)               # Abre arquivo wav
sinal=sinal*1.0 #forçando a conversão de int para float
#retorna a frequência de amostragem 'fs' e um array com as amostras 
t = np.linspace(0,len(sinal)/fs,len(sinal))
#array com os valores de tempo correspondentes à duração do sinal
#%matplotlib notebook 
from matplotlib import pyplot as plt #bib. para plotagem de gráficos
plt.figure(1,[10,7]) #cria uma 'figura em branco' para plotar gráficos
#a caixa dos gráficos terá 10x7 (largura,altura) polegadas
grafico_1 = plt.subplot(311) #subplotagem, '311' será explicado
plt.title('Sinal original') #título do gráfico 1
plt.xlabel('Tempo') #título do eixo X
plt.ylabel('Amplitude')#título do eixo Y
plt.plot(t,sinal)#plota os valores do sinal em função do tempo
grafico_2 = plt.subplot(313) #segundo gráfico da subplotagem
#amplifica-se o sinal dobrando o valor de suas amostras:
sinal_2 = 2*sinal 
plt.title('Sinal amplificado (x2.0)')#título do gráfico 2
plt.xlabel('Tempo') 
plt.ylabel('Amplitude')
plt.plot(t,sinal_2)
#definindo os limites verticais (eixo y) dos gráficos
grafico_1.set_ylim([-40000,40000])
grafico_2.set_ylim([-40000,40000])
plt.show() #finalmente, exibe-se a (sub)plotagem
