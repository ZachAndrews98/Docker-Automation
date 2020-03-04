""" Run Docker Automation and Setup Program """

import sys

from auto import terminal, install, arguments, command_line
from interface import interface_main


if __name__ == "__main__":
    args = arguments.parse_args(sys.argv[1:])

    if args.terminal:
        print(install.install())
        terminal.repl()
    elif len(sys.argv) == 1:
        print(install.install())
        interface_main.start_interface()
    else:
        print(install.install())
        print(command_line.command_line(args))
