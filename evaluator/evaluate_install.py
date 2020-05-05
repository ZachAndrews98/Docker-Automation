""" Evaluate Docker Installation """

import os

from auto import images, containers


def evaluate_ubuntu():
    """ Evaluates installation process on Ubuntu """
    images.delete_image("ubuntest:latest".split(','))
    containers.delete_container("ubuntest".split(','))
    images.build_image(
        "/Docker-Automation/evaluator/Dockerfiles/Ubuntest",
        image_name="ubuntest",
        threaded=False
    )
    return images.run_image(
        "ubuntest:latest",
        args="-v /var/run/docker.sock:/var/run/docker.sock -it --name ubuntest",
        sep=False
    )


def evaluate_fedora():
    """ Evaluates installation process on Fedora """
    images.delete_image("fedortest:latest".split(','))
    containers.delete_container("fedortest".split(','))
    images.build_image(
        "/Docker-Automation/evaluator/Dockerfiles/Fedortest",
        image_name="fedortest",
        threaded=False
    )
    return images.run_image(
        "fedortest:latest",
        args="-v /var/run/docker.sock:/var/run/docker.sock -it --name fedortest",
        sep=False
    )


def evaluate_debian():
    """ Evaluates installation process on Debian """
    images.delete_image("debtest:latest".split(','))
    containers.delete_container("debtest".split(','))
    images.build_image(
        "/Docker-Automation/evaluator/Dockerfiles/Debtest",
        image_name="debtest",
        threaded=False
    )
    return images.run_image(
        "debtest:latest",
        args="-v /var/run/docker.sock:/var/run/docker.sock -it --name debtest",
        sep=False
    )


def evaluate_install():
    ubuntu = evaluate_ubuntu()
    print(ubuntu)
    # fedora = evaluate_fedora() == None
    # debian = evaluate_debian() == None

    print("Evaluating Installation Process")
    print("\tUbuntu: " + str(ubuntu))
    print("\tFedora: " + str(fedora))
    print("\tDebian: " + str(debian))
