""" Evaluate Run Commands """

import threading
import time
import os

from auto import arguments, command_line
from evaluator import data


def threaded_evaluate_run_hello_world(num_threads):
    """ Threaded evaluation of running hello-world image """
    # print(str(num_threads))
    data.TOOL_DATA["thread_hello_world_threads"] = num_threads
    data.TERM_DATA["thread_hello_world_threads"] = num_threads
    tool_threads = list()
    term_threads = list()
    for threads in list(num_threads):
        # pylint: disable=W0612
        for i in range(threads):
            tool_threads.append(threading.Thread(target=tool_hello_world))
            term_threads.append(threading.Thread(target=term_hello_world))

        start_time = time.time()
        for thread in tool_threads:
            thread.start()
        for thread in tool_threads:
            thread.join()
        end_time = time.gmtime(time.time() - start_time).tm_sec
        data.TOOL_DATA["thread_hello_world_times"].append(end_time)
        data.TOOL_DATA['thread_hello_world_ave'].append(sum(
            data.TOOL_DATA["thread_hello_world_times"]
        ) / threads)

        start_time = time.time()
        for thread in term_threads:
            thread.start()
        for thread in term_threads:
            thread.join()
        end_time = time.gmtime(time.time() - start_time).tm_sec
        data.TERM_DATA["thread_hello_world_times"].append(end_time)
        data.TERM_DATA['thread_hello_world_ave'].append(sum(
            data.TERM_DATA["thread_hello_world_times"]
        ) / threads)

        tool_threads.clear()
        term_threads.clear()


def tool_hello_world():
    """ Tool run hello world image and return run time """
    args = ['--command', '--run', '--image',
            '--name', 'hello-world',
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

    data.TOOL_DATA['hello_world_ave'] = average_tool_time / num_tests
    data.TERM_DATA['hello_world_ave'] = average_terminal_time / num_tests
