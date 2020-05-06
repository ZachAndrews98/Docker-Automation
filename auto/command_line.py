""" Interpret command line arguments and run commands """

from auto import generate, images, containers, install


def command_line(args):
    """ Run functions via command line arguments """
    # Build command entered
    if args.build:
        # Checks to ensure required information given before calling function
        if args.image:
            # Building image
            if args.path and args.name:
                images.build_image(
                    args.path, args.name, threaded=args.threaded
                )
            else:
                return "Additional flags required"
        elif args.container:
            # Building container
            if args.name and args.args:
                containers.build_container(args.name, args.args)
            else:
                return "Additional flags required"
        else:
            return "Additional flags required"
    # Generate command entered
    elif args.generate:
        # Checks to ensure required information given before calling function
        if args.path and args.dest:
            return generate.generate_dockerfile(args.path, args.dest)
        return "Additional flags required"
    # List command entered
    elif args.list:
        # Checks to ensure required information given before calling function
        if args.image:
            # List images
            return images.list_images()
        if args.container:
            # List containers
            return containers.list_containers()
        return "Additional flags required"
    # Run command entered
    elif args.run:
        # Checks to ensure required information given before calling function
        if args.image:
            # Run image
            if args.args and args.name:
                images.run_image(args.name, args=args.args, sep=args.sep)
            elif args.name:
                images.run_image(args.name, sep=args.sep)
            else:
                return "Additional flags required"
        elif args.container:
            # Run container
            if args.args and args.name:
                containers.run_container(
                    args.name, args=args.args, sep=args.sep
                )
            elif args.name:
                containers.run_container(args.name, sep=args.sep)
            else:
                return "Additional flags required"
        else:
            return "Additional flags required"
    # Delete command entered
    elif args.delete:
        # Checks to ensure required information given before calling function
        if args.image:
            # Delete image
            if args.name:
                images.delete_image(args.name)
            elif args.names:
                images.delete_image(args.names[0])
            else:
                return "Additional flags required"
        elif args.container:
            # Delete container
            if args.name:
                containers.delete_container(args.name)
            elif args.names:
                containers.delete_container(args.names[0])
            else:
                return "Additional flags required"
        else:
            return "Additional flags required"
    # Login command entered
    elif args.login:
        # Checks to ensure required information given before calling function
        if args.username and args.password:
            images.login(args.username, args.password)
        else:
            return "Additional flags required"
    # Pull command entered
    elif args.pull:
        # Checks to ensure required information given before calling function
        if args.name and args.tag:
            images.pull_image(args.name, tag=args.tag)
        else:
            return "Additional flags required"
    # Push command entered
    elif args.push:
        # Checks to ensure required information given before calling function
        if args.name and args.tag:
            images.push_image(args.name, args.tag)
        else:
            return "Additional flags required"
    # Kill command entered
    elif args.kill:
        # Checks to ensure required information given before calling function
        if args.name:
            containers.kill_container(args.name)
        else:
            return "Additional flags required"
    # Stop command entered
    elif args.stop:
        # Checks to ensure required information given before calling function
        if args.name:
            containers.stop_container(args.name)
        else:
            return "Additional flags required"
    # Restart command entered
    elif args.restart:
        # Checks to ensure required information given before calling function
        if args.name:
            containers.restart_container(args.name)
        else:
            return "Additional flags required"
