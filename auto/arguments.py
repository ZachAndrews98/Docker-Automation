""" Argument Parsing """

import argparse

PARSER = argparse.ArgumentParser()

PARSER.add_argument('--terminal', action='store_true')
PARSER.add_argument('--build', action='store_true')
PARSER.add_argument('--run', action='store_true')
PARSER.add_argument('--list', action='store_true')
PARSER.add_argument('--delete', action='store_true')
PARSER.add_argument('--image', action='store_true')
PARSER.add_argument('--container', action='store_true')
PARSER.add_argument('--name', action='store')
PARSER.add_argument('--names', action='append', nargs='+')
PARSER.add_argument('--args', action='store')
PARSER.add_argument('--path', action='store')


def parse_args(args):
    """ Parse command line arguments and return results """
    return PARSER.parse_args(args)
