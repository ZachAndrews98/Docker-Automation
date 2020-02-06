""" Main file for running docker installation, generation, and gui """
import sys

from auto import install_docker
from auto import docfile_gen

COMMAND_LIST = ["generate", "build", "run", "exit", "quit"]


def main():
    """ Installs Docker and enters command system """
    print(install_docker.install())
    return repl()


def repl():
    """ Interactive command system """
    command = str(input(">> "))
    while command not in COMMAND_LIST:
        print("That is not a valid command")
        command = str(input(">> "))
    if command != "exit" and command != "quit":
        print(command)
        args = command.split(' ')
        if args[0] == "generate":
            directory = get_directory()
            to_dir = str(
                input("Input location to mount files (default:test):")).strip()
            if to_dir != "":
                docfile_gen.generate_dockerfile(directory, to_dir=to_dir)
            else:
                docfile_gen.generate_dockerfile(directory)
        if args[0] == "build":
            docfile_gen.build_image(
                get_directory(), str(
                    input("Input image name: ")))
        if args[0] == "run":
            image_name = str(input("Image Name: "))
            args = str(input("Arguments: ")).strip()
            if args != "":
                docfile_gen.run_image(image_name, args=args)
            else:
                docfile_gen.run_image(image_name)
        repl()
    return 0


def get_directory():
    """ Returns an inputted directory """
    return str(input("Input path to directory:\n"))
