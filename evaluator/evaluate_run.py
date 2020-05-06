""" Evaluate Run Commands """

import threading
import time
import os

from auto import arguments, command_line
from evaluator import data


def threaded_evaluate_run_hello_world(num_threads):
    """ Threaded evaluation of running hello-world image """
    # Add thread numbers to data file
    data.TOOL_DATA["thread_hello_world_threads"] = num_threads
    data.TERM_DATA["thread_hello_world_threads"] = num_threads
    tool_threads = list()
    term_threads = list()
    # Run evaluation for each number of threads
    for threads in list(num_threads):
        # pylint: disable=W0612
        for i in range(threads):
            # Add the number of threads being called to list
            tool_threads.append(threading.Thread(target=tool_hello_world))
            term_threads.append(threading.Thread(target=term_hello_world))

        # Start each tool thread and start timer
        start_time = time.time()
        for thread in tool_threads:
            thread.start()
        for thread in tool_threads:
            thread.join()
        # Total time for running tool test
        end_time = time.gmtime(time.time() - start_time).tm_sec
        # Add tool data to data file
        data.TOOL_DATA["thread_hello_world_times"].append(end_time)
        data.TOOL_DATA['thread_hello_world_ave'].append(sum(
            data.TOOL_DATA["thread_hello_world_times"]
        ) / threads)

        # Start each terminal thread and start timer
        start_time = time.time()
        for thread in term_threads:
            thread.start()
        for thread in term_threads:
            thread.join()
        # Total time for running terminal tests
        end_time = time.gmtime(time.time() - start_time).tm_sec
        # Add terminal data to data file
        data.TERM_DATA["thread_hello_world_times"].append(end_time)
        data.TERM_DATA['thread_hello_world_ave'].append(sum(
            data.TERM_DATA["thread_hello_world_times"]
        ) / threads)
        # Clear thread lists
        tool_threads.clear()
        term_threads.clear()


def tool_hello_world():
    """ Tool run hello world image and return run time """
    # Arguments to pass to command line run
    args = ['--command', '--run', '--image',
            '--name', 'hello-world',
            '--args', ' --rm', '--sep']
    # Start timer
    start_time = time.time()
    # Parse arguments
    parsed_args = arguments.parse_args(args)
    # Pass parsed arguments to command line
    command_line.command_line(parsed_args)
    # Return total runtime
    return time.gmtime(time.time() - start_time).tm_sec


def term_hello_world():
    """ Terminal run hello world image and return run time """
    # Start timer
    start_time = time.time()
    # Run image using terminal
    os.system(
        "docker run --rm hello-world"
    )
    # Return total runtime
    return time.gmtime(time.time() - start_time).tm_sec


def evalutate_run_hello_world(num_tests):
    """ Evaluate runtime of running hello-world image """
    average_tool_time = 0
    average_terminal_time = 0
    # Run the number of tests specified
    for x in range(num_tests):
        print("\n\nTest Number:", str(x+1))
        print("\n\n")
        # Run tool test
        tool_run_time = tool_hello_world()
        # Record average tool time
        average_tool_time = average_tool_time + tool_run_time
        # Append last tool run to data file
        data.TOOL_DATA["hello_world_times"].append(tool_run_time)
        print("Running Image directly using terminal")
        # Run terminal test
        term_run_time = term_hello_world()
        # Record average terminal time
        average_terminal_time = average_terminal_time + term_run_time
        # Append last terminal run to data file
        data.TERM_DATA["hello_world_times"].append(term_run_time)
        
    # Compute averages and add to data file
    data.TOOL_DATA['hello_world_ave'] = average_tool_time / num_tests
    data.TERM_DATA['hello_world_ave'] = average_terminal_time / num_tests
