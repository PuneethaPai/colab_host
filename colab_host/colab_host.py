"""Main module."""


def hello(name: str = None) -> str:
    return f"""Hello {name if name else "World"}!"""
