""" Evalutate Build Commands """

import time, os

import docker

from auto import arguments, command_line
from evaluator import data


def evaluate_build_image(num_tests):
    """ Evaluate runtimes of building images via tool and command line """
    os.system("docker rmi test-1:latest test:latest")
    args = ['--build', '--image', '--path', './gentest2',
            '--name', 'test', '--threaded']
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
        data.TOOL_AVERAGES["build_image_times"].append(tool_run_time)
        print("Building directly using terminal")
        start_time = time.time()
        os.system(
            "docker build " + str(parsed_args.path) + " -t " + \
            str(parsed_args.name) + "-1"
        )
        term_run_time = time.gmtime(time.time() - start_time).tm_sec
        average_terminal_time = average_terminal_time + \
                term_run_time
        data.TERM_AVERAGES["build_image_times"].append(term_run_time)
        os.system("docker rmi test-1:latest test:latest")

    data.TOOL_AVERAGES['build_image'] = average_tool_time / num_tests
    data.TERM_AVERAGES['build_image'] = average_terminal_time / num_tests
