""" Test Image Utilities """

import pytest

from auto import images
import docker


data = [
    ("hello-world", "latest", docker.models.images.Image)
]
@pytest.mark.parametrize("image_name, tag, expected", data)
def test_pull_image(image_name, tag, expected):
    """ Checks if image pull works properly """
    assert isinstance(images.pull_image(image_name, tag=tag), expected)


data = [
    (["hello-world:latest"])
]
@pytest.mark.parametrize("expected", data)
def test_list_images(expected):
    """ Checks if listed images works properly """
    assert images.list_images() == expected


data = [
    ("./instructions", "test", False),
    ("./gentest", "test", True)
]
@pytest.mark.parametrize("path, name, expected", data)
def test_build_image(path, name, expected):
    """ Checks if building an image works properly """
    assert images.build_image(path, name) == expected


# NOTE: Test disabled until can figure out how to check for successful run of image in separate terminal
# image = [
#     ("hello-world:latest", True),
#     ("hello-word:latest", False)
# ]
# @pytest.mark.parametrize("image, expected", image)
# def test_run_image(image, expected):
#     """ Checks if a separate terminal and Docker image can be run """
#     assert docfile_gen.run_image(image) == expected
