""" Test Docker Automation methods """

import io

import pytest

from auto import docker_auto


# data = [
#     ("exit", 0)
# ]
# @pytest.mark.parametrize("input, expected", data)
# def test_main(input, expected, monkeypatch):
#     """ Test main function """
#     monkeypatch.setattr('sys.stdin', io.StringIO(input))
#     assert docker_auto.main() == expected


DATA = [
    ("exit", 0)
]
@pytest.mark.parametrize("sim_input, expected", DATA)
def test_repl(sim_input, expected, monkeypatch):
    """ Test Repl function """
    monkeypatch.setattr('sys.stdin', io.StringIO(sim_input))
    assert docker_auto.repl() == expected


LOCATION = [
    ("../gentest", "../gentest")
]
@pytest.mark.parametrize("sim_input, expected", LOCATION)
def test_get_directory(sim_input, expected, monkeypatch):
    """ Test get directory function """
    monkeypatch.setattr('sys.stdin', io.StringIO(sim_input))
    assert docker_auto.get_directory() == expected
