""" Evaluation Data Management """

import matplotlib.pyplot as plt
import numpy as np

TOOL_AVERAGES = {
    "build_image_times": [],
    "hello_world_times": [],
    "build_image": 0,
    "hello_world": 0,
}

TERM_AVERAGES = {
    "build_image_times": [],
    "hello_world_times": [],
    "build_image": 0,
    "hello_world": 0,
}


def plot_data():
    fig1, ax1 = plt.subplots()
    fig1.suptitle("Run Times for Hello World Run")
    ax1.set_xlabel("Test Number")
    ax1.set_ylabel("Run Time (s)")
    # Run Times
    ax1.plot(
        list(range(0, len(TOOL_AVERAGES["hello_world_times"]))),
        TOOL_AVERAGES["hello_world_times"],
        label="Tool"
    )

    ax1.plot(
        list(range(0, len(TERM_AVERAGES["hello_world_times"]))),
        TERM_AVERAGES["hello_world_times"],
        label="Terminal"
    )
    # Average Run Times
    ax1.hlines(
        TOOL_AVERAGES["hello_world"],
        xmin=0, xmax=len(TOOL_AVERAGES["hello_world_times"]),
        label="Tool Average"
    )
    ax1.hlines(
        TERM_AVERAGES["hello_world"],
        xmin=0, xmax=len(TERM_AVERAGES["hello_world_times"]),
        label="Terminal Average"
    )

    ax1.legend()

    fig2, ax2 = plt.subplots()
    fig1.suptitle("Run Times for Hello World Run")
    ax2.set_xlabel("Test Number")
    ax2.set_ylabel("Run Time (s)")
    # Run Times
    ax2.plot(
        list(range(0, len(TOOL_AVERAGES["build_image_times"]))),
        TOOL_AVERAGES["build_image_times"],
        label="Tool"
    )

    ax2.plot(
        list(range(0, len(TERM_AVERAGES["build_image_times"]))),
        TERM_AVERAGES["build_image_times"],
        label="Terminal"
    )
    # Average Run Times
    ax2.hlines(
        TOOL_AVERAGES["build_image"],
        xmin=0, xmax=len(TOOL_AVERAGES["build_image_times"]),
        label="Tool Average"
    )
    ax2.hlines(
        TERM_AVERAGES["build_image"],
        xmin=0, xmax=len(TERM_AVERAGES["build_image_times"]),
        label="Terminal Average"
    )

    ax2.legend()

    plt.show()
