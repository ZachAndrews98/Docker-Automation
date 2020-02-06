""" Test Docker installation methods """
import pytest

import io

from auto import install_docker


# def test_install(monkeypatch):
#     """ Test Install Method """
#     monkeypatch.setattr('PLATFORM', io.StringIO('Linux'))
#     monkeypatch.setattr('distro', io.StringIO(("Ubuntu", "", "")))
#     assert install_docker.install() == "Docker successfully installed"

def test_get_instructions():
    """ Test Correct Instruction Set Found """
    assert install_docker.get_instructions(("Ubuntu", "", "")) == "./instructions/ubuntu"
    assert install_docker.get_instructions(("CentOS", "", "")) == "./instructions/centos"
    assert install_docker.get_instructions(("Debian", "", "")) == "./instructions/debian"
    assert install_docker.get_instructions(("Fedora", "", "")) == "./instructions/fedora"
    assert install_docker.get_instructions(("MacOS", "", "")) == "./instructions/macos"
    assert install_docker.get_instructions(("","","")) == "No Instruction Set"


def test_confirm_installation():
    """ Test Installation Confirmation """
    assert install_docker.confirm_installation() == True
