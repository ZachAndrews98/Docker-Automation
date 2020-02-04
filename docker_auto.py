import install_docker
import docfile_gen

def main():
    print(install_docker.install())
    repl(str(input(">> ")))


def repl(command):
    print(command)
    if command != "exit" and command != "quit":
        args = command.split(' ')
        if args[0] == "generate":
            dir = get_directory()
            to_dir = str(input("Input location to mount files (default:test):")).strip()
            if to_dir != "":
                print("empt")
                docfile_gen.generate_dockerfile(dir, to_dir=to_dir)
            else:
                print("not")
                docfile_gen.generate_dockerfile(dir)
        if args[0] == "build":
            docfile_gen.build_image(get_directory(),str(input("Input image name: ")))
        if args[0] == "run":
            image_name = str(input("Image Name: "))
            args = str(input("Arguments: ")).strip()
            if args != "":
                docfile_gen.run_image(image_name, args=args)
            else:
                docfile_gen.run_image(image_name)
        repl(str(input(">> ")))


def get_directory():
    pass
    return str(input("Input path to directory:\n"))

if __name__ == "__main__":
    main()
