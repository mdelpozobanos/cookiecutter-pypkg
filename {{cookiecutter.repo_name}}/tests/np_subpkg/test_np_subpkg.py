#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_{{ cookiecutter.repo_name }}
----------------------------------

Tests for `{{ cookiecutter.repo_name }}.np_subpkg` module.
"""

import pytest
from {{ cookiecutter.repo_name }} import np_subpkg


# The following is an attribute definition
@pytest.fixture(scope='class')
def foo_obj():
    return np_subpkg.NPClass()


class TestNPClass():
    """Class to test the {{ cookiecutter.repo_name }}.np_subpkg.GClass class"""

    def test_main(self):
        """Allocation"""
        obj = np_subpkg.NPClass('this')
        assert(isinstance(obj, np_subpkg.NPClass))

    def test_foo(self, foo_obj):
        """Method foo"""
        assert(foo_obj.foo(2, 2) == 0)

    def test_foo_args(self, foo_obj):
        """Bad arg detection"""
        with pytest.raises(TypeError):
            foo_obj.foo(2, 'a')


# Test the main file
from {{ cookiecutter.repo_name }}.np_subpkg import main


def test_main_foo():
    """String describing the test"""
    assert(main.np_function(1, 2) == -1)