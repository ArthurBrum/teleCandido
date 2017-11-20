
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


first = 220.00
third = (5/4.0)*first
fifth = (3/2.0)*first
seventh = (15/8.0)*first

list1 = 2*np.pi*np.array([first, third, fifth, seventh, seventh, fifth, first, third])

n_points = 0.1              # 'tempo' que a frequencia eh 'tocada'

n_items = list1.size        # numeros de itens (freqs, no caso)
t_end = n_items*n_points    # tamanho total no eixo X ('tempo' total)

# Teorema da amostragem pede um pouco mais de 2x a maior freq
s_rate = 2.1*list1.max()

# Cria vetor de tempo
t = np.linspace(0, t_end, s_rate*t_end)

#Aloca um novo vetor com mesmo tamanho de t
samples = np.empty(t.size)

# Para cada loop preenche uma parte da saida (uma frequencias por vez)
i_begin = 0
for i in range(1, n_items+1):

    # Estabelece fim da parte que sera preenchida nessa iteracao
    i_end = s_rate*n_points * i;

    samples[i_begin:i_end] = np.sin(list1[i-1]*t[i_begin:i_end])

    # Estabelece inicio da proxima parte
    i_begin = i_end


# adding white noise
noise = np.random.normal(size=t.shape)
samples = samples+noise


# plot pra ver o baguiu
plt.plot(t, samples)
#plt.xlim([0,0.1])
plt.show()

# Determina qual a frequencia que sera procurada criando um filtro
filter = np.sin(list1[1]*t[0:s_rate*n_points])

# Faz convolucao pelo sinal procurando 'matches' do filtro
out= signal.fftconvolve(samples, filter, mode='full')


# Plot the data
plt.plot(t, out[0:t.size])
plt.show()


