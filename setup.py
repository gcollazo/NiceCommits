import os
from setuptools import setup

setup(
    name = "NiceCommits",
    version = "0.0.1",
    author = "Giovanni Collazo",
    author_email = "gio@24veces.com",
    description = "Split commit messages in title and body",
    license = "MIT",
    keywords = "github commit message split",
    url = "http://github.com/gcollazo/NiceCommits",
    long_description="Super simple thing to extract title and body of a multiline commit, based on Github's Shiny new commit styles",
    classifiers=[
        "Development Status :: 3 - Alpha",
    ],
)