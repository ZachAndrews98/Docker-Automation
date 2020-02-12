""" Docker utilites """

import os
import subprocess
import time

import docker

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


def run_container(container_name, args=""):
    """ Runs a given container in a separate terminal """
    base_command = "docker start " + args + " " + container_name
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


def list_containers(filters={}, all=True):
    """ Return the conatiners on the machine """
    client = docker.from_env()
    raw_containers = client.containers.list(filters={}, all=all)
    containers = list()
    for container in raw_containers:
        containers.append(container.name)
    if containers != []:
        return containers
    return None


def delete_image(images):
    """ Delete a given image(s) from the machine """
    client = docker.from_env()
    for image in images:
        try:
            client.images.remove(image)
        except BaseException:
            return "Unable to remove image: " + image_name + " must force"
    


def delete_container(containers):
    """ Delete a given container(s) from the machine """
    client = docker.from_env()
    for container in containers:
        try:
            client.containers.get(container).remove()
        except BaseException:
            pass
