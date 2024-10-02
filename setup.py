# setup.py
from setuptools import setup, find_packages

setup(
    name="train_ml_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'scikit-learn',
    ],
    entry_points={
        'console_scripts': [
            'train_model=train_ml_package.training:train_model',
        ],
    },
)