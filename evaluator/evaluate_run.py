""" Evaluate Run Commands """

import time, os

import docker

from auto import arguments, command_line
from evaluator import data


def evalutate_run_hello_world(num_tests):
    """ Evaluate runtime of running hello-world image """
    args = ['--run', '--image', '--name', 'hello-world',
            '--args', ' --rm', '--sep']
    average_tool_time = 0
    average_terminal_time = 0
    for x in range(num_tests):
        print("\n\nTest Number:", str(x+1))
        print("\n\n")
        start_time = time.time()
        parsed_args = arguments.parse_args(args)
        command_line.command_line(parsed_args)
        tool_run_time = (time.gmtime(time.time() - start_time).tm_sec)
        average_tool_time = average_tool_time + \
                tool_run_time
        data.TOOL_AVERAGES["hello_world_times"].append(tool_run_time)
        print("Running Image directly using terminal")
        start_time = time.time()
        os.system(
            "docker run" + str(parsed_args.args) + " " + \
            str(parsed_args.name)
        )
        term_run_time = (time.gmtime(time.time() - start_time).tm_sec)
        average_terminal_time = average_terminal_time + \
                term_run_time
        data.TERM_AVERAGES["hello_world_times"].append(term_run_time)

    data.TOOL_AVERAGES['hello_world'] = average_tool_time / num_tests
    data.TERM_AVERAGES['hello_world'] = average_terminal_time / num_tests
