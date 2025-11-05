"""
Setup script for the CLI application.
"""
from setuptools import setup

setup(
    name="test-cli",
    version="1.0.0",
    description="A simple CLI application",
    author="test-public-2-rename",
    py_modules=["cli"],
    entry_points={
        "console_scripts": [
            "test-cli=cli:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
