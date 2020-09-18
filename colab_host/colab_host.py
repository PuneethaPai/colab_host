import subprocess
from pyngrok import ngrok
from git import Repo
import re
import os
import shutil
from pathlib import Path


class Host:
    """Base class for hosting any python application.

    Given `port` number it will expose the port to internet.
    Given `requirements` will install them using `pip install`.
    Given `git_url` it will clone the repo for you.

    Parameters:

        port : int, optional

        requirements : List[str] or str, optional
            List[str]: list of package requirements for hosting.
            str: requirements file path to install requirements from.
        git_url : str, optional

    """

    def __init__(
        self, port: int = 1000, requirements: list or str = None, git_url: str = None
    ):
        super().__init__()
        if isinstance(git_url, str):
            self._clone_repo(git_url)
        self._install_requirements(requirements)
        self.port = port
        self._start_tunnel()

    def _clone_repo(self, git_url) -> Repo:
        folder_name = re.search(r"[^/]+$", git_url).group().replace(".git", "")
        folder = Path(folder_name)
        if folder.exists() and folder.is_dir():
            shutil.rmtree(folder)
        repo = Repo.clone_from(git_url, folder)
        self.repo = repo
        os.chdir(self.repo.working_dir)

    def _install_requirements(self, requirements: list or str):
        subprocess.run(f"pip install --upgrade pip".split(), stdout=subprocess.PIPE)
        if not isinstance(requirements, (str, list)):
            return
        if isinstance(requirements, str):
            requirements_file = f"{self.repo.working_dir}/{requirements}"
            subprocess.run(
                ["pip", "install", "-r", requirements_file], stdout=subprocess.PIPE
            )
            return
        for requirement in requirements:
            subprocess.run(f"pip install {requirement}".split(), stdout=subprocess.PIPE)

    def _start_tunnel(self):
        active_tunnels = ngrok.get_tunnels()
        for tunnel in active_tunnels:
            public_url = tunnel.public_url
            ngrok.disconnect(public_url)
        url = ngrok.connect(port=self.port, options={"bind_tls": True})
        print(f"Hosted Server can be accessed on: {url}")


class SimpleHttpServer(Host):
    """Class to expose simple file server application.

    Parameters:

        port : int, optional
    """

    def __init__(self, port: int = 1000):
        super().__init__(port)
        self._start_server()

    def _start_server(self):
        subprocess.run(
            f"python -m http.server {self.port}".split(), stdout=subprocess.PIPE
        )


class JupyterNotebook(Host):
    """Class to expose Jupyter Notebook IDE on browser.

    Parameters:

        port : int, optional

        requirements : List[str], optional
            Defaults to `["notebook"]` and you can include
            other packages to include with this. For example
            notebook extension, theme, etc
    """

    def __init__(self, port: int = 1000, requirements: list = ["notebook"]):
        super().__init__(port, requirements)
        self._start_server()

    def _start_server(self):
        subprocess.run(
            f"python -m jupyter notebook --allow-root --ip=0.0.0.0 --port {self.port}".split(),
            stdout=subprocess.PIPE,
        )


class JupyterLab(Host):
    """Class to expose Jupyter Lab IDE on browser.

    Parameters:

        port : int, optional

        requirements : List[str], optional
            Defaults to `["jupyterlab"]` and you can include
            other packages to include with this. For example
            notebook extension, theme, etc
    """

    def __init__(self, port: int = 1000, requirements: list = ["jupyterlab"]):
        super().__init__(port, requirements)
        self._start_server()

    def _start_server(self):
        subprocess.run(
            f"python -m jupyter lab --allow-root --ip=0.0.0.0 --port {self.port}".split(),
            stdout=subprocess.PIPE,
        )


class FlaskApp(Host):
    """Class to expose python Flask or Gunicorn application.

    Parameters:

        port : int, optional

        app : str, optional
            Definition of your python gunicorn app. (Defaults to `"main:app"`).
        git_url : str, optional
            Git URL to clone your repo containing application.
            (Defaults to `"https://github.com/PuneethaPai/colab_host_flask_demo"`).
        requirements_file: str, optional
            Name of file in repo `git_url` containing requirements for hosting the
            application. (Defaults to `"requirements.txt"`).
    """

    def __init__(
        self,
        port: int = 1000,
        app="main:app",
        git_url="https://github.com/PuneethaPai/colab_host_flask_demo",
        requirements_file: str = "requirements.txt",
    ):
        self.port = port
        self.app = app
        super().__init__(port, requirements_file, git_url)
        self._start_server()

    def _start_server(self):
        subprocess.run(
            f"gunicorn --bind 0.0.0.0:{self.port} {self.app}".split(),
            stdout=subprocess.PIPE,
        )


class UvicornApp(Host):
    """Class to expose python FastApi or Uvicorn application.

    Parameters:

        port : int, optional

        app : str, optional
            Definition of your python gunicorn app. (Defaults to `"main:app"`).
        git_url : str, optional
            Git URL to clone your repo containing application.
            (Defaults to `"https://github.com/PuneethaPai/colab_host_uvicorn_demo"`).
        requirements_file: str, optional
            Name of file in repo `git_url` containing requirements for hosting the
            application. (Defaults to `"requirements.txt"`).
    """

    def __init__(
        self,
        port: int = 1000,
        app="main:app",
        git_url="https://github.com/PuneethaPai/colab_host_flask_demo",
        requirements_file: str = "requirements.txt",
    ):
        self.port = port
        self.app = app
        super().__init__(port, requirements_file, git_url)
        self._start_server()

    def _start_server(self):
        subprocess.run(
            f"uvicorn --host 0.0.0.0 --port {self.port} {self.app}".split(),
            stdout=subprocess.PIPE,
        )
