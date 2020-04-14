""" Evaluation Data Management """

import matplotlib.pyplot as plt
# import numpy as np

TOOL_DATA = {
    "build_image_times": [],
    "build_image_ave": 0,
    "hello_world_times": [],
    "hello_world_ave": 0,
    "thread_build_image_times": [],
    "thread_build_image_ave": [],
    "thread_build_image_threads": [],
    "thread_hello_world_times": [],
    "thread_hello_world_ave": [],
    "thread_hello_world_threads": [],
}

TERM_DATA = {
    "build_image_times": [],
    "build_image_ave": 0,
    "hello_world_times": [],
    "hello_world_ave": 0,
    "thread_build_image_times": [],
    "thread_build_image_ave": [],
    "thread_build_image_threads": [],
    "thread_hello_world_times": [],
    "thread_hello_world_ave": [],
    "thread_hello_world_threads": [],
}

GENERATE_DATA = {
    "output": [],
    "num_tests": 0,
    "num_correct": 0,
    "num_incorrect": 0
}


def write_data():
    """ Write gathered data to output file"""
    out_file = open("./evaluator/output.txt", "w+")

    out_file.write("\nIMAGE BUILDING EVALUATION DATA\n")
    out_file.write("\tTOOL TIMES\n")
    out_file.write("\t\tTimes:" + str(TOOL_DATA["build_image_times"]) + "\n")
    out_file.write(
        "\t\tAverage Time:" + str(TOOL_DATA["build_image_ave"]) + "\n"
    )
    out_file.write("\tTERMINAL TIMES\n")
    out_file.write("\t\tTimes:" + str(TERM_DATA["build_image_times"]) + "\n")
    out_file.write(
        "\t\tAverage Time:" + str(TERM_DATA["build_image_ave"]) + "\n"
    )

    out_file.write("\nHELLO WORLD EVALUATION DATA")
    out_file.write("\tTOOL TIMES\n")
    out_file.write("\t\tTimes:" + str(TOOL_DATA["hello_world_times"]) + "\n")
    out_file.write(
        "\t\tAverage Time:" + str(TOOL_DATA["hello_world_ave"]) + "\n"
    )
    out_file.write("\tTERMINAL TIMES\n")
    out_file.write("\t\tTimes:" + str(TERM_DATA["hello_world_times"]) + "\n")
    out_file.write(
        "\t\tAverage Time:" + str(TERM_DATA["hello_world_ave"]) + "\n"
    )

    out_file.write("\nTHREADED IMAGE BUILDING EVALUATION DATA\n")
    out_file.write(
        "Number of Threads List:" + str(
            TOOL_DATA["thread_build_image_threads"]
        ) + "\n"
    )
    out_file.write("\tTOOL TIMES\n")
    out_file.write(
        "\t\tTimes:" + str(TOOL_DATA["thread_build_image_times"]) + "\n"
    )
    out_file.write(
        "\t\tAverage Time:" + str(TOOL_DATA["thread_build_image_ave"]) + "\n"
    )
    out_file.write("\tTERMINAL TIMES\n")
    out_file.write(
        "\t\tTimes:" + str(TERM_DATA["thread_build_image_times"]) + "\n"
    )
    out_file.write(
        "\t\tAverage Time:" + str(TERM_DATA["thread_build_image_ave"]) + "\n"
    )

    out_file.write("\nTHREADED HELLO WORLD EVALUATION DATA\n")
    out_file.write(
        "Number of Threads List:" + str(
            TOOL_DATA["thread_hello_world_threads"]
        ) + "\n"
    )
    out_file.write("\tTOOL TIMES\n")
    out_file.write(
        "\t\tTimes:" + str(TOOL_DATA["thread_hello_world_times"]) + "\n"
    )
    out_file.write(
        "\t\tAverage Time:" + str(TOOL_DATA["thread_hello_world_ave"]) + "\n"
    )
    out_file.write("\tTERMINAL TIMES\n")
    out_file.write(
        "\t\tTimes:" + str(TERM_DATA["thread_hello_world_times"]) + "\n"
    )
    out_file.write(
        "\t\tAverage Time:" + str(TERM_DATA["thread_hello_world_ave"]) + "\n"
    )

    out_file.write("\nDOCKERFILE GENERATOR EVALUATION DATA\n")
    for line in GENERATE_DATA["output"]:
        if line != "\n":
            out_file.write("\t" + line + "\n")
        else:
            out_file.write("\t" + line)
    out_file.write(
        "\tEvaluated " + str(GENERATE_DATA["num_tests"]) + " Images\n"
    )
    out_file.write(
        "\t\t" + str(GENERATE_DATA["num_correct"]) + " Worked Properly\n"
    )
    out_file.write(
        "\t\t" + str(GENERATE_DATA["num_incorrect"]) + " Worked Improperly\n"
    )
    out_file.close()


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
    ax3.set_xlabel("Number of Simulataneous Runs")
    ax3.set_ylabel("Run Time (s)")

    # Run Times
    ax3.plot(
        TOOL_DATA["thread_hello_world_threads"],
        TOOL_DATA["thread_hello_world_times"],
        label="Tool",
        color="red"
    )

    ax3.plot(
        TERM_DATA["thread_hello_world_threads"],
        TERM_DATA["thread_hello_world_times"],
        label="Terminal",
        color="blue"
    )

    # Average Run Times
    ax3.hlines(
        TOOL_DATA["thread_hello_world_ave"],
        xmin=TOOL_DATA["thread_hello_world_threads"][0],
        xmax=TOOL_DATA["thread_hello_world_threads"][len(
            TOOL_DATA["thread_hello_world_threads"]
        ) - 1],
        label="Tool Average",
        color="red",
        linestyles="dashed"
    )
    ax3.hlines(
        TERM_DATA["thread_hello_world_ave"],
        xmin=TERM_DATA["thread_hello_world_threads"][0],
        xmax=TERM_DATA["thread_hello_world_threads"][len(
            TERM_DATA["thread_hello_world_threads"]
        ) - 1],
        label="Terminal Average",
        color="blue",
        linestyles="dashed"
    )

    ax3.legend()

    fig4, ax4 = plt.subplots()
    fig4.suptitle("Run Times for Threaded Image Building")
    ax4.set_xlabel("Number of Simulataneous Builds")
    ax4.set_ylabel("Run Time (s)")
    # Run Times
    ax4.plot(
        TOOL_DATA["thread_build_image_threads"],
        TOOL_DATA["thread_build_image_times"],
        label="Tool",
        color="red"
    )

    ax4.plot(
        TERM_DATA["thread_build_image_threads"],
        TERM_DATA["thread_build_image_times"],
        label="Terminal",
        color="blue"
    )
    # Average Run Times
    ax4.hlines(
        TOOL_DATA["thread_build_image_ave"],
        xmin=TOOL_DATA["thread_build_image_threads"][0],
        xmax=TOOL_DATA["thread_build_image_threads"][len(
            TOOL_DATA["thread_build_image_threads"]
        ) - 1],
        label="Tool Average",
        color="red",
        linestyles="dashed"
    )
    ax4.hlines(
        TERM_DATA["thread_build_image_ave"],
        xmin=TERM_DATA["thread_build_image_threads"][0],
        xmax=TERM_DATA["thread_build_image_threads"][len(
            TERM_DATA["thread_build_image_threads"]
        ) - 1],
        label="Terminal Average",
        color="blue",
        linestyles="dashed"
    )

    ax4.legend()

    plt.show()
