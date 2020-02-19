""" Main file for running docker installation, generation, and gui """
import sys

from auto import install, generate, images, containers

COMMAND_LIST = ["generate", "build", "run", "exit", "quit", "delete", "list"]


def repl():
    """ Interactive command system """
    command = str(input(">> ")).split(' ')
    while command[0] not in COMMAND_LIST:
        print("That is not a valid command")
        command = str(input(">> "))

    if command[0] != "exit" and command[0] != "quit":
        if command[0] == "generate":
            directory = get_directory()
            to_dir = str(
                input("Input location to mount files (default:test):")).strip()
            if to_dir != "":
                generate.generate_dockerfile(directory, to_dir=to_dir)
            else:
                generate.generate_dockerfile(directory)

        elif command[0] == "build":
            images.build_image(
                get_directory(), str(
                    input("Input image name: ")))

        elif command[0] == "run":
            if len(command) < 2 or command[1] not in ("image", "container"):
                run_type = str(input("Run image or container: "))
                while run_type not in ("image", "container"):
                    run_type = str(input("Run image or container: "))
            else:
                run_type = command[1]

            if run_type == "image":
                image_name = str(input("Image Name: "))
                args = str(input("Arguments: "))
                if args != "":
                    images.run_image(image_name, args=args)
                else:
                    images.run_image(image_name)
            elif run_type == "container":
                container_name = str(input("Container Name: "))
                args = str(input("Arguments: "))
                if args != "":
                    containers.run_container(container_name, args=args)
                else:
                    containers.run_container(container_name)

        elif command[0] == "delete":
            if len(command) < 2 or command[1] not in ("image", "container"):
                remove_type = str(input("Delete image or container: "))
                while remove_type not in ("image", "container"):
                    remove_type = str(input("Remove image or container: "))
            else:
                remove_type = command[1]

            if remove_type == "image":
                image_name = str(input("Image to remove: ")).strip(),split(',')
                images.delete_image(image_name)
            elif remove_type == "container":
                container_name = str(input("Container to remove: ")).strip().split(',')
                containers.delete_container(container_name)

        elif command[0] == "list":
            if len(command) < 2 or command[1] not in ("images", "containers"):
                list_type = str(input("List images or containers: "))
                while list_type not in ("images", "containers"):
                    list_type = str(input("List images or containers: "))
            else:
                list_type = command[1]

            if list_type == "images":
                images = images.list_images()
                if images is not None:
                    for image in images:
                        print(image)
                else:
                    print("None")
            elif list_type == "containers":
                containers = containers.list_containers()
                if containers is not None:
                    for container in containers:
                        print(container)
                else:
                    print("None")

        repl()
    return 0


def get_directory():
    """ Returns an inputted directory """
    return str(input("Input path to directory:\n"))
