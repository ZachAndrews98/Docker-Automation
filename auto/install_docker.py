""" Checks OS and installs Docker following a specific instruction set """
import os
import platform
import subprocess


PLATFORM = platform.system()


def install():
    """ Main installation function """
    if confirm_installation():
        if PLATFORM == "Linux":
            # pylint: disable=W1505
            distro = platform.linux_distribution()
        elif PLATFORM == "MacOS":
            distro = ("MacOS", "", "")
        file = get_instructions(distro)
        if file != "No Instruction Set":
            execute_instructions(file)
        if not confirm_installation():
            return "Docker successfully installed"
        return "Issue installing Docker"
    return "Docker already installed"


def get_instructions(distro):
    """ Determines what instruction set is required to install Docker """
    file = ""
    if distro[0] == "Ubuntu":
        file = "./instructions/ubuntu"
    elif distro[0] == "CentOS":
        file = "./instructions/centos"
    elif distro[0] == "Debian":
        file = "./instructions/debian"
    elif distro[0] == "Fedora":
        file = "./instructions/fedora"
    elif distro[0] == "MacOS":
        file = "./instructions/macos"
    else:
        file = "No Instruction Set"
    return file


def execute_instructions(file):
    """ Executes the installation instructions """
    commands = open(file, 'r')
    for command in commands:
        command = command.replace("\n", "")
        os.system(command)


def confirm_installation():
    """ Confirms if Docker was properly installed """
    proc = subprocess.Popen(
        ["docker", "run", "hello-world"], stdout=subprocess.PIPE)
    # pylint: disable=W0106
    proc.communicate()[0]
    return proc.returncode


print(get_instructions(("MacOS","","")))
