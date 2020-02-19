""" Test Dockerfile Generation methods """

import pytest

from auto import generate
from os import path


location = [
    ('./gentest', {'py', 'c', 'java', 'js', 'sh', 'rb', 'go'})
]
@pytest.mark.parametrize("location, expected", location)
def test_get_file_types(location, expected):
    """ Checks that correct file types are found """
    assert generate.get_file_types(location) == expected


location = [
    ('./gentest', './gentest/Dockerfile', True),
    ('./gentest', './instructions/Dockerfile', False)
]
@pytest.mark.parametrize("location, path_check, expected", location)
def test_generate_dockerfile(location, path_check, expected):
    """ Checks if the proper Dockerfile is created """
    generate.generate_dockerfile(location)
    assert path.exists(path_check) == expected
