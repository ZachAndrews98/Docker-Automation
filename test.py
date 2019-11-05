import os
import sys
import re

FILE_REGEX = '^[a-zA-Z0-9]+\.[a-zA-Z0-9]+$'

file_types = {
    "py": "Python",
    "java": "Java",
    "js": "JavaSript",
    "c": "C",
    "cs": "C#",
    "cpp": "C++",
    "md": "MarkDown",
    "css": "CSS",
    "html": "HTML",
    "txt": "Text File"
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

def generate_dockerfile(directory):
    try:
        docfile = open("./" + directory + "/Dockerfile", "w+")
    except FileExistsError:
        print("File Already Exists")
        sys.quit()
    docfile.close()


directory = str(input("Enter directory\n"))
get_file_types(directory)
# generate_dockerfile(directory)
