"""
    - Members: Tom Murphy and Brian Ogbebor
    - This python script will make sure the OS has the correct directories
    and environment setup!

"""
import subprocess
from pathlib import Path
import os

# Check if the user has /decode_audio as a directory.


def hasDecodeDir():

    os.chdir("/")  # Go to root dir

    if os.path.exists("/decode_audio"):

        print("decode_audio directory already exists")
        return 1

    print("decode_audio directory does not exist")
    return 0


def main():

    home = str(Path.home())

    if hasDecodeDir() == 0:
        print("Creating Directory")

        os.chdir("/")
        os.system("sudo mkdir decode_audio")

        assert os.path.exists(
            "/decode_audio"), "decode_audio could not be created!"

        print("Directory successfully created!")

    # We are going to assume that kaldi is already installed on the machine
    # so let's run the script to prepare online decoding\

    os.system("./run.sh")

    os.chdir(home)
    os.chdir("kaldi/egs/aspire/s5")

    print("Set up complete!")

    # Sets up Path variables and begins the connection to the tcp server
    os.system("./runn.sh")


if __name__ == "__main__":
    main()
