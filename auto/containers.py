""" Container Utilites """

import subprocess

import docker

CLIENT = docker.from_env()


def run_container(container_name, args="", sep=True):
    """ Runs a given container in a separate terminal """
    base_command = "docker start " + args + " " + container_name
    if sep:
        command = "gnome-terminal --command '" + base_command + "'"
    else:
        command = base_command
    subprocess.call(command, shell=True)


def connect_container(container_name, args="", command="", sep=True):
    """ Connect to a given running container """
    base_command = "docker exec " + args + " " + container_name + " " + command
    if sep:
        command = "gnome-terminal --command '" + base_command + "'"
    else:
        command = base_command
    subprocess.call(command, shell=True)

# pylint: disable=W0622, W0102
def list_containers(filters=dict(), all=True):
    """ Return the conatiners on the machine """
    raw_containers = CLIENT.containers.list(filters=filters, all=all)
    containers = list()
    for container in raw_containers:
        containers.append(container.name)
    if containers != []:
        return containers
    return None


def kill_container(container_name):
    """ Kill a running container """
    container = CLIENT.containers.get(container_name)
    container.kill()


def stop_container(container_name):
    """ Stop a running container """
    container = CLIENT.containers.get(container_name)
    container.stop()


def restart_container(container_name):
    """ Restart a container """
    container = CLIENT.containers.get(container_name)
    container.restart()


def build_container(image_name, args):
    """ Create a container, but do not run it """
    return isinstance(CLIENT.containers.create(image_name, command=args),
                      docker.models.containers.Container)


def delete_container(containers):
    """ Delete a given container(s) from the machine """
    for container in containers:
        try:
            CLIENT.containers.get(container.strip()).remove()
        # pylint: disable=W0703
        except BaseException:
            print("Unable to delete: " + container)
