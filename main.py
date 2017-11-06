

import pyaudio
import numpy as np


#### Pseudo-codigo
# Ler texto da entrada
#
# Pegar caracter por caracter
# Para cada caracter, pegar valor ascii
# Converter valor ascii em binario
# Agrupar bits em duplas e mapear para 4 opcoes de frequencia
# Concatenar uma freq diferente no inicio de cada caracter
#

# text = raw_input('Choose a number: ')
text = 'blabla'

first = 528
third = (5/4.0)*first
fifth = (3/2.0)*first
seventh = (15/8.0)*first

list1 = np.array([first, third, fifth, seventh])


p = pyaudio.PyAudio()

volume = 1     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 1   # in seconds, may be float
f = 200.0        # sine frequency, Hz, may be float

# creates a vector for time
t = np.arange(fs*duration)

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