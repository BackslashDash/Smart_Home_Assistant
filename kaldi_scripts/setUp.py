""" 
    - Members: Tom Murphy and Brian Ogbebor
    - This python script will make sure the OS has the correct directories
    and environment setup!

"""
import os

# Check if the user has /decode_audio as a directory.


def hasRootDir():

    # Grab working directory (should be within Smart_Home_Assistant/kaldi_scripts)
    originDir = os.getcwd()

    # Nav to root dir

    os.chdir("/")

    if os.path.exists("/decode_audio"):

        os.chdir(originDir)
        print("decode_audio directory already exists")
        return 1

    print("decode_audio directory does not exist")
    os.chdir(originDir)
    return 0


def main():
    if hasRootDir() == 0:
        print("Creating Directory")

        os.chdir("/")
        os.system("sudo mkdir decode_audio")

        assert os.path.exists(
            "/decode_audio"), "decode_audio could not be created!"

    # We are going to assume that kaldi is already installed on the machine


if __name__ == "__main__":
    main()
