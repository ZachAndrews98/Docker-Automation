""" Analyze and generate a Dockerfile for an inputted directory """

import os
import re

FILE_REGEX = r'^[a-zA-Z0-9_]+\.[a-zA-Z0-9]+$'

FILE_TYPES = {
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
    """ grabs the filetypes in a directory based on file extension """
    filetypes = set()
    for _, _, files in os.walk(os.getenv('HOME') + "/" + directory):
        # print(files)
        for name in files:
            if re.match(FILE_REGEX, name):
                print(name)
                ext = name.split('.')[1]
                if ext not in filetypes:
                    filetypes.add(ext)
    print("Detected:")
    for filetype in filetypes:
        try:
            print("\t", FILE_TYPES[filetype])
        except BaseException:
            print("\t #Unknown Extension: " + filetype)
    return filetypes


def generate_dockerfile(directory, to_dir="project", add=""):
    """ Creates a Dockerfile based on detected filetypes """
    base_image = "debian:bullseye"
    exts = get_file_types(directory)
    installs = ""
    for ext in exts:
        try:
            installs += FILE_TYPES[ext] + " "
        except BaseException:
            pass
    try:
        docfile = open(
            os.getenv('HOME') + "/" + directory + "/Dockerfile", "w"
        )
    except FileExistsError:
        print("File Already Exists")
        return False
    docfile.write("# BEGIN GENERATED CONTENTS\n")
    docfile.write("FROM " + base_image + "\n\n")
    docfile.write("ADD ./ " + to_dir + "/" + "\n\n")
    docfile.write(
        "RUN apt update && apt upgrade -y && \\\n" +
        "apt install " + installs + "-y" + "\n\n"
    )
    docfile.write("CMD cd ./" + to_dir + " " + add + "\n")
    docfile.write("# END GENERATED CONTENTS\n")
    docfile.close()
    return True
