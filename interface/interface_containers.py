""" Flask routes for containers """

from flask import render_template, request, redirect, url_for, Blueprint

from auto import containers
from interface import interface_main

CONTAINERS_APP = Blueprint('containers_app', __name__)


@CONTAINERS_APP.route('/containers')
def container():
    """ Page for containers """
    image_list, container_list = interface_main.get_lists()
    return render_template('containers.html', images=image_list,
                           containers=container_list)


@CONTAINERS_APP.route('/containers/build', methods=['POST'])
def build_container():
    """ Path to call image builder """
    image_name = request.form['build_image_name']
    args = request.form['build_container_args']
    containers.build_container(image_name, args)
    return redirect(url_for("containers_app.container"))


@CONTAINERS_APP.route('/containers/run', methods=['POST'])
def run_container():
    """ Path to call run container """
    container_name = request.form['run_container_name']
    args = request.form['run_container_args']
    if args != "":
        containers.run_container(container_name, args=args)
    else:
        containers.run_container(container_name)
    return redirect(url_for("containers_app.container"))


@CONTAINERS_APP.route('/containers/kill', methods=['POST'])
def kill_container():
    """ Kill a running container """
    container_name = request.form['kill_container_name']
    containers.kill_container(container_name)
    return redirect(url_for("containers_app.container"))


@CONTAINERS_APP.route('/containers/stop', methods=['POST'])
def stop_container():
    """ Stop a running container """
    container_name = request.form['stop_container_name']
    containers.stop_container(container_name)
    return redirect(url_for("containers_app.container"))


@CONTAINERS_APP.route('/containers/restart', methods=['POST'])
def restart_container():
    """ Restart a stopped container """
    container_name = request.form['restart_container_name']
    containers.restart_container(container_name)
    return redirect(url_for("containers_app.container"))


@CONTAINERS_APP.route('/containers/delete', methods=['POST'])
def delete_container():
    """ Path to delete container """
    container_name = request.form['delete_container_name']
    containers.delete_container(container_name.strip().split(','))
    return redirect(url_for("containers_app.container"))
