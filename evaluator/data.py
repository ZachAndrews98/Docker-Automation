""" Evaluation Data Management """

import matplotlib.pyplot as plt
# import numpy as np

TOOL_DATA = {
    "build_image_times": [],
    "build_image_ave": 0,
    "hello_world_times": [],
    "hello_world_ave": 0,
    "thread_build_image_times": [],
    "thread_build_image_ave": 0,
    "thread_hello_world_times": [],
    "thread_hello_world_ave": 0,
}

TERM_DATA = {
    "build_image_times": [],
    "build_image_ave": 0,
    "hello_world_times": [],
    "hello_world_ave": 0,
    "thread_build_image_times": [],
    "thread_build_image_ave": 0,
    "thread_hello_world_times": [],
    "thread_hello_world_ave": 0,
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
        TOOL_DATA["hello_world_ave"],
        xmin=0, xmax=len(TOOL_DATA["hello_world_times"]),
        label="Tool Average",
        color="red",
        linestyles="dashed"
    )
    ax1.hlines(
        TERM_DATA["hello_world_ave"],
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
        TOOL_DATA["build_image_ave"],
        xmin=0, xmax=len(TOOL_DATA["build_image_times"]),
        label="Tool Average",
        color="red",
        linestyles="dashed"
    )
    ax2.hlines(
        TERM_DATA["build_image_ave"],
        xmin=0, xmax=len(TERM_DATA["build_image_times"]),
        label="Terminal Average",
        color="blue",
        linestyles="dashed"
    )

    ax2.legend()

    fig3, ax3 = plt.subplots()
    fig3.suptitle("Run Times for Threaded Hello World Run")
    ax3.set_xlabel("Test Number")
    ax3.set_ylabel("Run Time (s)")

    # Run Times
    ax3.plot(
        list(range(0, len(TOOL_DATA["thread_hello_world_times"]))),
        TOOL_DATA["thread_hello_world_times"],
        label="Tool",
        color="red"
    )

    ax3.plot(
        list(range(0, len(TERM_DATA["thread_hello_world_times"]))),
        TERM_DATA["thread_hello_world_times"],
        label="Terminal",
        color="blue"
    )
    # Average Run Times
    ax3.hlines(
        TOOL_DATA["thread_hello_world_ave"],
        xmin=0, xmax=len(TOOL_DATA["thread_hello_world_times"]),
        label="Tool Average",
        color="red",
        linestyles="dashed"
    )
    ax3.hlines(
        TERM_DATA["thread_hello_world_ave"],
        xmin=0, xmax=len(TERM_DATA["thread_hello_world_times"]),
        label="Terminal Average",
        color="blue",
        linestyles="dashed"
    )

    ax3.legend()

    fig4, ax4 = plt.subplots()
    fig4.suptitle("Run Times for Threaded Image Building")
    ax4.set_xlabel("Test Number")
    ax4.set_ylabel("Run Time (s)")
    # Run Times
    ax4.plot(
        list(range(0, len(TOOL_DATA["thread_build_image_times"]))),
        TOOL_DATA["thread_build_image_times"],
        label="Tool",
        color="red"
    )

    ax4.plot(
        list(range(0, len(TERM_DATA["thread_build_image_times"]))),
        TERM_DATA["thread_build_image_times"],
        label="Terminal",
        color="blue"
    )
    # Average Run Times
    ax4.hlines(
        TOOL_DATA["thread_build_image_ave"],
        xmin=0, xmax=len(TOOL_DATA["thread_build_image_times"]),
        label="Tool Average",
        color="red",
        linestyles="dashed"
    )
    ax4.hlines(
        TERM_DATA["thread_build_image_ave"],
        xmin=0, xmax=len(TERM_DATA["thread_build_image_times"]),
        label="Terminal Average",
        color="blue",
        linestyles="dashed"
    )

    ax4.legend()

    plt.show()
