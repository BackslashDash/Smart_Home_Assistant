'''
    - Team Members: Brian Ogbebor and Tom Murphy
    - This script aims to run the online decoding command while using 
    input from the pyaudio to take in sound
'''

import os
import subprocess
import datetime
from pathlib import Path

p1 = subprocess.run(["cat", "setUp.py"], capture_output=True, text=True)

# print(p1.stdout)

p2 = subprocess.run(["grep", "-n", "print"],
                    capture_output=True, text=True, input=p1.stdout)

print(p2.stdout)
