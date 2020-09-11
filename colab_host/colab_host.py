import subprocess
from pyngrok import ngrok


def hello(name: str = None) -> str:
    return f"""Hello {name if name else "World"}!"""


class Host:
    def __init__(self, port: int, requirements: list = None):
        super().__init__()
        self.port = port
        self._install_requirements(requirements)
        self._start_tunnel()

    def _install_requirements(self, requirements: list):
        subprocess.run(f"pip install --upgrade pip".split(), stdout=subprocess.PIPE)
        if not requirements:
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
