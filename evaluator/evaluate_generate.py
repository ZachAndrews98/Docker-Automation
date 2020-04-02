""" Evaluate Dockerfile Generator """

from auto import generate
from auto import images


def evaluate_generate():
    """ Evaluate the correctness of Generated Dockerfiles """
    incorrect = 0
    correct = 0
    directories = ("gentest2", "gentest3", "gentest4")
    for file in directories:
        print("Evaluating " + file)
        generate.generate_dockerfile(
            "samples/" + file,
            add="&& chmod +x test.sh && ./test.sh"
        )
        images.build_image("samples/" + file, file, threaded=False)
        if images.run_image(file + ":latest", args="--rm", sep=False) == 1:
            print("\tImage: " + file + " is incorrect")
            incorrect = incorrect + 1
        else:
            print("\tImage: " + file + " is correct")
            correct = correct + 1
        print("\n")
    print("Evaluated " + str(len(directories)) + " Images")
    print("\t" + str(correct) + " Worked Properly")
    print("\t" + str(incorrect) + " Worked Improperly")
