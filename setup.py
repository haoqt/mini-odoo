from setuptools import setup, find_packages

setup(
    name="mini-odoo",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer>=0.9",
    ],
    entry_points={
        "console_scripts": [
            "mini-odoo=mini_odoo.cli:app",
        ],
    },
)