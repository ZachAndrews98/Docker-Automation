""" Test Docker utilities functions """

from auto import containers

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


# data = [
#     (["hello"])
# ]
# @pytest.mark.parametrize("expected", data)
# def test_list_containers(expected):
#     """ Checks if listed containers works properly """
#     assert utilities.list_containers() == expected
