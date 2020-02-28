""" Flask routes for homepage and common functions """

import webbrowser

from flask import Flask, render_template, request, redirect, url_for
from flask_fontawesome import FontAwesome

from auto import images, containers
from interface.interface_images import IMAGES_APP
from interface.interface_containers import CONTAINER_APP


APP = Flask(__name__)
APP.register_blueprint(IMAGES_APP)
APP.register_blueprint(CONTAINER_APP)
# pylint: disable=C0103
fa = FontAwesome(APP)


@APP.route('/')
def home():
    """ Homepage of web interface """
    image_list, container_list = get_lists()
    return render_template('gui.html', images=image_list,
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


def start_interface():
    """ Create interface """
    webbrowser.open("http://localhost:5000")
    APP.run()