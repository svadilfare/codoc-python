from setuptools import setup

setup(
    name="codoc",
    version="0.1",
    author="Casper Weiss Bang",
    author_email="casper@svadilfare.dev",
    url="https://codoc.org/",
    packages=["codoc"],
    install_requires=[
        "requests==2.25.1",
    ],
)
