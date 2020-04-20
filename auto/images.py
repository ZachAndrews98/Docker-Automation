""" Image Utilites """

import os
import subprocess
import threading

import docker

CLIENT = docker.from_env()


def login(user, passwd):
    """ Login to Docker """
    return CLIENT.login(username=user, password=passwd)


def pull_image(image_name, tag="latest"):
    """ Pull a docker image """
    return CLIENT.images.pull(image_name, tag=tag)


def push_image(image_name, tag):
    """ Push a docker image """
    if tag != "":
        CLIENT.images.push(image_name, tag=tag)
    else:
        CLIENT.images.push(image_name)


def build_image(directory, image_name, threaded=True):
    """ Builds an image based on the path to a Dockerfile """
    directory = os.getenv('HOME') + "/" + directory
    if os.path.exists(directory + "/Dockerfile"):
        print("Building Image. This may take a while")
        if threaded:
            thread = threading.Thread(
                target=build_thread, args=(directory, image_name)
            )
            thread.start()
            return True
        build_thread(directory, image_name)
        return True
    print("No Dockerfile found in " + directory)
    return False


def build_thread(directory, image_name):
    """ Creates thread for building images """
    CLIENT.images.build(path=directory, tag=str(image_name), rm=True)


def run_image(image_name, args="", sep=True):
    """ Runs a given image in a separate terminal """
    base_command = "docker run " + args + " " + image_name
    if sep:
        command = "gnome-terminal --command '" + base_command + "'"
    else:
        command = base_command
    return subprocess.call(command, shell=True)


# pylint: disable=W0622
def list_images(name="", all=False):
    """ Return the images on the machine """
    raw_images = CLIENT.images.list(name=name, all=all)
    images = list()
    for image in raw_images:
        if image.tags is not None:
            images.append(''.join(image.tags))
    if images != []:
        return images
    return None


def delete_image(images):
    """ Delete a given image(s) from the machine """
    for image in images:
        try:
            CLIENT.images.remove(image)
        except BaseException:
            print("Unable to remove image: " + image)
