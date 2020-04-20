import os
import time
from random import randint

phrases = ["turn on the lights", "turn off the lights", "it's too dark in here",
           "it's too bright in here", "flip off the lights", "flip off the lights"]


numCorrect = 0
numIncorrect = 0

for i in range(0, 30):  # Change the 5 to any other number and that is how many tests you will do!
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
