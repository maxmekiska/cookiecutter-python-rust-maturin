import pytest
from {{cookiecutter.package_name}}.utils.fake import show_diff, show_sum


def test_show_sum():
    assert show_sum(1, 2) == "3"


def test_show_diff():
    assert show_diff(2, 1) == "1"
