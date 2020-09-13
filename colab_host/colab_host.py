import subprocess
from pyngrok import ngrok
from git import Repo
import regex as re
import os
import shutil
from pathlib import Path


def hello(name: str = None) -> str:
    return f"""Hello {name if name else "World"}!"""


class Host:
    def __init__(self, port: int, requirements: list or str = None):
        super().__init__()
        self.port = port
        self._install_requirements(requirements)
        self._start_tunnel()

    def _install_requirements(self, requirements: list or str):
        subprocess.run(f"pip install --upgrade pip".split(), stdout=subprocess.PIPE)
        if not isinstance(requirements, (str, list)):
            return
        if isinstance(requirements, str):
            subprocess.run(
                ["pip", "install", "-r", requirements], stdout=subprocess.PIPE
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
        print(f"Code Server can be accessed on: {url}")


class SimpleHttpServer(Host):
    def __init__(self, port: int, requirements: list = None):
        super().__init__(port, requirements)
        self._start_server()

    def _start_server(self):
        subprocess.run(
            f"python -m http.server {self.port}".split(), stdout=subprocess.PIPE
        )


class JupyterNotebook(Host):
    def __init__(self, port: int, requirements: list = ["notebook"]):
        super().__init__(port, requirements)
        self._start_server()

    def _start_server(self):
        subprocess.run(
            f"python -m jupyter notebook --allow-root --ip=0.0.0.0 --port {self.port}".split(),
            stdout=subprocess.PIPE,
        )


class JupyterLab(Host):
    def __init__(self, port: int, requirements: list = ["jupyterlab"]):
        super().__init__(port, requirements)
        self._start_server()

    def _start_server(self):
        subprocess.run(
            f"python -m jupyter lab --allow-root --ip=0.0.0.0 --port {self.port}".split(),
            stdout=subprocess.PIPE,
        )


class FlaskApp(Host):
    def __init__(
        self,
        port: int = 1000,
        app="main:app",
        git_url="https://github.com/PuneethaPai/colab_host_flask_demo",
        requirements_file: str = "requirements.txt",
    ):
        self.port = port
        self.app = app
        self._clone_repo(git_url)
        requirements_file = f"{self.repo.working_dir}/{requirements_file}"
        super().__init__(port, requirements_file)
        self._start_server()

    def _start_server(self):
        subprocess.run(
            f"gunicorn --bind 0.0.0.0:{self.port} {self.app}".split(),
            stdout=subprocess.PIPE,
        )

    def _clone_repo(self, git_url) -> Repo:
        subprocess.run("pip install GitPython".split(), stdout=subprocess.PIPE)
        folder_name = re.search(r"[^/]+$", git_url).group().replace(".git", "")
        folder = Path(folder_name)
        if folder.exists() and folder.is_dir():
            shutil.rmtree(folder)
        repo = Repo.clone_from(git_url, folder)
        self.repo = repo
        os.chdir(self.repo.working_dir)
