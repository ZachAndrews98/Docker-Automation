""" Evaluation Data Management """

import matplotlib.pyplot as plt
# import numpy as np

TOOL_DATA = {
    "build_image_times": [],
    "hello_world_times": [],
    "build_image": 0,
    "hello_world": 0,
}

TERM_DATA = {
    "build_image_times": [],
    "hello_world_times": [],
    "build_image": 0,
    "hello_world": 0,
}


def plot_data():
    """ Plot Data within Dictionaries """
    fig1, ax1 = plt.subplots()
    fig1.suptitle("Run Times for Hello World Run")
    ax1.set_xlabel("Test Number")
    ax1.set_ylabel("Run Time (s)")
    # Run Times
    ax1.plot(
        list(range(0, len(TOOL_DATA["hello_world_times"]))),
        TOOL_DATA["hello_world_times"],
        label="Tool",
        color="red"
    )

    ax1.plot(
        list(range(0, len(TERM_DATA["hello_world_times"]))),
        TERM_DATA["hello_world_times"],
        label="Terminal",
        color="blue"
    )
    # Average Run Times
    ax1.hlines(
        TOOL_DATA["hello_world"],
        xmin=0, xmax=len(TOOL_DATA["hello_world_times"]),
        label="Tool Average",
        color="red",
        linestyles="dashed"
    )
    ax1.hlines(
        TERM_DATA["hello_world"],
        xmin=0, xmax=len(TERM_DATA["hello_world_times"]),
        label="Terminal Average",
        color="blue",
        linestyles="dashed"
    )

    ax1.legend()

    fig2, ax2 = plt.subplots()
    fig2.suptitle("Run Times for Image Building")
    ax2.set_xlabel("Test Number")
    ax2.set_ylabel("Run Time (s)")
    # Run Times
    ax2.plot(
        list(range(0, len(TOOL_DATA["build_image_times"]))),
        TOOL_DATA["build_image_times"],
        label="Tool",
        color="red"
    )

    ax2.plot(
        list(range(0, len(TERM_DATA["build_image_times"]))),
        TERM_DATA["build_image_times"],
        label="Terminal",
        color="blue"
    )
    # Average Run Times
    ax2.hlines(
        TOOL_DATA["build_image"],
        xmin=0, xmax=len(TOOL_DATA["build_image_times"]),
        label="Tool Average",
        color="red",
        linestyles="dashed"
    )
    ax2.hlines(
        TERM_DATA["build_image"],
        xmin=0, xmax=len(TERM_DATA["build_image_times"]),
        label="Terminal Average",
        color="blue",
        linestyles="dashed"
    )

    ax2.legend()

    plt.show()
