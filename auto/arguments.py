""" Argument Parsing """

import argparse

PARSER = argparse.ArgumentParser()
# Command flags
PARSER.add_argument('--command', action='store_true', default=False)
PARSER.add_argument('--no-install', action="store_true", default=False)
PARSER.add_argument('--terminal', action='store_true')
PARSER.add_argument('--build', action='store_true')
PARSER.add_argument('--run', action='store_true')
PARSER.add_argument('--list', action='store_true')
PARSER.add_argument('--delete', action='store_true')
PARSER.add_argument('--login', action='store_true')
PARSER.add_argument('--pull', action='store_true')
PARSER.add_argument('--push', action='store_true')
PARSER.add_argument('--kill', action='store_true')
PARSER.add_argument('--stop', action='store_true')
PARSER.add_argument('--restart', action='store_true')
PARSER.add_argument('--generate', action='store_true')
PARSER.add_argument('--threaded', action='store_false', default=True)
# Parameter flags
PARSER.add_argument('--image', action='store_true')
PARSER.add_argument('--container', action='store_true')
PARSER.add_argument('--name', action='store')
PARSER.add_argument('--names', action='append', nargs='+')
PARSER.add_argument('--args', action='store')
PARSER.add_argument('--path', action='store')
PARSER.add_argument('--username', action='store')
PARSER.add_argument('--password', action='store')
PARSER.add_argument('--tag', action='store')
PARSER.add_argument('--dest', action='store')
PARSER.add_argument('--sep', action='store_false', default=True)


def parse_args(args):
    """ Parse command line arguments and return results """
    return PARSER.parse_args(args)
