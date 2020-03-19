""" Evaluate Run Commands """

import time
# import threading
import os

from auto import arguments, command_line
from evaluator import data

# def threaded_evaluate_run_hello_world(num_tests, num_threads):
#     """ Threaded evaluation of running hello-world image """
#     for x in range(num_threads):
#


def tool_hello_world():
    """ Tool run hello world image and return run time """
    args = ['--run', '--image', '--name', 'hello-world',
            '--args', ' --rm', '--sep']
    start_time = time.time()
    parsed_args = arguments.parse_args(args)
    command_line.command_line(parsed_args)
    return time.gmtime(time.time() - start_time).tm_sec


def term_hello_world():
    """ Terminal run hello world image and return run time """
    start_time = time.time()
    os.system(
        "docker run --rm hello-world"
    )
    return time.gmtime(time.time() - start_time).tm_sec


def evalutate_run_hello_world(num_tests):
    """ Evaluate runtime of running hello-world image """
    average_tool_time = 0
    average_terminal_time = 0
    for x in range(num_tests):
        print("\n\nTest Number:", str(x+1))
        print("\n\n")
        tool_run_time = tool_hello_world()
        average_tool_time = average_tool_time + tool_run_time
        data.TOOL_DATA["hello_world_times"].append(tool_run_time)
        print("Running Image directly using terminal")
        term_run_time = term_hello_world()
        average_terminal_time = average_terminal_time + term_run_time
        data.TERM_DATA["hello_world_times"].append(term_run_time)

    data.TOOL_DATA['hello_world'] = average_tool_time / num_tests
    data.TERM_DATA['hello_world'] = average_terminal_time / num_tests
