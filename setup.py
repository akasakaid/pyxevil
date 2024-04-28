import os
from setuptools import setup

long_description = open("README.md").read()

about = {}
current_dir = os.path.dirname(__file__)
_version = os.path.join(current_dir, "src", "pyxevil", "__version__.py")
with open(_version, "r") as r:
    exec(r.read(), about)

setup(
    name=about["__title__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=about["__url__"],
    install_requires=[
        "requests",
    ],
    packages=["pyxevil"],
    package_dir={"": "src"},
    python_requires=">=3.8",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
    ],
)