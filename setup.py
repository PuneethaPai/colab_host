#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()


install_requires = ["pyngrok>=4"]
setup(
    author="Puneetha Pai",
    author_email="puneethapai29@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Host any python application in colab environment..",
    entry_points={
        "console_scripts": [
            "colab_host=colab_host.cli:main",
        ],
    },
    install_requires=install_requires,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="colab_host",
    name="colab_host",
    packages=find_packages(include=["colab_host", "colab_host.*"]),
    url="https://github.com/PuneethaPai/colab_host",
    version="0.1.2",
    zip_safe=False,
)
