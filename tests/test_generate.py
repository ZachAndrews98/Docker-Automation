""" Test Dockerfile Generation methods """

import os

import pytest

from auto import generate


LOCATION = [
    (
        'Docker-Automation/samples/gentest',
        {'py', 'c', 'java', 'js', 'sh', 'rb', 'go'}
    )
]
@pytest.mark.parametrize("location, expected", LOCATION)
def test_get_file_types(location, expected):
    """ Checks that correct file types are found """
    assert generate.get_file_types(location) == expected


LOCATION = [
    (
        'Docker-Automation/samples/gentest',
        'Docker-Automation/samples/gentest/Dockerfile',
        True
    ),
    (
        'Docker-Automation/samples/gentest',
        'Docker-Automation/instructions/Dockerfile',
        False
    )
]
@pytest.mark.parametrize("location, path_check, expected", LOCATION)
def test_generate_dockerfile(location, path_check, expected):
    """ Checks if the proper Dockerfile is created """
    generate.generate_dockerfile(location)
    assert os.path.exists(os.getenv('HOME') + "/" + path_check) == expected
