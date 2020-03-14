"""
    - Members: Tom Murphy and Brian Ogbebor
    - This python script will make sure the OS has the correct directories
    and environment setup!

"""
import subprocess
import os

# Check if the user has /decode_audio as a directory.


def hasDecodeDir():

    os.system("/")  # Go to root dir

    if os.path.exists("/decode_audio"):

        print("decode_audio directory already exists")
        return 1

    print("decode_audio directory does not exist")
    return 0


def main():
    if hasDecodeDir() == 0:
        print("Creating Directory")

        os.system("/")

        make_dir = "sudo mkdir decode_audio"
        os.system(make_dir)

        assert os.path.exists(
            "/decode_audio"), "decode_audio could not be created!"

        print("Directory successfully created!")

    # We are going to assume that kaldi is already installed on the machine
    # Next let's set up a directory

    subprocess.run("cd", shell=True)
    subprocess.run("cd kaldi/egs/aspire/s5", shell=True)
    print("Now in the s5 directory")
    # yes | os.system("steps/online/nnet3/prepare_online_decoding.sh \
    # --mfcc-config conf/mfcc_hires.conf data/lang_chain exp/nnet3/extractor exp/chain/tdnn_7b exp/tdnn_7b_chain_online")


if __name__ == "__main__":
    main()
