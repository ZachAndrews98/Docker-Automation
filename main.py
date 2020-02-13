""" Run Docker Automation and Setup Program """
import sys

from flask import Flask, render_template, request, redirect, url_for

from auto import docker_auto, generate, install, utilities


APP = Flask(__name__)


@APP.route('/')
def home():
    """ Homepage of web interface """
    image_list = utilities.list_images()
    if image_list is not None:
        image_list = ', '.join(image_list)
    container_list = utilities.list_containers()
    if container_list is not None:
        container_list = ', '.join(container_list)
    return render_template('gui.html', images=image_list,
                           containers=container_list)


@APP.route('/update', methods=['POST'])
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
    return redirect(url_for("home"))


@APP.route('/build', methods=['POST'])
def build():
    """ Path to call image builder """
    directory = request.form['build_path']
    name = request.form['build_name']
    utilities.build_image(directory, name)
    return redirect(url_for("home"))


@APP.route('/run_image', methods=['POST'])
def run_image():
    """ Path to call run image """
    image_name = request.form['run_image_name']
    args = request.form['run_image_args']
    if args != "":
        utilities.run_image(image_name, args=args)
    else:
        utilities.run_image(image_name)
    return redirect(url_for("home"))


@APP.route('/run_container', methods=['POST'])
def run_container():
    """ Path to call run container """
    container_name = request.form['run_container_name']
    args = request.form['run_container_args']
    if args != "":
        utilities.run_container(container_name, args=args)
    else:
        utilities.run_container(container_name)
    return redirect(url_for("home"))


@APP.route('/delete_image', methods=['POST'])
def delete_image():
    """ Path to delete image """
    image_name = request.form['delete_image_name']
    utilities.delete_image(image_name.strip().split(','))
    return redirect(url_for("home"))


@APP.route('/delete_container', methods=['POST'])
def delete_container():
    """ Path to delete container """
    container_name = request.form['delete_container_name']
    utilities.delete_container(container_name.strip().split(','))
    return redirect(url_for("home"))


# pylint: disable=W0622
def exit():
    """ Shutdown interface """
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@APP.route('/shutdown', methods=['POST'])
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
        install.install()
        APP.run()
