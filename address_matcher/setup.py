from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='address_matcher',
    version='0.1.0',
    description='A tool for matching Indian addresses',
    author='Karan Choudhary',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'address_matcher=src.cli:main',
        ],
    },
    install_requires=requirements,
    python_requires='>=3.6',
) 