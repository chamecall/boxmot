from glob import glob
from setuptools import setup, find_packages, Extension

setup(
    name='boxmot',
    packages=find_packages(),
    python_requires='>=3.9',
    install_requires=['numpy'],
    zip_safe=False
)
