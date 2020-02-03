import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="dsalgo",
    version="1.0.0",
    description="Data Structures and Algorithms implemented in Python",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/alzed/dsalgo",
    author="alzed",
    license="GNU",
    packages=["reader"],
    include_package_data=True,
)