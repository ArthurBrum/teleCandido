import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Fazer depois:
# A) instanciador da classe:
# -Criar com valor padrao de framerate e tempo de gravacao por parametro


# gravar do microfone

CHUNKSIZE = 1024  # fixed chunk size

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 2
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

numpydata = np.fromstring(data, dtype=np.int16)

stream.stop_stream()
stream.close()
p.terminate()

plt.plot(numpydata)
plt.show()





# passar para numpy array




