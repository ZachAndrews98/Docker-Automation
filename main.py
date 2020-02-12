""" Run Docker Automation and Setup Program """
import sys

from auto import docker_auto

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--terminal":
        docker_auto.main()
    else:
        docker_auto.main()
