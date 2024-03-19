from setuptools import setup, find_packages

setup(
    name="quickcli",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "quickcli=quickcli.cli_app:app",
        ],
    },
    install_requires=[
        "pydantic==2.6.4",
        "requests==2.31.0",
    ],
)
