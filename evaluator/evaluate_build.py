""" Evalutate Build Commands """

# import concurrent.futures
import threading
import time
import os

from auto import arguments, command_line
from evaluator import data


def threaded_evaluate_build_image(num_threads):
    """ Threaded evaluation of running hello-world image """
    data.TOOL_DATA["thread_build_image_threads"] = num_threads
    data.TERM_DATA["thread_build_image_threads"] = num_threads
    tool_threads = list()
    term_threads = list()
    for threads in list(num_threads):
        # pylint: disable=W0612
        for i in range(threads):
            tool_threads.append(threading.Thread(target=tool_build_image))
            term_threads.append(threading.Thread(target=term_build_image))

        start_time = time.time()
        for thread in tool_threads:
            thread.start()
        for thread in tool_threads:
            thread.join()
        end_time = time.gmtime(time.time() - start_time).tm_sec
        data.TOOL_DATA["thread_build_image_times"].append(end_time)
        data.TOOL_DATA['thread_build_image_ave'].append(sum(
            data.TOOL_DATA["thread_build_image_times"]
        ) / threads)

        start_time = time.time()
        for thread in term_threads:
            thread.start()
        for thread in term_threads:
            thread.join()
        end_time = time.gmtime(time.time() - start_time).tm_sec
        data.TERM_DATA["thread_build_image_times"].append(end_time)
        data.TERM_DATA['thread_build_image_ave'].append(sum(
            data.TERM_DATA["thread_build_image_times"]
        ) / threads)

        tool_threads.clear()
        term_threads.clear()


def tool_build_image():
    """ Tool build image and return run time """
    args = ['--build', '--image', '--path',
            'Docker-Automation/samples/gentest2',
            '--name', 'test', '--threaded']
    start_time = time.time()
    parsed_args = arguments.parse_args(args)
    command_line.command_line(parsed_args)
    return time.gmtime(time.time() - start_time).tm_sec


def term_build_image():
    """ Terminal build image and return run time """
    start_time = time.time()
    os.system(
        "docker build ~/Docker-Automation/samples/gentest2 -t test-1"
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
