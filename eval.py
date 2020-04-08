""" Evaluator """

import time, os

import docker

from auto import arguments, command_line

from evaluator import data
from evaluator import evaluate_build as build
from evaluator import evaluate_run as run
from evaluator import evaluate_generate as generate


CLIENT = docker.from_env()

# build.evaluate_build_image(10)
# run.evalutate_run_hello_world(10)
# build.threaded_evaluate_build_image((1,5,10,15))
# run.threaded_evaluate_run_hello_world((1,5,10,15))
generate.evaluate_generate()


# print("Build Image Test")
# print("\tTool Run Times: " + str(data.TOOL_DATA['build_image_times']))
# print("\tTerminal Run Times: " + str(data.TERM_DATA['build_image_times']))
# print("\tAverage Tool: " + str(data.TOOL_DATA['build_image_ave']))
# print("\tAverage Terminal: " + str(data.TERM_DATA['build_image_ave']))
# print("\n\n")
#
# print("Hello World Test")
# print("\tTool Run Times: " + str(data.TOOL_DATA['hello_world_times']))
# print("\tTerminal Run Times: " + str(data.TERM_DATA['hello_world_times']))
# print("\tAverage Tool: " + str(data.TOOL_DATA['hello_world_ave']))
# print("\tAverage Terminal: " + str(data.TERM_DATA['hello_world_ave']))
# print("\n\n")
#
# print("Threaded Build Image Test")
# print(
#     "\tNumber of Threads List: " + str(
#         data.TOOL_DATA["thread_build_image_threads"]
#     )
# )
# print("\tTool Run Times: " + str(data.TOOL_DATA["thread_build_image_times"]))
# print(
#     "\tTerminal Run Times: " + str(data.TERM_DATA["thread_build_image_times"])
# )
# print("\tAverage Tool: " + str(data.TOOL_DATA['thread_build_image_ave']))
# print("\tAverage Terminal: " + str(data.TERM_DATA['thread_build_image_ave']))
# print("\n\n")
#
# print("Threaded Hello World Test")
# print(
#     "\tNumber of Threads List: " + str(
#         data.TOOL_DATA["thread_hello_world_threads"]
#     )
# )
# print("\tTool Run Times: " + str(data.TOOL_DATA["thread_hello_world_times"]))
# print(
#     "\tTerminal Run Times: " + str(data.TERM_DATA["thread_hello_world_times"])
# )
# print("\tAverage Tool: " + str(data.TOOL_DATA['thread_hello_world_ave']))
# print("\tAverage Terminal: " + str(data.TERM_DATA['thread_hello_world_ave']))
# print("\n\n")

data.write_data()
# data.plot_data()
