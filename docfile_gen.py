import os
import sys
import re
import time

import docker

FILE_REGEX = '^[a-zA-Z0-9_]+\.[a-zA-Z0-9]+$'

file_types = {
    "py": "python3",
    "java": "default-jdk",
    "js": "nodejs",
    "c": "gcc",
    "cs": "gcc",
    "cpp": "gcc",
    'rb': "ruby-full",
    'go': "golang",
}


def get_file_types(directory):
    types = set()
    for root, dirs, files in os.walk("./" + directory):
        for name in files:
            if re.match(FILE_REGEX,name):
                print(name)
                ext = name.split('.')[1]
                if ext not in types:
                    types.add(ext)
    print("Detected:")
    for type in types:
        try:
            print("\t",file_types[type])
        except:
            print("\t #Unknown Extension: "+type)
    return types


def generate_dockerfile(directory):
    BASE_IMAGE = "debian:bullseye"
    DIRECTORY = directory
    EXTS = get_file_types(directory)
    INSTALLS = ""
    for ext in EXTS:
        try:
            INSTALLS += file_types[ext] + " "
        except:
            pass
    print(INSTALLS)
    try:
        docfile = open("./" + directory + "/Dockerfile", "w+")
    except FileExistsError:
        print("File Already Exists")
        sys.quit()
    docfile.write("FROM " + BASE_IMAGE + "\n\n")
    docfile.write("ADD ./ test/" + "\n\n")
    docfile.write(
        "RUN apt update && apt upgrade -y && \\\n" + \
        "apt install " + INSTALLS + "-y" + "\n\n"
    )
    docfile.write("CMD cd test && chmod +x testPrograms.sh && ./testPrograms.sh")
    docfile.close()


def build_image(directory):
    client = docker.from_env()
    start = time.time()
    client.images.build(path=directory, tag="test", rm=True)
    print("Buildtime: " + str((time.time() - start)/60))


def run_image(image_name):
    os.system("gnome-terminal --command 'docker run -it --rm " + image_name + "'")


directory = str(input("Enter directory\n"))
generate_dockerfile(directory)
print("Building Image. This may take a while")
build_image(directory)
run_image(str(input("Image Name: ")))
