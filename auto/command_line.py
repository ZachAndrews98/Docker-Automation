""" Interpret command line arguments and run commands """


def command_line(args):
    """ Run functions via command line arguments """
    from auto import generate, images, containers
    if args.build:
        if args.image:
            if args.path and args.name:
                images.build_image(args.path, args.name)
            else:
                return "Additional flags required"
        elif args.container:
            if args.name and args.args:
                containers.build_container(args.name, args.args)
            else:
                return "Additional flags required"
        else:
            return "Additional flags required"
    elif args.generate:
        if args.image:
            if args.path and args.dest:
                generate.generate_dockerfile(args.path, args.dest)
    elif args.list:
        if args.image:
            print(images.list_images())
        elif args.container:
            print(containers.list_containers())
        else:
            return "Additional flags required"
    elif args.run:
        if args.image:
            if args.args and args.name:
                images.run_image(args.name, args.args)
            elif args.name:
                images.run_image(args.name)
            else:
                return "Additional flags required"
        elif args.container:
            if args.args and args.name:
                containers.run_container(args.name, ', '.join(args.args))
            elif args.name:
                containers.run_container(args.name)
            else:
                return "Additional flags required"
        else:
            return "Additional flags required"
    elif args.delete:
        if args.image:
            if args.name:
                images.delete_image(args.name)
            elif args.names:
                images.delete_image(args.names[0])
            else:
                return "Additional flags required"
        elif args.container:
            if args.name:
                containers.delete_container(args.name)
            elif args.names:
                containers.delete_container(args.names[0])
            else:
                return "Additional flags required"
        else:
            return "Additional flags required"
    elif args.login:
        if args.username and args.password:
            images.login(args.username, args.password)
        else:
            return "Additional flags required"
    elif args.pull:
        if args.name and args.tag:
            images.pull_image(args.name, tag=args.tag)
        else:
            return "Additional flags required"
    elif args.push:
        if args.name and args.tag:
            images.push_image(args.name, args.tag)
        else:
            return "Additional flags required"
    elif args.kill:
        if args.name:
            containers.kill_container(args.name)
        else:
            return "Additional flags required"
    elif args.stop:
        if args.name:
            containers.stop_container(args.name)
        else:
            return "Additional flags required"
    elif args.restart:
        if args.name:
            containers.restart_container(args.name)
        else:
            return "Additional flags required"
