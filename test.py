import os
import sys
import re

FILE_REGEX = '^[a-zA-Z0-9_]+\.[a-zA-Z0-9]+$'

file_types = {
    "py": "python3",
    "java": "default-jdk",
    "js": "node",
    "c": "gcc",
    "cs": "gcc",
    "cpp": "gcc",
    'rb': "ruby",
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
    docfile.write("FROM " + BASE_IMAGE + "\n")
    docfile.write("ADD ./ test/" + "\n")
    docfile.write("RUN apt-get update && apt-get upgrade -y && \\\n    apt-get install " + INSTALLS + "-y" + "\n")
    docfile.close()


directory = str(input("Enter directory\n"))
# get_file_types(directory)
generate_dockerfile(directory)
