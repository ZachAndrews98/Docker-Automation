""" Evalutate Build Commands """

import concurrent.futures
import time
import os

from auto import arguments, command_line
from evaluator import data


def threaded_evaluate_build_image(num_tests, num_threads):
    """ Threaded evaluation of running hello-world image """
    # pylint: disable=W0612
    for x in range(num_threads):
        print("\n\nTest Number:", str(x+1))
        print("\n\n")
        with concurrent.futures.ThreadPoolExecutor(
                max_workers=num_threads
        ) as executor:
            os.system("docker rmi test:latest")
            future = executor.submit(tool_build_image)
            data.TOOL_DATA["thread_build_image_times"].append(future.result())

        with concurrent.futures.ThreadPoolExecutor(
                max_workers=num_threads
        ) as executor:
            os.system("docker rmi test-1:latest")
            future = executor.submit(term_build_image)
            data.TERM_DATA["thread_build_image_times"].append(future.result())

    data.TOOL_DATA['thread_build_image_ave'] = sum(
        data.TOOL_DATA["thread_build_image_times"]
    ) / num_tests
    data.TERM_DATA['thread_build_image_ave'] = sum(
        data.TERM_DATA["thread_build_image_times"]
    ) / num_tests


def tool_build_image():
    """ Tool build image and return run time """
    args = ['--build', '--image', '--path', './gentest2',
            '--name', 'test', '--threaded']
    start_time = time.time()
    parsed_args = arguments.parse_args(args)
    command_line.command_line(parsed_args)
    return time.gmtime(time.time() - start_time).tm_sec


def term_build_image():
    """ Terminal build image and return run time """
    start_time = time.time()
    os.system(
        "docker build ./gentest2 -t test-1"
    )
    return time.gmtime(time.time() - start_time).tm_sec


def evaluate_build_image(num_tests):
    """ Evaluate runtimes of building images via tool and command line """
    os.system("docker rmi test-1:latest test:latest")
    average_tool_time = 0
    average_terminal_time = 0
    for x in range(num_tests):
        print("\n\nTest Number:", str(x+1))
        print("\n\n")
        tool_run_time = tool_build_image()
        average_tool_time = average_tool_time + tool_run_time
        data.TOOL_DATA["build_image_times"].append(tool_run_time)
        print("Building directly using terminal")
        term_run_time = term_build_image()
        average_terminal_time = average_terminal_time + term_run_time
        data.TERM_DATA["build_image_times"].append(term_run_time)
        os.system("docker rmi test-1:latest test:latest")

    data.TOOL_DATA['build_image_ave'] = average_tool_time / num_tests
    data.TERM_DATA['build_image_ave'] = average_terminal_time / num_tests
