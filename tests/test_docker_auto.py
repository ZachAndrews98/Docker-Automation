import pytest

import io

from auto import docker_auto


def test_main(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('exit'))
    assert docker_auto.main() == 0


def test_repl(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('exit'))
    assert docker_auto.repl() == 0

def test_get_directory(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('../gentest'))
    assert docker_auto.get_directory() == "../gentest"
