""" Run Docker Automation and Setup Program """

import sys

from auto import terminal, install, arguments, command_line
from interface import interface_main


if __name__ == "__main__":
    # parse any arguments passed on runtime
    args = arguments.parse_args(sys.argv[1:])
    if not args.no_install:
        # Check installation status if not supplied
        print(install.install())
    if args.command:
        # If run is command line based
        print(command_line.command_line(args))
    elif args.terminal:
        # If run is terminal repl based
        terminal.repl()
    elif len(sys.argv) <= 2:
        # If operating via interface
        interface_main.start_interface()
