""" Run Docker Automation and Setup Program """

import sys
import webbrowser

from flask import Flask, render_template, request, redirect, url_for
from flask_fontawesome import FontAwesome

from auto import docker_auto, generate, install, images, containers


APP = Flask(__name__)
# pylint: disable=C0103
fa = FontAwesome(APP)


@APP.route('/')
def home():
    """ Homepage of web interface """
    image_list, container_list = get_lists()
    return render_template('gui.html', images=image_list,
                           containers=container_list)


@APP.route('/images')
def image():
    """ Page for images """
    image_list, container_list = get_lists()
    return render_template('images.html', images=image_list,
                           containers=container_list)


@APP.route('/containers')
def container():
    """ Page for containers """
    image_list, container_list = get_lists()
    return render_template('containers.html', images=image_list,
                           containers=container_list)


def get_lists():
    """ Get the list of images and containers """
    image_list = images.list_images()
    if image_list is None:
        image_list = ["None"]
    container_list = containers.list_containers()
    if container_list is None:
        container_list = ["None"]
    return image_list, container_list


@APP.route('/update')
def update():
    """ Update the interface """
    return redirect(url_for("home"))


@APP.route('/generate_doc', methods=['POST'])
def generate_doc():
    """ Path to call dockerfile generator """
    directory = request.form['generate_dir']
    to_dir = request.form['generate_to_dir']
    if to_dir != "":
        generate.generate_dockerfile(directory, to_dir=to_dir)
    else:
        generate.generate_dockerfile(directory)
    return redirect(url_for("image"))


@APP.route('/build_image', methods=['POST'])
def build_image():
    """ Path to call image builder """
    directory = request.form['build_path']
    name = request.form['build_name']
    images.build_image(directory, name)
    return redirect(url_for("image"))


@APP.route('/build_container', methods=['POST'])
def build_container():
    """ Path to call image builder """
    directory = request.form['build_path']
    name = request.form['build_name']
    images.build_image(directory, name)
    return redirect(url_for("container"))


@APP.route('/run_image', methods=['POST'])
def run_image():
    """ Path to call run image """
    image_name = request.form['run_image_name']
    args = request.form['run_image_args']
    if args != "":
        images.run_image(image_name, args=args)
    else:
        images.run_image(image_name)
    return redirect(url_for("image"))


@APP.route('/run_container', methods=['POST'])
def run_container():
    """ Path to call run container """
    container_name = request.form['run_container_name']
    args = request.form['run_container_args']
    if args != "":
        containers.run_container(container_name, args=args)
    else:
        containers.run_container(container_name)
    return redirect(url_for("container"))


@APP.route('/delete_image', methods=['POST'])
def delete_image():
    """ Path to delete image """
    image_name = request.form['delete_image_name']
    images.delete_image(image_name.strip().split(','))
    return redirect(url_for("image"))


@APP.route('/delete_container', methods=['POST'])
def delete_container():
    """ Path to delete container """
    container_name = request.form['delete_container_name']
    containers.delete_container(container_name.strip().split(','))
    return redirect(url_for("container"))


# pylint: disable=W0622
def exit():
    """ Shutdown interface """
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@APP.route('/shutdown')
def shutdown():
    """ Path to shutdown interface """
    # pylint: disable=R1722
    exit()
    return render_template("exit.html")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--terminal":
        print(install.install())
        docker_auto.repl()
    else:
        print(install.install())
        webbrowser.open("http://localhost:5000")
        APP.run()
