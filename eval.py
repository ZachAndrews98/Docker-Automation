""" Evaluator """

import time, os

import docker

from auto import arguments, command_line

from evaluator import data
from evaluator import evaluate_build as build
from evaluator import evaluate_run as run

CLIENT = docker.from_env()

build.evaluate_build_image(5)
run.evalutate_run_hello_world(5)
build.threaded_evaluate_build_image(5,5)
run.threaded_evaluate_run_hello_world(5,5)


print("Build Image Test")
print("\tTool Run Times: " + str(data.TOOL_DATA['build_image_times']))
print("\tTerminal Run Times: " + str(data.TERM_DATA['build_image_times']))
print("\tAverage Tool: " + str(data.TOOL_DATA['build_image_ave']))
print("\tAverage Terminal: " + str(data.TERM_DATA['build_image_ave']))
print("\n\n")

print("Hello World Test")
print("\tTool Run Times: " + str(data.TOOL_DATA['hello_world_times']))
print("\tTerminal Run Times: " + str(data.TERM_DATA['hello_world_times']))
print("\tAverage Tool: " + str(data.TOOL_DATA['hello_world_ave']))
print("\tAverage Terminal: " + str(data.TERM_DATA['hello_world_ave']))
print("\n\n")

print("Threaded Build Image Test")
print("\tTool Run Times: " + str(data.TOOL_DATA['thread_build_image_times']))
print(
    "\tTerminal Run Times: " + str(data.TERM_DATA['thread_build_image_times'])
)
print("\tAverage Tool: " + str(data.TOOL_DATA['thread_build_image_ave']))
print("\tAverage Terminal: " + str(data.TERM_DATA['thread_build_image_ave']))
print("\n\n")

print("Threaded Hello World Test")
print("\tTool Run Times: " + str(data.TOOL_DATA["thread_hello_world_times"]))
print(
    "\tTerminal Run Times: " + str(data.TERM_DATA["thread_hello_world_times"])
)
print("\tAverage Tool: " + str(data.TOOL_DATA['thread_hello_world_ave']))
print("\tAverage Terminal: " + str(data.TERM_DATA['thread_hello_world_ave']))
print("\n\n")

data.plot_data()
