""" Test Docker utilities functions """

from auto import utilities

import pytest



# NOTE: Test disabled until can figure out how to check for successful run of image in separate terminal
# image = [
#     ("hello-world:latest", True),
#     ("hello-word:latest", False)
# ]
# @pytest.mark.parametrize("image, expected", image)
# def test_run_image(image, expected):
#     """ Checks if a separate terminal and Docker image can be run """
#     assert docfile_gen.run_image(image) == expected

data = [
    ("./instructions", "test", False),
    ("./gentest", "test", True)
]
@pytest.mark.parametrize("path, name, expected", data)
def test_build_image(path, name, expected):
    """ Checks if building an image works properly """
    assert utilities.build_image(path, name) == expected


data = [
    (["test:latest", "debian:bullseye", "hello-world:latest"])
]
@pytest.mark.parametrize("expected", data)
def test_list_images(expected):
    """ Checks if listed images works properly """
    assert utilities.list_images() == expected


# data = [
#     (["hello"])
# ]
# @pytest.mark.parametrize("expected", data)
# def test_list_containers(expected):
#     """ Checks if listed containers works properly """
#     assert utilities.list_containers() == expected
