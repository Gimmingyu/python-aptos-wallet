import io
from setuptools import setup, find_packages


def long_description():
    """

    :rtype: str
    """
    with io.open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme


setup(
    name='python_aptos_wallet',
    version='0.1',
    description='Implementation of Aptos HD Wallet in Python',
    long_description=long_description(),
    author='primrose',
    packages=find_packages(),
    zip_safe=False,
)

