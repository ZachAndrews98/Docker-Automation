""" Test Docker installation methods """

import pytest

from auto import install


def test_install():
    """ Test Install Method """
    assert install.install() == "Docker already installed."


DISTROS = [
    (("Ubuntu", "", ""), "./instructions/ubuntu"),
    (("CentOS", "", ""), "./instructions/centos"),
    (("Debian", "", ""), "./instructions/debian"),
    (("Fedora", "", ""), "./instructions/fedora"),
    (("MacOS", "", ""), "./instructions/macos"),
    (("", "", ""), "No Instruction Set")
]
@pytest.mark.parametrize("distro, expected", DISTROS)
def test_get_instructions(distro, expected):
    """ Test Correct Instruction Set Found """
    assert install.get_instructions(distro) == expected


def test_confirm_installation():
    """ Test Installation Confirmation """
    assert install.confirm_installation() is True
