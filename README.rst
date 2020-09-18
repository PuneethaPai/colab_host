=========
ColabHost
=========


.. image:: https://img.shields.io/github/workflow/status/PuneethaPai/colab_host/CI%20Build.svg
        :target: https://github.com/PuneethaPai/colab_host/actions

.. image:: https://img.shields.io/pypi/v/colab_host.svg
        :target: https://pypi.python.org/pypi/colab_host

.. image:: https://readthedocs.org/projects/colab-host/badge/?version=latest
        :target: https://colab-host.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black



Host any (python) application in colab or kaggle notebook environment
---------------------------------------------------------------------

Google Colab and Kaggle notebook environments are great. You have powerful compute, but just using their notebook environment feels restrictive.
Given the hardware you should be able to do more.


Inspired from `Abhishek Thakur <https://github.com/abhishekkrthakur/>`_, and his work on `colab code <https://github.com/abhishekkrthakur/colabcode>`_ this package extends the idea.

=========
Features:
=========

Supported IDEs:
~~~~~~~~~~~~~~

* Jupyter Notebook 
* Jupyter Lab 
* For VScode you can use `colabcode <https://github.com/abhishekkrthakur/colabcode>`_

Supported Applications:
~~~~~~~~~~~~~~~~~~~~~~

* Flask and Gunicron applications 
* FastAPI and Uvicorn applications

*This is purely for developement and testing purpose. You can use supported IDEs to seamlessly develop your idea and also host them for testing purpose.*
*It is not advised to use for production purpose.*

=============
Installation:
=============
.. code-block:: console

    $ pip install colab_host


.. include:: usage.rst

* Free software: MIT license
* Documentation: https://colab-host.readthedocs.io.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
