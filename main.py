""" Run Docker Automation and Setup Program """

import sys

from auto import terminal, install, arguments, command_line
from interface import interface_main


if __name__ == "__main__":
    args = arguments.parse_args(sys.argv[1:])

    if not args.install:
        print(install.install())
    if args.terminal:
        terminal.repl()
    elif len(sys.argv) <= 2:
        interface_main.start_interface()
    else:
        print(command_line.command_line(args))
