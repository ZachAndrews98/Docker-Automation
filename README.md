# Docker Installation and Setup Automation [![Build Status](https://travis-ci.com/ZachAndrews98/Docker-Automation.svg?branch=master)](https://travis-ci.com/ZachAndrews98/Docker-Automation)

## Description:

A software tool for automating the installation and setup of Docker on a given
machine. This tool is currently proven to work on Linux, primarily Ubuntu,
though there is hypothetical support for CentOS, Debian, Fedora, and MacOS.

## Installation:

### Requirements:

In order to install this program there are several requirements that must be
met which are listed below.

- Python (3.7 or up)
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

### Graphical Interface

The main way this tool is designed to be used is via the browser based user interface. This interface utilizes Python Flask which is automatically installed with the other requirements as described in the Requirements section of the README. This interface as previously mentioned is hosted at localhost:5000 and is automatically opened in the default browser once the Flask server is running.

### Command Line Interface

In addition to the graphical interface there is also a Terminal based system which offers all of the same functions of the graphical interface within the command line. In order to use this system the user must supply the `--terminal` flag at the end of the run command.

The commands for each function is listed below with a short description of what it does.

- `generate`: Generates a Dockerfile for an inputted directory and places the file in the directory.

- `build`: Builds an images based on a path to a directory with a Dockerfile and will give it a user specified name.

- `run <image/container>`: Runs an image or container and any supplied arguments in a separate terminal window.

- `list <images/containers>`: List all of the images or containers that are installed on the current machine.

- `delete <image/container>`: Delete the specified image(s) or container(s) that is installed on the current machine. If you would like to delete more than one image or container separate the list with `,`.

- `login`: Allows the user to login to Dockerhub, completely optional and only has an effect on pushing Images to Dockerhub.

- `pull`: Allows a user to download an Image to the user's machine.

- `push`: Allows a user to upload an Image to Dockerhub.

- `kill`: Force stop a Container that is running.

- `stop`: Stop a Container that is running.

- `restart`: Restart a stopped or killed Container.


### Command Line Arguments

An additional way to interact with the tool is via command line arguments. Each of these arguments corresponds to a different base command and the additional arguments that may be required to execute a desired command. Each command and the possible/required additional flags can be seen below.

#### Base Commands Flags

- `--build`:  Build either an Image or Container. Requires `--image` or `--container` flags. Additional flags are required for `--image` and `--container`. If `--image` is supplied, `--path` and `--name` are required. If `--container` is supplied, `--name` and `--args` are required.

- `--generate`: Generate a Dockerfile. Requires `--path` and `--dest` flags.

- `--list`: List either Images or Containers on the machine. Requires `--image` or `--container` flags.

- `--run`: Run either an Image or a Container. Requires `--image` or `--container` with an additional `--name` flag. Optionally, the user can also supply a `--args` flag with any run time arguments they would like to supply.

- `--delete`: Delete either an Image or a Container. Requires `--image` or `--container` flags. Also required is either `--name` or `--names` to supply either a single Image or Container to be deleted or a list of Images or Containers to be deleted.

- `--login`: Login to Dockerhub. Requires `--username` and `--password` flags.

- `--pull`: Pull an Image from Dockerhub. Requires `--name` and `--tag` flags.

- `--push`: Push an Image to Dockerhub. Requires `--name` and `--tag` flags.

- `--kill`: Kill a running Container. Requires `--name` flag.

- `--stop`: Stop a running Container. Requires `--name` flag.

- `--restart`: Restart a stopped or killed Container. Requires `--name` flag.


#### Advanced Command Flags

- `--no-install`: Skip the installation check/process.

- `--threaded`: Do not run the program on a separate thread in the background.

- `--sep`: Do not run the image in a new terminal window.
