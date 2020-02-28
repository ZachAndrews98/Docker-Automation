""" Test Dockerfile Generation methods """

from os import path

import pytest

from auto import generate


LOCATION = [
    ('./gentest', {'py', 'c', 'java', 'js', 'sh', 'rb', 'go'})
]
@pytest.mark.parametrize("location, expected", LOCAITON)
def test_get_file_types(location, expected):
    """ Checks that correct file types are found """
    assert generate.get_file_types(location) == expected


LOCAITON = [
    ('./gentest', './gentest/Dockerfile', True),
    ('./gentest', './instructions/Dockerfile', False)
]
@pytest.mark.parametrize("location, path_check, expected", LOCAITON)
def test_generate_dockerfile(location, path_check, expected):
    """ Checks if the proper Dockerfile is created """
    generate.generate_dockerfile(location)
    assert path.exists(path_check) == expected
