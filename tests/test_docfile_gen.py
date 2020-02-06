""" Test Dockerfile Generation methods """
import pytest

from auto import docfile_gen
from os import path


def test_get_file_types():
    """ Checks that correct file types are found """
    assert docfile_gen.get_file_types('./gentest') == {'py', 'c', 'java', 'js', 'sh', 'rb', 'go'}


def test_generate_dockerfile():
    """ Checks if the proper Dockerfile is created """
    docfile_gen.generate_dockerfile('./gentest')
    assert path.exists("./gentest/Dockerfile") == True


def test_run_image():
    """ Checks if a separate terminal and Docker image can be run """
    assert docfile_gen.run_image("hello-world:latest") == True


def test_build_image():
    """ Checks if building an image works properly """
    assert docfile_gen.build_image("./instructions", "") == 1
    assert docfile_gen.build_image("./gentest", "test") == 0
