""" Evalutate Build Commands """

import threading
import time
import os

from auto import arguments, command_line, images
from evaluator import data


def threaded_evaluate_build_image(num_threads):
    """ Threaded evaluation of running hello-world image """
    # Add thread numbers to data file
    data.TOOL_DATA["thread_build_image_threads"] = num_threads
    data.TERM_DATA["thread_build_image_threads"] = num_threads
    tool_threads = list()
    term_threads = list()
    # Run evaluation for each number of threads
    for threads in list(num_threads):
        print("Running with " + str(threads) + " Threads")
        # pylint: disable=W0612
        for i in range(threads):
            # Add the number of threads being called to list
            tool_threads.append(threading.Thread(target=tool_build_image))
            term_threads.append(threading.Thread(target=term_build_image))

        # Start each tool thread and start timer
        start_time = time.time()
        for thread in tool_threads:
            thread.start()
        for thread in tool_threads:
            thread.join()
        # Total time for running tool test
        end_time = time.gmtime(time.time() - start_time).tm_sec
        # Add tool data to data file
        data.TOOL_DATA["thread_build_image_times"].append(end_time)
        data.TOOL_DATA['thread_build_image_ave'].append(
            data.TOOL_DATA["thread_build_image_times"][
                list(num_threads).index(threads)
            ] / threads
        )

        # Start each terminal thread and start timer
        start_time = time.time()
        for thread in term_threads:
            thread.start()
        for thread in term_threads:
            thread.join()
        # Total time for running terminal tests
        end_time = time.gmtime(time.time() - start_time).tm_sec
        # Add terminal data to data file
        data.TERM_DATA["thread_build_image_times"].append(end_time)
        data.TERM_DATA['thread_build_image_ave'].append(
            data.TERM_DATA["thread_build_image_times"][
                list(num_threads).index(threads)
            ] / threads
        )
        # Clear thread lists
        tool_threads.clear()
        term_threads.clear()
        # Delete test images
        images.delete_image("test, test-1")


def tool_build_image():
    """ Tool build image and return run time """
    # Arguments to pass to command line run
    args = ['--command', '--build', '--image', '--path',
            'Docker-Automation/samples/gentest2',
            '--name', 'test', '--threaded']
    # Start timer
    start_time = time.time()
    # Parse arguments
    parsed_args = arguments.parse_args(args)
    # Pass parsed arguments to command line
    command_line.command_line(parsed_args)
    # Return total runtime
    return time.gmtime(time.time() - start_time).tm_sec


def term_build_image():
    """ Terminal build image and return run time """
    # Start timer
    start_time = time.time()
    # Build image using terminal
    os.system(
        "docker build ~/Docker-Automation/samples/gentest2 -t test-1"
    )
    # Return total runtime
    return time.gmtime(time.time() - start_time).tm_sec


def evaluate_build_image(num_tests):
    """ Evaluate runtimes of building images via tool and command line """
    # Delete any preexisting test images
    os.system("docker rmi test-1:latest test:latest")
    average_tool_time = 0
    average_terminal_time = 0
    # Run the number of tests specified
    for x in range(num_tests):
        print("\n\nTest Number:", str(x+1))
        print("\n\n")
        # Run tool test
        tool_run_time = tool_build_image()
        # Record average tool time
        average_tool_time = average_tool_time + tool_run_time
        # Append last tool run to data file
        data.TOOL_DATA["build_image_times"].append(tool_run_time)
        print("Building directly using terminal")
        # Run terminal test
        term_run_time = term_build_image()
        # Record average terminal time
        average_terminal_time = average_terminal_time + term_run_time
        # Append last terminal run to data file
        data.TERM_DATA["build_image_times"].append(term_run_time)
        os.system("docker rmi test-1:latest test:latest")

    # Compute averages and add to data file
    data.TOOL_DATA['build_image_ave'] = average_tool_time / num_tests
    data.TERM_DATA['build_image_ave'] = average_terminal_time / num_tests
