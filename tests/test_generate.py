""" Test Dockerfile Generation methods """

from os import path

import pytest

from auto import generate


LOCATION = [
    ('./samples/gentest', {'py', 'c', 'java', 'js', 'sh', 'rb', 'go'})
]
@pytest.mark.parametrize("location, expected", LOCATION)
def test_get_file_types(location, expected):
    """ Checks that correct file types are found """
    assert generate.get_file_types(location) == expected


LOCATION = [
    ('./samples/gentest', './samples/gentest/Dockerfile', True),
    ('./samples/gentest', './instructions/Dockerfile', False)
]
@pytest.mark.parametrize("location, path_check, expected", LOCATION)
def test_generate_dockerfile(location, path_check, expected):
    """ Checks if the proper Dockerfile is created """
    generate.generate_dockerfile(location)
    assert path.exists(path_check) == expected
