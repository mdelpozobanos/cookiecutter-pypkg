#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_{{ cookiecutter.repo_name }}
----------------------------------

Tests for `{{ cookiecutter.repo_name }}` module.
"""

import pytest
from {{ cookiecutter.repo_name }} import {{ cookiecutter.repo_name }}


def test_foo():
    """String describing the test"""
    assert({{ cookiecutter.repo_name }}.foo(1, 2) == 2)


# The following is an attribute definition
@pytest.fixture(scope='class')
def foo_obj():
    return {{ cookiecutter.repo_name }}.Foo({{ cookiecutter.repo_name }}.foo)


class TestFoo():
    """Class to test the {{ cookiecutter.repo_name }}.Foo class"""

    def test_main(self):
        """Allocation"""
        {{ cookiecutter.repo_name }}.Foo({{ cookiecutter.repo_name }}.foo)

    def test_foo(self, foo_obj):
        """Method foo"""
        assert(foo_obj.foo(2, 2) == 4)

    def test_foo_args(self, foo_obj):
        """Bad arg detection"""
        with pytest.raises(TypeError):
            foo_obj.foo(2, 'a')
