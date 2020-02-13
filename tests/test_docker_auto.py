""" Test Docker Automation methods """
import pytest

import io

from auto import docker_auto


# data = [
#     ("exit", 0)
# ]
# @pytest.mark.parametrize("input, expected", data)
# def test_main(input, expected, monkeypatch):
#     """ Test main function """
#     monkeypatch.setattr('sys.stdin', io.StringIO(input))
#     assert docker_auto.main() == expected


data = [
    ("exit", 0)
]
@pytest.mark.parametrize("input, expected", data)
def test_repl(input, expected, monkeypatch):
    """ Test Repl function """
    monkeypatch.setattr('sys.stdin', io.StringIO(input))
    assert docker_auto.repl() == expected


location = [
    ("../gentest", "../gentest")
]
@pytest.mark.parametrize("input, expected", location)
def test_get_directory(input, expected, monkeypatch):
    """ Test get directory function """
    monkeypatch.setattr('sys.stdin', io.StringIO(input))
    assert docker_auto.get_directory() == expected
