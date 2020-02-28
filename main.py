""" Run Docker Automation and Setup Program """

import sys

from auto import docker_auto, install
from interface import interface_main


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--terminal":
        print(install.install())
        docker_auto.repl()
    else:
        print(install.install())
        interface_main.start_interface()
