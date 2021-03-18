from setuptools import setup

setup(
    name="codocpy",
    version="0.1",
    author="Casper Weiss Bang",
    author_email="casper@svadilfare.dev",
    url="https://codoc.org/",
    packages=["codoc"],
    install_requires=["requests==2.25.1", "fire==0.4.0"],
    python_requires="!=2.*, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    entry_points={
        # Install a script as "codocpy"
        "console_scripts": [
            "codocpy = codoc.entrypoints.cli:_main",
        ],
    },
)
