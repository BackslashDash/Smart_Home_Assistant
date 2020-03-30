'''
    - Team Members: Brian Ogbebor and Tom Murphy
    - This script aims to pipe audio to the tcp server!
'''

import pyaudio
import wave
import os

# The code below will be for the raspberry pi!

# FORMAT = pyaudio.paInt16
# CHANNELS = 1
# RATE = 44100
# CHUNK = 1024
# RECORD_SECONDS = 5
# WAVE_OUTPUT_FILENAME = "file.wav"
# audio = pyaudio.PyAudio()
# # start Recording
# stream = audio.open(format=FORMAT, channels=CHANNELS,
#                     rate=RATE, input=True,
#                     frames_per_buffer=CHUNK)

# print("recording...")
# frames = []

# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):

#     data = stream.read(CHUNK)
#     frames.append(data)


# print("finished recording")
# # stop Recording
# stream.stop_stream()
# stream.close()
# audio.terminate()
# waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# waveFile.setnchannels(CHANNELS)
# waveFile.setsampwidth(audio.get_sample_size(FORMAT))
# waveFile.setframerate(RATE)
# waveFile.writeframes(b''.join(frames))
# waveFile.close()


# User this if you are on your own laptop/desktop and not on the server! Be sure to change path as you need it for your own individual computer
os.system("rec -t raw -c 1 -b 16 -r 8k -e signed-integer - trim 0 3 | nc 35.230.174.96 5050 > ~/Desktop/decode_audio/output.txt")

os.chdir("/")
os.chdir("Users/brianogbebor/Desktop/decode_audio")
os.system("cat output.txt")
