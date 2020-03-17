'''
    - Team Members: Brian Ogbebor and Tom Murphy
    - This script aims to pipe audio to the tcp server!
'''

import os
import subprocess
import pyaudio
from pathlib import Path

p1 = subprocess.Popen(["cat", "setUp.py"],
                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

stdout, stderr = p1.communicate()

print(stdout.decode())
