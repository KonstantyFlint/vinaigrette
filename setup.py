from setuptools import setup, find_packages

setup(
    name="vinaigrette",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "vinaigrette=scripts.app:app",
        ],
    },
)