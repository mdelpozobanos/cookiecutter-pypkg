==================
cookiecutter-pypkg
==================

Cookiecutter template for a Python package. See
https://github.com/audreyr/cookiecutter.

The basic properties of this package are:

+ Free software: MIT license
+ Uses a single definition of the package's **version** within the top
  *__init__.py* file.
+ PyTest_: For code testing.
+ Coverage_: For tracking test coverage.
+ Tox_: To test different environments.
+ Flake8_: To check the coding style.
+ Sphinx_: Ready for Sphinx documentation auto-generator.
+ Travis-CI_: Ready for Travis Continuous Integration testing.
+ ReadTheDocs_: Ready for ReadTheDocs documentation service.
+ Wheel_: Use the newest python package distribution standard from the get go


Usage
-----

Generate a Python package project::

    cookiecutter https://github.com/mdelpozobanos/cookiecutter-pypkg.git

Then:

* Create a repo and put it there.
* Add the repo to your Travis CI account.
* Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service hook.
* Release your package the standard Python way. Here's a release checklist:
  https://gist.github.com/audreyr/5990987


Not Exactly What You Want?
--------------------------

Don't worry, go back to the origin and check other options. This is a fork of
`Audrey's cookiecutter python-package`_. You can also easily create your own
template. Check `Daniel Greenfeld's blog`_ for a nice explanation on how to do this.


.. _Coverage: https://bitbucket.org/ned/coveragepy
.. _Flake8: https://pypi.python.org/pypi/flake8
.. _PyTest: http://pytest.org/latest/
.. _ReadTheDocs: https://readthedocs.org/
.. _Sphinx: http://sphinx-doc.org/
.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Wheel: https://github.com/pypa/pip
.. _`Audrey's cookiecutter python-package`: https://github.com/audreyr/cookiecutter-pypackage
.. _`Daniel Greenfeld's blog`: http://www.pydanny.com/cookie-project-templates-made-easy.html
