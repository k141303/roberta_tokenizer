from glob import glob
from os.path import basename, sep
from os.path import splitext

from setuptools import setup
from setuptools import find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name="roberta_tokenizer",
    version="1.0.2",
    description="RoBERTa Tokenizer",
    author="k141303",
    url="https://github.com/k141303/roberta_tokenizer",
    packages=["roberta_tokenizer", "roberta_tokenizer.tokenizer"],
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=_requires_from_file('requirements.txt'),
)
