""" Test Dockerfile Generation methods """
import pytest

from auto import docfile_gen
from os import path


location = [
    ('./gentest', {'py', 'c', 'java', 'js', 'sh', 'rb', 'go'})
]
@pytest.mark.parametrize("location, expected", location)
def test_get_file_types(location, expected):
    """ Checks that correct file types are found """
    assert docfile_gen.get_file_types(location) == expected


location = [
    ('./gentest', './gentest/Dockerfile', True),
    ('./gentest', './instructions/Dockerfile', False)
]
@pytest.mark.parametrize("location, path_check, expected", location)
def test_generate_dockerfile(location, path_check, expected):
    """ Checks if the proper Dockerfile is created """
    docfile_gen.generate_dockerfile(location)
    assert path.exists(path_check) == expected


# NOTE: Test disabled until can figure out how to check for successful run of image in separate terminal
# image = [
#     ("hello-world:latest", True),
#     ("hello-word:latest", False)
# ]
# @pytest.mark.parametrize("image, expected", image)
# def test_run_image(image, expected):
#     """ Checks if a separate terminal and Docker image can be run """
#     assert docfile_gen.run_image(image) == expected


# def test_build_image():
#     """ Checks if building an image works properly """
#     assert docfile_gen.build_image("./instructions", "") == 1
#     assert docfile_gen.build_image("./gentest", "test") == True
