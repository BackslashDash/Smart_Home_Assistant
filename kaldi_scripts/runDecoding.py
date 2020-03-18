'''
    - Team Members: Brian Ogbebor and Tom Murphy
    - This script aims to pipe audio to the tcp server!
'''


import subprocess
import sys
import pyaudio
import numpy as np
import pylab
import time
import matplotlib.pyplot as plt


RATE = 44100
CHUNK = int(RATE/20)  # RATE / number of updates per second


def soundplot(stream):
    t1 = time.time()
    data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
    print(data)


if __name__ == "__main__":
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    for i in range(sys.maxsize**10):
        soundplot(stream)
    stream.stop_stream()
    stream.close()
    p.terminate()


#os.system("sox ~/Desktop/brian_flip_on_the_lights.wav -t raw -c 1 -b 16 -r 8k -e signed-integer - | nc 35.245.124.99 5050")

# p1 = subprocess.Popen("sox brian_flip_on_the_lights.wav -t raw -c 1 -b 16 -r 8k -e signed-integer -",
#                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

# process = subprocess.Popen(
#    ["nc", "35.245.124.99", "5050"], stdin=p1.stdout, stdout=subprocess.PIPE)
