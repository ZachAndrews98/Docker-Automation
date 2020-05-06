""" Main file for running docker installation, generation, and gui """

from auto import generate, images, containers

# List of valid commands
COMMAND_LIST = [
    "generate",
    "build",
    "run",
    "exit",
    "quit",
    "delete",
    "list",
    "help",
    "pull",
    "stop",
    "kill",
    "push",
    "login",
    "restart",
    "connect",
]


def repl():
    """ Interactive command system """
    # Get command entered in terminal
    command = str(input(">> ")).split(' ')
    # Ensure command is valid
    while command[0] not in COMMAND_LIST:
        print("That is not a valid command")
        command = str(input(">> "))
    # Check if command was to exit or quit
    if command[0] != "exit" and command[0] != "quit":
        # Generate command entered
        if command[0] == "generate":
            directory = str(input("Input path to directory:\n"))
            to_dir = str(
                input(
                    "Input location to mount files (default:project/):")
                ).strip()
            if to_dir != "":
                generate.generate_dockerfile(directory, to_dir=to_dir)
            else:
                generate.generate_dockerfile(directory)
        # Build command entered
        elif command[0] == "build":
            # Check if image or container entered with command
            if len(command) < 2 or command[1] not in ("image", "container"):
                build_type = str(input("Build image or container: "))
                while build_type not in ("image", "container"):
                    build_type = str(input("Build image or container: "))
            else:
                build_type = command[1]
            # Build image
            if build_type == "image":
                images.build_image(
                    str(input("Input path to directory:\n")),
                    str(input("Input image name: "))
                )
            # Build container
            elif build_type == "container":
                containers.build_container(
                    str(input("Image to build container: ")),
                    str(input("Arguments: "))
                )
        # Run command entered
        elif command[0] == "run":
            # Check if image or container entered with command
            if len(command) < 2 or command[1] not in ("image", "container"):
                run_type = str(input("Run image or container: "))
                while run_type not in ("image", "container"):
                    run_type = str(input("Run image or container: "))
            else:
                run_type = command[1]
            # Run image
            if run_type == "image":
                image_name = str(input("Image Name: "))
                args = str(input("Arguments: "))
                if args != "":
                    images.run_image(image_name, args=args)
                else:
                    images.run_image(image_name)
            # Run container
            elif run_type == "container":
                container_name = str(input("Container Name: "))
                args = str(input("Arguments: "))
                if args != "":
                    containers.run_container(container_name, args=args)
                else:
                    containers.run_container(container_name)
        # Connect command entered
        elif command[0] == "connect":
            container_name = str(input("Container to connect to: "))
            arguments = str(input("Arguments to pass: "))
            command = str(input("Command to run: "))
            containers.connect_container(
                container_name, args=arguments, command=command
            )
        # Delete command entered
        elif command[0] == "delete":
            # Check if image or container entered with command
            if len(command) < 2 or command[1] not in ("image", "container"):
                remove_type = str(input("Delete image or container: "))
                while remove_type not in ("image", "container"):
                    remove_type = str(input("Remove image or container: "))
            else:
                remove_type = command[1]
            # Delete image
            if remove_type == "image":
                image_name = str(input("Image to remove: ")).strip().split(',')
                images.delete_image(image_name)
            # Delete container
            elif remove_type == "container":
                container_name = str(
                    input("Container to remove: ")
                ).strip().split(',')
                containers.delete_container(container_name)
        # List command entered
        elif command[0] == "list":
            # Check if image or container entered with command
            if len(command) < 2 or command[1] not in ("images", "containers"):
                list_type = str(input("List images or containers: "))
                while list_type not in ("images", "containers"):
                    list_type = str(input("List images or containers: "))
            else:
                list_type = command[1]
            # List images
            if list_type == "images":
                images = images.list_images()
                if images is not None:
                    for image in images:
                        print(image)
                else:
                    print("None")
            # List containers
            elif list_type == "containers":
                containers = containers.list_containers()
                if containers is not None:
                    for container in containers:
                        print(container)
                else:
                    print("None")

        repl()
    return 0
