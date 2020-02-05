""" Test Dockerfile Generation methods """
import pytest

from auto import docfile_gen


def test_get_file_types():
    """ Checks that correct file types are found """
    assert docfile_gen.get_file_types('./gentest') == {'py', 'c', 'java', 'js', 'sh', 'rb', 'go'}
