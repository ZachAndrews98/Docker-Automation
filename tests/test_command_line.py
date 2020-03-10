""" Tests for command line arguments """

import pytest

from auto import command_line, arguments


DATA = [
    (["--build"], "Additional flags required"),
    (["--build", "--image"], "Additional flags required"),
    (["--build", "--image", "--path", "path"], "Additional flags required"),
    (["--build", "--image", "--name", "name"], "Additional flags required"),
    (["--build", "--container"], "Additional flags required"),
    (
        ["--build", "--container", "--name", "name"],
        "Additional flags required"
    ),
    (
        ["--build", "--container", "--args", "args"],
        "Additional flags required"
    ),
]
@pytest.mark.parametrize("args, expected", DATA)
def test_build_not_enough_flags(args, expected):
    """ Test build with not enough flags """
    parsed_args = arguments.parse_args(args)
    assert command_line.command_line(parsed_args) == expected


DATA = [
    (["--run"], "Additional flags required"),
    (["--run", "--image"], "Additional flags required"),
    (["--run", "--image", "--args", "args"], "Additional flags required"),
    (["--run", "--container"], "Additional flags required"),
    (["--run", "--container", "--args", "args"], "Additional flags required"),
]
@pytest.mark.parametrize("args, expected", DATA)
def test_run_not_enough_flags(args, expected):
    """ Test build with not enough flags """
    parsed_args = arguments.parse_args(args)
    assert command_line.command_line(parsed_args) == expected


DATA = [
    (["--generate"], "Additional flags required"),
    (["--generate", "--image", "--path", "path"], "Additional flags required"),
    (["--generate", "--image", "--name", "name"], "Additional flags required"),
]
@pytest.mark.parametrize("args, expected", DATA)
def test_generate_not_enough_flags(args, expected):
    """ Test build with not enough flags """
    parsed_args = arguments.parse_args(args)
    assert command_line.command_line(parsed_args) == expected


DATA = [
    (["--delete"], "Additional flags required"),
    (["--delete", "--image"], "Additional flags required"),
    (["--delete", "--container"], "Additional flags required"),
]
@pytest.mark.parametrize("args, expected", DATA)
def test_delete_not_enough_flags(args, expected):
    """ Test build with not enough flags """
    parsed_args = arguments.parse_args(args)
    assert command_line.command_line(parsed_args) == expected


DATA = [
    (["--pull"], "Additional flags required"),
    (["--pull", "--name", "name"], "Additional flags required"),
    (["--pull", "--tag", "tag"], "Additional flags required"),
]
@pytest.mark.parametrize("args, expected", DATA)
def test_pull_not_enough_flags(args, expected):
    """ Test build with not enough flags """
    parsed_args = arguments.parse_args(args)
    assert command_line.command_line(parsed_args) == expected


DATA = [
    (["--push"], "Additional flags required"),
    (["--push", "--name", "name"], "Additional flags required"),
    (["--push", "--tag", "tag"], "Additional flags required"),
]
@pytest.mark.parametrize("args, expected", DATA)
def test_push_not_enough_flags(args, expected):
    """ Test build with not enough flags """
    parsed_args = arguments.parse_args(args)
    assert command_line.command_line(parsed_args) == expected


DATA = [
    (["--list"], "Additional flags required"),
]
@pytest.mark.parametrize("args, expected", DATA)
def test_list_not_enough_flags(args, expected):
    """ Test build with not enough flags """
    parsed_args = arguments.parse_args(args)
    assert command_line.command_line(parsed_args) == expected


DATA = [
    (["--login"], "Additional flags required"),
]
@pytest.mark.parametrize("args, expected", DATA)
def test_login_not_enough_flags(args, expected):
    """ Test build with not enough flags """
    parsed_args = arguments.parse_args(args)
    assert command_line.command_line(parsed_args) == expected


DATA = [
    (["--kill"], "Additional flags required"),
]
@pytest.mark.parametrize("args, expected", DATA)
def test_kill_not_enough_flags(args, expected):
    """ Test build with not enough flags """
    parsed_args = arguments.parse_args(args)
    assert command_line.command_line(parsed_args) == expected


DATA = [
    (["--stop"], "Additional flags required"),
]
@pytest.mark.parametrize("args, expected", DATA)
def test_stop_not_enough_flags(args, expected):
    """ Test build with not enough flags """
    parsed_args = arguments.parse_args(args)
    assert command_line.command_line(parsed_args) == expected


DATA = [
    (["--restart"], "Additional flags required"),
]
@pytest.mark.parametrize("args, expected", DATA)
def test_restart_not_enough_flags(args, expected):
    """ Test build with not enough flags """
    parsed_args = arguments.parse_args(args)
    assert command_line.command_line(parsed_args) == expected
