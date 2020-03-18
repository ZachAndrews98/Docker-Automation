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

print("Build Image Test")
print("\tTool Run Times: " + str(data.TOOL_AVERAGES['build_image_times']))
print("\tTerminal Run Times: " + str(data.TERM_AVERAGES['build_image_times']))
print("\tAverage Tool: " + str(data.TOOL_AVERAGES['build_image']))
print("\tAverage Terminal: " + str(data.TERM_AVERAGES['build_image']))
print("\n\n")
print("Hello World Test")
print("\tTool Run Times: " + str(data.TOOL_AVERAGES['hello_world_times']))
print("\tTerminal Run Times: " + str(data.TERM_AVERAGES['hello_world_times']))
print("\tAverage Tool: " + str(data.TOOL_AVERAGES['hello_world']))
print("\tAverage Terminal: " + str(data.TERM_AVERAGES['hello_world']))

data.plot_data()
