""" Analyze and generate a Dockerfile for an inputted directory """
import os
import sys
import re
import time

import docker

# pylint: disable=W1401
FILE_REGEX = r'^[a-zA-Z0-9_]+\.[a-zA-Z0-9]+$'

FILE_TYPES = {
    "py": "python3",
    "java": "default-jdk",
    "js": "nodejs",
    "c": "gcc",
    "cs": "gcc",
    "cpp": "gcc",
    'rb': "ruby-full",
    'go': "golang",
}


def get_file_types(directory):
    """ grabs the filetypes in a directory based on file extension """
    filetypes = set()
    for _, _, files in os.walk("./" + directory):
        for name in files:
            if re.match(FILE_REGEX, name):
                print(name)
                ext = name.split('.')[1]
                if ext not in filetypes:
                    filetypes.add(ext)
    print("Detected:")
    for filetype in filetypes:
        try:
            print("\t", FILE_TYPES[filetype])
        # pylint: disable=W0703
        except BaseException:
            print("\t #Unknown Extension: " + filetype)
    return filetypes


def generate_dockerfile(directory, to_dir="test"):
    """ Creates a Dockerfile based on detected filetypes """
    base_image = "debian:bullseye"
    exts = get_file_types(directory)
    installs = ""
    for ext in exts:
        try:
            installs += FILE_TYPES[ext] + " "
        # pylint: disable=W0703
        except BaseException:
            pass
    try:
        docfile = open("./" + directory + "/Dockerfile", "w+")
    except FileExistsError:
        print("File Already Exists")
        sys.exit()
    docfile.write("FROM " + base_image + "\n\n")
    docfile.write("ADD ./ " + to_dir + "/" + "\n\n")
    docfile.write(
        "RUN apt update && apt upgrade -y && \\\n" +
        "apt install " + installs + "-y" + "\n\n"
    )
    docfile.write(
        "CMD cd test && chmod +x testPrograms.sh && ./testPrograms.sh")
    docfile.close()


def build_image(directory, image_name):
    """ Builds an image based on the path to a Dockerfile """
    client = docker.from_env()
    print("Building Image. This may take a while")
    start = time.time()
    client.images.build(path=directory, tag=str(image_name), rm=True)
    print("Buildtime: " + str((time.time() - start) / 60))


def run_image(image_name, args=""):
    """ Runs a given image in a separate terminal """
    os.system(
        "gnome-terminal --command 'docker run -it --rm " +
        image_name +
        " " +
        args +
        "'")
