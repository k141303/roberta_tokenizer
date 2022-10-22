from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup
from setuptools import find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="roberta_tokenizer",
    version="1.0.0",
    description="RoBERTa Tokenizer",
    author="k141303",
    url="https://github.com/k141303/roberta_tokenizer",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    install_requires=_requires_from_file('requirements.txt'),
)
