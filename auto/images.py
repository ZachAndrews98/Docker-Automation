""" Image Utilites """

import os
import subprocess
import time

import docker


def login(user, passwd):
    """ Login to Docker """
    client = docker.from_env()
    client.login(username=user, password=passwd)


def pull_image(image_name, tag="latest"):
    """ Pull a docker image """
    client = docker.from_env()
    return client.images.pull(image_name, tag=tag)
    # return client.images.pull(image_name)


def push_image(image_name, tag):
    """ Push a docker image """
    client = docker.from_env()
    if tag != "":
        client.images.push(image_name, tag=tag)
    else:
        client.images.push(image_name)


def build_image(directory, image_name):
    """ Builds an image based on the path to a Dockerfile """
    if os.path.exists(directory + "/Dockerfile"):
        client = docker.from_env()
        print("Building Image. This may take a while")
        start = time.time()
        client.images.build(path=directory, tag=str(image_name), rm=True)
        print("Buildtime: " + str((time.time() - start) / 60))
        return True
    else:
        print("No Dockerfile found")
        return False


def run_image(image_name, args=""):
    """ Runs a given image in a separate terminal """
    # if install_docker.PLATFORM == Linux:
    base_command = "docker run " + args + " " + image_name
    command = "gnome-terminal --command '" + base_command + "'"
    subprocess.call(command, shell=True)


def list_images(name="", all=False):
    """ Return the images on the machine """
    client = docker.from_env()
    raw_images = client.images.list(name=name, all=all)
    images = list()
    for image in raw_images:
        images.append(''.join(image.tags))
    if images != []:
        return images
    return None


def delete_image(images):
    """ Delete a given image(s) from the machine """
    client = docker.from_env()
    for image in images:
        try:
            client.images.remove(image)
        except BaseException:
            print("Unable to remove image: " + image)


if __name__ == "__main__":
    print(isinstance(pull_image("hello-world"), docker.models.images.Image))
