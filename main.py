

import pyaudio
import numpy as np


#### Pseudo-codigo

#### TRANSMISSION
#
# Ler texto da entrada
#
# Pegar caracter por caracter
# Para cada caracter, pegar valor ascii
# Converter valor ascii em binario
# Agrupar bits em duplas e mapear para 4 opcoes de frequencia
# Concatenar uma freq diferente no inicio de cada caracter
#

#### RECEPTION
#
# Gravar audio
# Passar para vetor/waveform
# Encontrar sincronia
# Fazer produtos internos (ou filtro casado de outra forma) para avaliar distancia minima
# Determinar frequencias e converter para conjunto de bits


# text = raw_input('Choose a number: ')
text = 'blabla'

first = 32.70
third = 2*(5/4.0)*first
fifth = 4*(3/2.0)*first
seventh = 8*(15/8.0)*first

list1 = np.array([first, third, fifth, seventh, seventh, fifth, first, third])


p = pyaudio.PyAudio()

volume = 1     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 1   # in seconds, may be float
f = 200.0        # sine frequency, Hz, may be float

# creates a vector for time
t = np.arange(fs*duration)

# white noise
noise = np.random.normal(size=t.shape)

for note in list1:
    # generate samples (note conversion to float32 array)
    samples = (np.sin(2*np.pi*t*note/fs)).astype(np.float32)

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    # play. May repeat with different volume values (if done interactively)
    stream.write(volume*samples)

stream.stop_stream()
stream.close()

p.terminate()