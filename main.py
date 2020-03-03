""" Run Docker Automation and Setup Program """

import sys

from auto import docker_auto, install, arguments
from interface import interface_main


if __name__ == "__main__":
    args = arguments.parse_args(sys.argv[1:])

    if args.terminal:
        print(install.install())
        docker_auto.repl()
    elif len(sys.argv) == 1:
        print("gui")
        # print(install.install())
        # interface_main.start_interface()
    else:
        print(install.install())
        docker_auto.command_line(args)
