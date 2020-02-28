""" Flask routes for images """

from flask import render_template, request, redirect, url_for, Blueprint

from auto import generate, images
from interface import interface_main

IMAGES_APP = Blueprint('images_app', __name__)


@IMAGES_APP.route('/images')
def image():
    """ Page for images """
    image_list, container_list = interface_main.get_lists()
    return render_template('images.html', images=image_list,
                           containers=container_list)


@IMAGES_APP.route('/generate_doc', methods=['POST'])
def generate_doc():
    """ Path to call dockerfile generator """
    directory = request.form['generate_dir']
    to_dir = request.form['generate_to_dir']
    if to_dir != "":
        generate.generate_dockerfile(directory, to_dir=to_dir)
    else:
        generate.generate_dockerfile(directory)
    return redirect(url_for("images_app.image"))


@IMAGES_APP.route('/images/build', methods=['POST'])
def build_image():
    """ Path to call image builder """
    directory = request.form['build_path']
    name = request.form['build_name']
    images.build_image(directory, name)
    return redirect(url_for("images_app.image"))


@IMAGES_APP.route('/images/pull', methods=['POST'])
def pull_image():
    """ Pull an image from an external source """
    image_name = request.form['pull_image_name']
    image_tag = request.form['pull_image_tag']
    images.pull_image(image_name, tag=image_tag)
    return redirect(url_for("images_app.image"))


@IMAGES_APP.route('/images/push', methods=['POST'])
def push_image():
    """ Push an image to an external repository """
    image_name = request.form['push_image_name']
    image_tag = request.form['push_image_tag']
    images.push_image(image_name, tag=image_tag)
    return redirect(url_for("images_app.image"))


@IMAGES_APP.route('/images/run', methods=['POST'])
def run_image():
    """ Path to call run image """
    image_name = request.form['run_image_name']
    args = request.form['run_image_args']
    if args != "":
        images.run_image(image_name, args=args)
    else:
        images.run_image(image_name)
    return redirect(url_for("images_app.image"))


@IMAGES_APP.route('/images/delete', methods=['POST'])
def delete_image():
    """ Path to delete image """
    image_name = request.form['delete_image_name']
    images.delete_image(image_name.strip().split(','))
    return redirect(url_for("images_app.image"))
