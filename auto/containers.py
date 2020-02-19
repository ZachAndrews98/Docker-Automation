""" Container Utilites """

import os
import subprocess

import docker


def run_container(container_name, args=""):
    """ Runs a given container in a separate terminal """
    base_command = "docker start " + args + " " + container_name
    command = "gnome-terminal --command '" + base_command + "'"
    subprocess.call(command, shell=True)


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


def kill_container(container_name):
    """ Kill a running container """
    client = docker.from_env()
    container = client.containers.get(container_name)
    container.kill()


def stop_container(container_name):
    """ Stop a running container """
    client = docker.from_env()
    container = client.containers.get(container_name)
    container.stop()


def restart_container(container_name):
    """ Restart a container """
    client = docker.from_env()
    container = client.containers.get(container_name)
    container.restart()


def create_container(image_name, args):
    """ Create a container, but do not run it """
    client = docker.from_env()
    return isinstance(client.containers.create(image_name, command=args),
                docker.models.containers.Container)


def delete_container(containers):
    """ Delete a given container(s) from the machine """
    client = docker.from_env()
    for container in containers:
        try:
            client.containers.get(container.strip()).remove()
        except BaseException:
            print("Unable to delete: " + container)
