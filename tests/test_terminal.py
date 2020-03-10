""" Test Docker Automation methods """

import io

import pytest

from auto import terminal


DATA = [
    ("exit", 0)
]
@pytest.mark.parametrize("sim_input, expected", DATA)
def test_repl(sim_input, expected, monkeypatch):
    """ Test Repl function """
    monkeypatch.setattr('sys.stdin', io.StringIO(sim_input))
    assert terminal.repl() == expected
