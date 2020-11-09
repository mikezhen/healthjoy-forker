from setuptools import find_packages, setup

setup(
    name='forker',
    version='0.0.1',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'Flask>=1.1.2',
        'requests>=2.24.0',
    ]
)