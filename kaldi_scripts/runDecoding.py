'''
    - Team Members: Brian Ogbebor and Tom Murphy
    - This script aims to pipe audio to the tcp server!
'''

import pyaudio
import wave
import os
from random import randint
import time

# Say yes or anything else if you want to run tests or else just press enter!
runStats = input("Are you running for statistical purposes?: ")

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

phrases = ["turn on the lights", "turn off the lights", "it's too dark in here",
           "it's too bright in here", "flip off the lights", "flip off the lights"]

if runStats:
    numCorrect = 0
    numIncorrect = 0

    for i in range(0, 5):  # Change the 5 to any other number and that is how many tests you will do!
        position = randint(0, 5)
        print()
        print("Please say: " + phrases[position])
        print("Sleeping for 3 seconds...")
        time.sleep(3)
        # Change the path below for wherever your decode_audio directory is on your computer
        os.system("rec -t raw -c 1 -b 16 -r 8k -e signed-integer - trim 0 3 | nc 35.236.233.51 5050 > ~/Desktop/decode_audio/output.txt")

        # Change the path below for wherever yoru decode_audio directory is on your computer
        with open("/Users/brianogbebor/Desktop/decode_audio/output.txt", "r") as output:
            if phrases[position] in output.read():
                print("Good!")
                numCorrect += 1
            else:
                print("Bad!")
                numIncorrect += 1
    print()
    print("Kaldi decoded " + str(numCorrect) + " phrases correctly")
    print()
    print("Kaldi decoded " + str(numIncorrect) + " phrases incorrectly")

else:
    # Use this if you are on your own laptop/desktop and not on the server! Be sure to change path as you need it for your own individual computer
    os.system("rec -t raw -c 1 -b 16 -r 8k -e signed-integer - trim 0 3 | nc 35.236.233.51 5050 > ~/Desktop/decode_audio/output.txt")

    os.chdir("/")
    os.chdir("Users/brianogbebor/Desktop/decode_audio")
    os.system("cat output.txt")
