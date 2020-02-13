# Docker Installation and Setup Automation [![Build Status](https://travis-ci.com/ZachAndrews98/Docker-Automation.svg?branch=master)](https://travis-ci.com/ZachAndrews98/Docker-Automation)

## Description:

A software tool for automating the installation and setup of Docker on a given
machine. This tool is currently proven to work on Linux, primarily Ubuntu,
though there is hypothetical support for CentOS, Debian, Fedora, and MacOS.

## Installation:

### Requirements:

In order to install this program there are several requirements that must be
met which are listed below.

- Python (3.6 or up)
- Pipenv (Handles required packages)

Once the requirements have been met, this tool can be installed by cloning the
repository to anywhere on your host machine and running the following command
`pipenv install` This command will install all required packages for the tool
to operate correctly. To run the actual tool use the command `pipenv run
python3 main.py`. This command will generate a Flask page hosted at
`localhost:5000` which currently has most of the functions that the command line
does. If you do not want to use the graphical interface just append the flag
`--terminal` on the end of the previous command.

## Usage:

Currently there are three commands available in the built in Repl system, which
can be seen below with appropriate descriptions of each.

- `generate`: Generates a Dockerfile for an inputted directory and places the file in the directory.

- `build`: Builds an images based on a path to a directory with a Dockerfile and will give it a user specified name.

- `run <image/container>`: Runs an image or container and any supplied arguments in a separate terminal window.

- `list <images/containers>`: List all of the images or containers that are installed on the current machine.

- `delete <image/container>`: Delete the specified image(s) or container(s) that is installed on the current machine. If you would like to delete more than one image or container separate the list with `,`.
