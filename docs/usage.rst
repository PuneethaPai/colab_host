=====
Usage
=====

To use Host a simple in a project::

    from colab_host import Host
    
    Host(port=1000)

To start Jupyter Notebook in colab::

    from colab_host import JupyterNotebook

    JupyterNotebook(port=1000)

To start Jupyter Lab in colab::

    from colab_host import JupyterLab

    JupyterLab(port=1000)

To start Flas Application in colab::

    from colab_host import FlaskApp

    FlaskApp(
        port=1000,
        app="main:app",
        git_url="https://github.com/PuneethaPai/colab_host_flask_demo.git",
        requirements_file="requirements.txt"
    )

To start Uvicorn App in colab::

    from colab_host import UvicornApp

    UvicornApp(
        port=1000,
        app="main:app",
        git_url="https://github.com/PuneethaPai/colab_host_uvicorn_demo.git",
        requirements_file="requirements.txt"
    )
