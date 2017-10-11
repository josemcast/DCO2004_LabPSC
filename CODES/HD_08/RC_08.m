% ResolucaoC_08.m
clc;close all;clear all;
%% Parâmetros
load('Pratica_08_sinal_complexo.mat')

%% Resolução 1
L=length(y);                                            % Comprimento do sinal
t=0:1/fs:1/fs*L-1/fs;                                   % Eixo do tempo
x= Ar*cos(2*pi*fm*t)+Ai*cos(2*pi*fm*t);             % Reconstrução do sinal x(t)
Noise1 = y-x;                                           % Isola o ruido
potx1=sum(abs(x.^2))/L;                                 % Potência do sinal x(t)
potN1=sum(abs(Noise1.^2))/L;                            % Potência do sinal ruido
SNR1=potx1/potN1;                                       % Estimação da SNR
SNR1=10*log10(SNR1)                                     % Converte para dB