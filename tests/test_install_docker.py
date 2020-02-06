""" Test Docker installation methods """
import pytest

import io

from auto import install_docker


def test_install():
    """ Test Install Method """
    assert install_docker.install() == "Docker already installed"


distros = [
    (("Ubuntu", "", ""), "./instructions/ubuntu"),
    (("CentOS", "", ""), "./instructions/centos"),
    (("Debian", "", ""), "./instructions/debian"),
    (("Fedora", "", ""), "./instructions/fedora"),
    (("MacOS", "", ""), "./instructions/macos"),
    (("", "", ""), "No Instruction Set")
]
@pytest.mark.parametrize("distro, expected",distros)
def test_get_instructions(distro, expected):
    """ Test Correct Instruction Set Found """
    assert install_docker.get_instructions(distro) == expected


def test_confirm_installation():
    """ Test Installation Confirmation """
    assert install_docker.confirm_installation() == True
