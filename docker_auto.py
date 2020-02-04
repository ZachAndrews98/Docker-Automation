""" Main file for running docker installation, generation, and gui """
import install_docker
import docfile_gen


def main():
    """ Installs Docker and enters command system """
    print(install_docker.install())
    repl(str(input(">> ")))


def repl(command):
    """ Interactive command system """
    print(command)
    if command != ("exit", "quit"):
        args = command.split(' ')
        if args[0] == "generate":
            directory = get_directory()
            to_dir = str(
                input("Input location to mount files (default:test):")).strip()
            if to_dir != "":
                docfile_gen.generate_dockerfile(directory, to_dir=to_dir)
            else:
                docfile_gen.generate_dockerfile(directory)
        if args[0] == "build":
            docfile_gen.build_image(
                get_directory(), str(
                    input("Input image name: ")))
        if args[0] == "run":
            image_name = str(input("Image Name: "))
            args = str(input("Arguments: ")).strip()
            if args != "":
                docfile_gen.run_image(image_name, args=args)
            else:
                docfile_gen.run_image(image_name)
        repl(str(input(">> ")))


def get_directory():
    """ Returns an inputted directory """
    return str(input("Input path to directory:\n"))


if __name__ == "__main__":
    main()
