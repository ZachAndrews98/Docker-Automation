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
            docfile_gen.generate_dockerfile(str(input("Input path to directory:\n")))

        repl(str(input(">> ")))


if __name__ == "__main__":
    main()
