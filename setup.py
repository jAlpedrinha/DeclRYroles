from setuptools import setup, find_packages
from io import open

setup(
    name='DeclRYRoles',
    version='0.1.01',
    author='Jorge Alpedrinha Ramos',
    author_email='jalpedrinharamos@gmail.com',
    packages=find_packages(),
    package_data = { '': ['*.yml']},
    license='LICENSE.txt',
    description='D(ecl)RY permissions engine.',
    long_description=open('README.rst').read(),
    install_requires=[
    ],
)
