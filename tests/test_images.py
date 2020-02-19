import pytest

from auto import images

data = [
    ("./instructions", "test", False),
    ("./gentest", "test", True)
]
@pytest.mark.parametrize("path, name, expected", data)
def test_build_image(path, name, expected):
    """ Checks if building an image works properly """
    assert images.build_image(path, name) == expected


data = [
    (["test:latest", "debian:bullseye", "hello-world:latest"])
]
@pytest.mark.parametrize("expected", data)
def test_list_images(expected):
    """ Checks if listed images works properly """
    assert images.list_images() == expected
