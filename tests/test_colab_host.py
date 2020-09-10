#!/usr/bin/env python
import pytest
from colab_host import colab_host


def test_sample_function():
    assert "Hello World!" == colab_host.hello()
    assert "Hello Puneeth!" == colab_host.hello("Puneeth")