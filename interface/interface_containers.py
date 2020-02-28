""" Flask routes for containers """

from flask import render_template, request, redirect, url_for, Blueprint

from auto import containers
from interface import interface_main

CONTAINER_APP = Blueprint('containers_app', __name__)


@CONTAINER_APP.route('/containers')
def container():
    """ Page for containers """
    image_list, container_list = interface_main.get_lists()
    return render_template('containers.html', images=image_list,
                           containers=container_list)


@CONTAINER_APP.route('/build_container', methods=['POST'])
def build_container():
    """ Path to call image builder """
    directory = request.form['build_path']
    name = request.form['build_name']
    containers.build_container(directory, name)
    return redirect(url_for("containers_app.container"))


@CONTAINER_APP.route('/run_container', methods=['POST'])
def run_container():
    """ Path to call run container """
    container_name = request.form['run_container_name']
    args = request.form['run_container_args']
    if args != "":
        containers.run_container(container_name, args=args)
    else:
        containers.run_container(container_name)
    return redirect(url_for("containers_app.container"))


@CONTAINER_APP.route('/delete_container', methods=['POST'])
def delete_container():
    """ Path to delete container """
    container_name = request.form['delete_container_name']
    containers.delete_container(container_name.strip().split(','))
    return redirect(url_for("containers_app.container"))
