# importing libraries
import subprocess
import os

# installing a python package
def install(package):
    temp = subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    # get the output of ping
    output = str(temp.communicate())

    output = output.split("\n")

    output = output[0].split("\\")

    # variable to store the result
    res = []

    for line in output:
        res.append(line)

    # print the results
    print("ping results: ")
    print("\n".join(res[len(res) - 3 : len(res) - 1]))
    return res


def apt_install(module_name):
    try:
        temp = subprocess.check_call(
            ["sudo apt install {}".format(module_name)],
            shell=True,
            stdin=None,
            stdout=open(os.devnull, "wb"),
            executable="/bin/bash",
        )
    #    output = str(temp.communicate())
    #
    #        output = output.split("\n")
    #
    #       output = output[0].split('\\')
    #
    # 	    # variable to store the result
    #       res = []
    #
    #       for line in output:
    #  	    res.append(line)
    #
    # 	    # print the results
    #       print('ping results: ')
    #      print('\n'.join(res[len(res) - 3:len(res) - 1]))
    except subprocess.CalledProcessError as e:
        print(e.output)


# install('selenium')
apt_install("ffmpeg")
